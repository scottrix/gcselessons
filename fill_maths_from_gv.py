#!/usr/bin/env python3
"""Fill gcselessons maths lesson brackets from the matching gcserevise lesson content."""
import glob
import html as H
import os
import re
import sys

GC = '/home/scott/src/gcselessons'
GV = '/home/scott/src/gcserevise/topics/mathematics/aqa'


def strip_tags(s):
    s = re.sub(r'<[^>]+>', '', s)
    return re.sub(r'\s+', ' ', H.unescape(s)).strip()


def sections(html):
    out = {}
    for m in re.finditer(r'<section class="section">\s*<h2>([^<]+)</h2>(.*?)(?=<section class="section">|\Z)', html, re.DOTALL):
        out[m.group(1).strip()] = m.group(2)
    return out


def parse_gv(slug):
    path = f'{GV}/{slug}.html'
    if not os.path.exists(path):
        return None
    h = open(path, encoding='utf-8').read()
    secs = sections(h)
    d = {'title': slug, 'keyfacts': [], 'we': [], 'errors': [], 'links': ''}
    kf = secs.get('📌 Key Facts to Memorise', '')
    d['keyfacts'] = [strip_tags(x) for x in re.findall(r'<li>(.*?)</li>', kf, re.DOTALL)][:6]
    we = secs.get('🧮 Worked Examples — Exam Style', '') + secs.get('🧮 Worked Examples — Harder Exam Style', '')
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


def fill_gcse(path, gv, prev_t, next_t):
    h = open(path, encoding='utf-8').read()
    title = re.search(r'<title>([^:<]+)', h).group(1).strip()
    we = gv['we']
    w1 = we[0] if we else None
    w2 = we[1] if len(we) > 1 else (we[0] if we else None)
    w3 = we[2] if len(we) > 2 else w2
    kf0 = gv['keyfacts'][0] if gv['keyfacts'] else title
    vocab = ', '.join(re.findall(r'<strong>([^<]+)</strong>', ' '.join(gv['keyfacts'])[:500])) or title
    outcome = (w1['q'][0].lower() + w1['q'][1:]).rstrip('.?') if w1 else f'carry out {title} calculations accurately'
    prior = gv['links'].split(',')[0].strip() if gv['links'] else 'the previous lesson in this unit'
    link = "you'll reuse its method throughout today's work"
    analogy = (w1['q'].rstrip('?') if w1 else title)
    concept = re.sub(r'^[A-Za-z]+\d+\s*', '', kf0)[:60]
    prev_t = prev_t or 'the previous lesson'
    next_t = next_t or 'the next lesson'

    q1 = w1['q'] if w1 else f'A standard exam question on {title}.'
    q2 = w2['q'] if w2 else f'A multi-step question on {title}.'
    q3 = w3['q'] if w3 else f'Interpret the data in the context of {title}.'
    fills = {
        '[specific outcome]': f'by the end you can {outcome}, using the method shown step by step',
        '[prior topic]': prior,
        '[link]': link,
        '[bolded terms]': vocab,
        '[everyday example]': f'{analogy} - the same maths you already do when shopping or cooking',
        '[Command word]': (re.match(r'^(\w+)', w1['q']).group(1) if w1 else 'Work out'),
        '[Key facts]': '; '.join(gv['keyfacts'][:2]),
        '[Working]': w1['steps'] if w1 else 'Show every line of working.',
        '[Units/sense]': 'Check the units named in the question and sense-check the size of your answer.',
        '[With units]': (w1['steps'].split('=')[-1].strip().rstrip('.') if w1 and '=' in w1['steps'] else 'State the final answer with units.'),
        '[Detail]': w2['steps'][:300] if w2 else 'Solve each part in turn, showing working.',
        '[How they fit]': 'The parts chain: each answer feeds the next step of the question.',
        '[Complete]': w2['marks'] if w2 else 'State the complete final answer with units.',
        '[concept]': concept,
        '[Relevant analogy]': analogy,
        '[hands-on activity]': 're-draw the worked example from memory, then check it against the model answer',
        '[prev/next topic]': f'{prev_t} / {next_t}',
    }
    for k, v in fills.items():
        h = h.replace(k, v)
    # question-type brackets (case-insensitive content varies per file)
    h = re.sub(r'\[Typical exam question on [^\]]*\]', q1, h)
    h = re.sub(r'\[Harder question[^\]]*\]', q2, h)
    h = re.sub(r'\[Graph/table interpretation\]', q3, h)
    h = re.sub(r'\[Exam question[^\]]*\]', q1, h)
    # common errors box (P0-3 for this lesson)
    if gv['errors'] and 'Common Errors (Mark-Scheme View)' not in h:
        lis = ''.join(f'<li>{e}</li>' for e in gv['errors'])
        box = ('<section class="section">\n<h2>Common Errors (Mark-Scheme View)</h2>\n'
               f'<ul>{lis}</ul>\n</section>')
        m = re.search(r'<h2[^>]*>\s*Board Notes & Revision Links</h2>', h)
        if m:
            h = h[:m.start()] + box + '\n' + h[m.start():]
    open(path, 'w', encoding='utf-8').write(h)
    return True


def main():
    only = sys.argv[1:] or None
    n = 0
    for path in sorted(glob.glob(f'{GC}/topics/number/*.html') + glob.glob(f'{GC}/topics/ratio/*.html')):
        slug = os.path.basename(path)[:-5]
        if '[specific outcome]' not in open(path, encoding='utf-8', errors='replace').read():
            continue
        if only and slug not in only:
            continue
        gv = parse_gv(slug)
        if not gv:
            print('NO GCSEREVISE SOURCE:', slug)
            continue
        unit = path.split('/')[-2]
        sibs = sorted(os.path.basename(x)[:-5] for x in glob.glob(f'{GC}/topics/{unit}/*.html'))
        i = sibs.index(slug)
        prev_t = sibs[i - 1] if i > 0 else None
        next_t = sibs[i + 1] if i + 1 < len(sibs) else None
        fill_gcse(path, gv, prev_t, next_t)
        n += 1
    print(f'filled: {n} lessons')


if __name__ == '__main__':
    main()
