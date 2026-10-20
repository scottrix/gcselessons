#!/usr/bin/env python3
"""Generic P0-1 filler: fill gcselessons lesson brackets from the matching gcserevise
lesson (any subject) using the unit->subject alias map."""
import glob
import html as H
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from board_notes import ALIAS

GC = '/home/scott/src/gcselessons'
GVR = '/home/scott/src/gcserevise/topics'


def strip_tags(s):
    s = re.sub(r'<[^>]+>', '', s)
    return re.sub(r'\s+', ' ', H.unescape(s)).strip()


def sections(html):
    out = {}
    for m in re.finditer(r'<section class="section">\s*<h2>([^<]+)</h2>(.*?)(?=<section class="section">|\Z)', html, re.DOTALL):
        out[m.group(1).strip()] = m.group(2)
    return out


def find_gv(subj, slug):
    for hit in glob.glob(f'{GVR}/{subj}/*/{slug}.html') + glob.glob(f'{GVR}/{subj}/{slug}.html'):
        if 'http-equiv="refresh"' not in open(hit, encoding='utf-8', errors='replace').read(600):
            return hit
    return None


def parse_gv(path):
    h = open(path, encoding='utf-8').read()
    secs = sections(h)
    d = {'keyfacts': [], 'we': [], 'errors': [], 'links': ''}
    kf = secs.get('📌 Key Facts to Memorise', '')
    d['keyfacts'] = [strip_tags(x) for x in re.findall(r'<li>(.*?)</li>', kf, re.DOTALL)][:6]
    we = (secs.get('🧮 Worked Examples — Exam Style', '') + secs.get('🧮 Worked Examples — Harder Exam Style', '')
          + secs.get('🔬 Case Study Focus — ', ''))
    if not we:
        # humanities-style: use the first content section's paragraphs as the "example"
        for k, v in secs.items():
            if k.startswith(('📋', '📝', '⚗', '🌍', '⚡')):
                ps = [strip_tags(p) for p in re.findall(r'<p>(.*?)</p>', v, re.DOTALL) if len(strip_tags(p)) > 80]
                if ps:
                    d['we'].append({'q': ps[0][:200], 'steps': ' '.join(ps[1:3]), 'marks': 'Evidence cited from the lesson content.'})
                    break
    for m in re.finditer(r'<div class="example">(.*?)</div>', we, re.DOTALL):
        blk = m.group(1)
        ps = re.findall(r'<p>(.*?)</p>', blk, re.DOTALL)
        if not ps:
            continue
        q = strip_tags(ps[0])
        steps = ' '.join(strip_tags(p) for p in ps[1:-1]) if len(ps) > 2 else ''
        marks = strip_tags(ps[-1]) if ps else ''
        d['we'].append({'q': q, 'steps': steps, 'marks': marks})
    err = secs.get('⚠️ Common Errors', '')
    d['errors'] = [strip_tags(x) for x in re.findall(r'<li>(.*?)</li>', err, re.DOTALL)][:4]
    ex = secs.get('🗺️ In the Exam', '')
    m = re.search(r'Links to:([^<.]+)', strip_tags(ex))
    d['links'] = strip_tags(m.group(1)) if m else ''
    return d


def fill(path, gv, prev_t, next_t, title):
    h = open(path, encoding='utf-8').read()
    we = gv['we']
    w1 = we[0] if we else None
    w2 = we[1] if len(we) > 1 else w1
    w3 = we[2] if len(we) > 2 else w2
    kf0 = gv['keyfacts'][0] if gv['keyfacts'] else title
    vocab = ', '.join(re.findall(r'<strong>([^<]+)</strong>', ' '.join(gv['keyfacts'])[:500])) or title
    outcome = (w1['q'][0].lower() + w1['q'][1:]).rstrip('.?') if w1 else f'deliver the {title} lesson confidently'
    prior = gv['links'].split(',')[0].strip() if gv['links'] else 'the previous lesson in this unit'
    q1 = w1['q'] if w1 else f'A standard exam question on {title}.'
    q2 = w2['q'] if w2 else f'A multi-step question on {title}.'
    q3 = w3['q'] if w3 else f'Apply {title} to an unfamiliar context.'
    concept = re.sub(r'^[A-Za-z]+\d+\s*', '', kf0)[:60]
    fills = {
        '[specific outcome]': f'by the end you can {outcome}, using the method shown step by step',
        '[prior topic]': prior,
        '[link]': "you'll reuse its method throughout today's work",
        '[bolded terms]': vocab,
        '[everyday example]': f'{(w1["q"].rstrip("?") if w1 else title)} - a real example worked through in full',
        '[Command word]': ((re.match(r'^(\w+)', w1['q']).group(1) if w1 and re.match(r'^(\w+)', w1['q']) else 'Explain')),
        '[Key facts]': '; '.join(gv['keyfacts'][:2]),
        '[Working]': w1['steps'] if w1 else 'Work through the steps shown in the lesson content.',
        '[Units/sense]': 'Check the units named in the question and sense-check the size of your answer.',
        '[With units]': (w1['steps'].split('=')[-1].strip().rstrip('.') if w1 and '=' in w1['steps'] else 'State the complete final answer.'),
        '[Detail]': w2['steps'][:300] if w2 else 'Solve each part in turn, showing working.',
        '[How they fit]': 'The parts chain: each answer feeds the next step of the question.',
        '[Complete]': w2['marks'] if w2 else 'State the complete final answer.',
        '[concept]': concept,
        '[Relevant analogy]': (w1['q'].rstrip('?') if w1 else title),
        '[hands-on activity]': 're-draw or re-write the worked example from memory, then check it against the model answer',
        '[prev/next topic]': f'{prev_t or "the previous lesson"} / {next_t or "the next lesson"}',
    }
    for k, v in fills.items():
        h = h.replace(k, v)
    h = re.sub(r'\[Typical exam question on [^\]]*\]', q1, h)
    h = re.sub(r'\[Harder question[^\]]*\]', q2, h)
    h = re.sub(r'\[Graph/table interpretation\]', q3, h)
    h = re.sub(r'\[Exam question[^\]]*\]', q1, h)
    if gv['errors'] and 'Common Errors (Mark-Scheme View)' not in h:
        lis = ''.join(f'<li>{e}</li>' for e in gv['errors'])
        box = ('<section class="section">\n<h2>Common Errors (Mark-Scheme View)</h2>\n'
               f'<ul>{lis}</ul>\n</section>')
        m = re.search(r'<h2[^>]*>\s*Board Notes & Revision Links</h2>', h)
        if m:
            h = h[:m.start()] + box + '\n' + h[m.start():]
    open(path, 'w', encoding='utf-8').write(h)


def main():
    n = 0
    skipped = []
    for path in sorted(glob.glob(f'{GC}/topics/*/*.html')):
        h = open(path, encoding='utf-8', errors='replace').read()
        if '[specific outcome]' not in h:
            continue
        unit = path.split('/')[-2]
        slug = os.path.basename(path)[:-5]
        subj = ALIAS.get(unit)
        gvpath = find_gv(subj, slug) if subj else None
        if not gvpath:
            skipped.append(unit + '/' + slug)
            continue
        gv = parse_gv(gvpath)
        title = re.search(r'<title>([^:<]+)', h).group(1).strip()
        unit_dir = os.path.dirname(path)
        sibs = sorted(os.path.basename(x)[:-5] for x in glob.glob(f'{unit_dir}/*.html'))
        i = sibs.index(slug)
        prev_t = sibs[i - 1] if i > 0 else None
        next_t = sibs[i + 1] if i + 1 < len(sibs) else None
        fill(path, gv, prev_t, next_t, title)
        n += 1
    print(f'filled: {n} lessons')
    print(f'still unfilled (no gcserevise source): {len(skipped)}')
    from collections import Counter
    c = Counter(s.split('/')[0] for s in skipped)
    print('by unit:', dict(c))


if __name__ == '__main__':
    main()
