#!/usr/bin/env python3
"""Rebuild P0-4 cross-links with TITLE-SIMILARITY matching against gcserevise;
also fill remaining lesson brackets where a strong title match exists."""
import glob
import html as H
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from board_notes import ALIAS
from fill_from_gv_generic import parse_gv, fill

GCSEREVISE = '/home/scott/src/gcserevise'
BOARDS_ORDER = ['AQA', 'Edexcel', 'OCR', 'Eduqas', 'CCEA']


def toks(s):
    stop = {'with', 'and', 'the', 'for', 'through', 'using', 'your', 'from', 'that', 'into'}
    return {w for w in re.findall(r'[a-z]{3,}', s.lower()) if w not in stop}


def title_of(path):
    h = open(path, encoding='utf-8', errors='replace').read()
    m = re.search(r'<title>([^<]+)', h)
    if not m:
        return '', h
    t = m.group(1).split(' - ')[0].strip()
    t = re.sub(r'^[A-Za-z]+\d+\s*:\s*', '', t)
    return t, h


def build_index():
    idx = {}
    for f in glob.glob(f'{GCSEREVISE}/topics/*/*/*.html') + glob.glob(f'{GCSEREVISE}/topics/*/*.html'):
        subj = f.split(f'{GCSEREVISE}/topics/')[1].split('/')[0]
        t, h = title_of(f)
        if 'page moved' in h[:400]:
            continue
        idx.setdefault(subj, []).append((f, t, toks(t)))
    return idx


def best_match(subject, title, idx):
    cands = idx.get(subject, [])
    tt = toks(title)
    best, best_score = None, 0.0
    for entry in cands:
        f, t, tk = entry[0], entry[1], entry[2]
        if not tk or not tt:
            continue
        score = len(tt & tk) / max(1, min(len(tt), len(tk)))
        if score > best_score:
            best, best_score = (f, t), score
    return best, best_score


def rel_url(f):
    return '/gcserevise/' + os.path.relpath(f, GCSEREVISE)


def main():
    idx = build_index()
    n_rel = n_fill = 0
    weak = []
    for path in sorted(glob.glob('topics/*/*.html')):
        unit = path.split('/')[1]
        subj = ALIAS.get(unit)
        if not subj:
            continue
        h = open(path, encoding='utf-8').read()
        t1, _h = title_of(path)
        base = os.path.basename(path)[:-5]
        best, score = best_match(subj, t1, idx)
        if not best or score < 0.5:
            weak.append((unit + '/' + base, round(score, 2)))
            continue
        link, label = rel_url(best[0]), os.path.basename(best[0])[:-5]
        # 1. fix the cross-link in the Board Notes box
        m = re.search(r'(<p>Follow-up revision: <a href=")/gcserevise/[^"]+("[^<]*</a>)[^<]*(</p>)', h)
        if m:
            h = h[:m.start()] + f'<p>Follow-up revision: <a href="{link}">{label}</a> on GCSE Revise (notes, flashcards and auto-graded target tests for this exact topic).</p>' + h[m.end():]
            open(path, 'w', encoding='utf-8').write(h)
            n_rel += 1
        # 2. fill brackets if any remain (title-matched gcserevise content)
        if '[specific outcome]' in h:
            gv = parse_gv(best[0])
            if gv and gv['we']:
                unit_dir = os.path.dirname(path)
                sibs = sorted(os.path.basename(x)[:-5] for x in glob.glob(f'{unit_dir}/*.html'))
                i = sibs.index(base)
                fill(path, gv, sibs[i - 1] if i else None, sibs[i + 1] if i + 1 < len(sibs) else None, t1)
                n_fill += 1
    print(f'cross-links rebuilt: {n_rel} | brackets filled: {n_fill} | weak/no-match: {len(weak)}')
    from collections import Counter
    print('weak by unit:', dict(Counter(u.split("/")[0] for u, _ in weak)))


if __name__ == '__main__':
    main()
