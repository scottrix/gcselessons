#!/usr/bin/env python3
"""P0-4: Board-notes box + gcserevise cross-links for every gcselessons lesson."""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
GCSEREVISE = '/home/scott/src/gcserevise'

ALIAS = {}
for d in ['ad-art-craft-design', 'ad-fine-art', 'ad-graphic-communication', 'ad-photography',
          'ad-textile-design', 'ad-three-dimensional-design', 'art-and-design-general']:
    ALIAS[d] = 'art-and-design'
for d in ['ah-athens', 'ah-exam-technique', 'ah-greece', 'ah-persian-wars', 'ah-rome-emperors',
          'ah-rome-republic', 'ancient-history-general']:
    ALIAS[d] = 'ancient-history'
for d in ['ast-exploration', 'ast-galaxies-cosmology', 'ast-observation', 'ast-planet-earth',
          'astronomy-general', 'ast-solar-system', 'ast-stars']:
    ALIAS[d] = 'astronomy'
for d in ['bs-finance', 'bs-human-resources', 'bs-influences', 'bs-marketing', 'bs-operations',
          'bs-real-world', 'business-general']:
    ALIAS[d] = 'business'
for d in ['cc-city-rome', 'cc-exam-technique', 'cc-homeric-world', 'cc-military-rome',
          'cc-mythology', 'cc-religion', 'classical-civilisation-general', 'roman-civilisation']:
    ALIAS[d] = 'classical-civilisation'
for d in ['ci-active-citizenship', 'ci-british-values', 'ci-global-citizenship', 'ci-law-justice',
          'ci-politics-participation', 'ci-rights-responsibilities', 'citizenship-studies-general']:
    ALIAS[d] = 'citizenship-studies'
for d in ['combined-biology', 'combined-chemistry', 'combined-general', 'combined-physics']:
    ALIAS[d] = 'combined-science'
for d in ['algorithms', 'computer-science-general', 'computer-systems', 'cyber-security',
          'databases-impacts', 'data-representation', 'networks', 'programming']:
    ALIAS[d] = 'computer-science'
for d in ['dance-appreciation', 'dance-choreography', 'dance-dance-contexts', 'dance-exam-technique',
          'dance-general', 'dance-performance-skills', 'dance-professional-works']:
    ALIAS[d] = 'dance'
for d in ['dr-design-and-technical', 'dr-devising', 'dr-live-theatre', 'dr-performing-texts',
          'dr-practitioners', 'dr-theatrical-terms', 'drama-general', 'modern']:
    ALIAS[d] = 'drama'
for d in ['dt-core-principles', 'dt-designing-and-making', 'dt-materials', 'dt-specialist-technical',
          'design-and-technology-general']:
    ALIAS[d] = 'design-and-technology'
for d in ['ec-economy', 'ec-foundations', 'ec-global', 'ec-government', 'ec-markets',
          'economics-general', 'ec-producers']:
    ALIAS[d] = 'economics'
for d in ['elec-analogue-systems', 'elec-applications', 'elec-digital-systems', 'elec-exam-technique',
          'elec-fundamentals', 'elec-practical-circuits', 'electronics-general']:
    ALIAS[d] = 'electronics'
for d in ['eng-materials', 'eng-modern-tech', 'eng-practical', 'eng-processes', 'eng-systems',
          'eng-testing', 'engineering-general']:
    ALIAS[d] = 'engineering'
for d in ['english-language-general', 'english-reading', 'english-writing', 'spelling', 'analysis',
          'reading', 'writing-creative', 'writing-transactional']:
    ALIAS[d] = 'english-language'
for d in ['english-literature-general', 'nineteenth-century', 'poetry', 'shakespeare', 'writing']:
    ALIAS[d] = 'english-literature'
for d in ['film-exam-technique', 'film-film-language', 'film-genres', 'film-global-film',
          'film-studies-general', 'film-uk-film', 'film-us-film']:
    ALIAS[d] = 'film-studies'
for d in ['fn-cooking-techniques', 'fn-food-choice', 'fn-food-provenance', 'fn-food-safety',
          'fn-food-science', 'fn-nutrition-health', 'food-preparation-nutrition-general']:
    ALIAS[d] = 'food-preparation-nutrition'
ALIAS['french-general'] = 'french'
for d in ['customs-festivals', 'free-time-activities', 'grammar', 'healthy-living',
          'identity-relationships', 'media-technology', 'travel-tourism', 'education-work',
          'environment-living', 'celebrity-culture']:
    ALIAS[d] = 'french'
for d in ['geographical-applications', 'geographical-skills', 'geography-general', 'natural-hazards',
          'living-world', 'physical-landscapes-uk', 'urban-issues', 'resource-management']:
    ALIAS[d] = 'geography'
for d in ['geo-applied-geology', 'geo-earth-structure', 'geo-geological-time', 'geology-general',
          'geo-minerals-rocks', 'geo-surface-processes', 'geo-tectonics']:
    ALIAS[d] = 'geology'
ALIAS['german-general'] = 'german'
for d in ['gm-celebrity-culture', 'gm-customs-festivals', 'gm-education-work', 'gm-environment-living',
          'gm-free-time-activities', 'gm-grammar', 'gm-healthy-living', 'gm-identity-relationships',
          'gm-media-technology', 'gm-travel-tourism']:
    ALIAS[d] = 'german'
for d in ['elizabethan-england', 'germany-1890-1945', 'health-and-people', 'history-general',
          'inter-war-years']:
    ALIAS[d] = 'history'
ALIAS['latin-general'] = 'latin'
for d in ['exam-technique-latin', 'latin-language', 'latin-literature-prose', 'latin-literature-verse',
          'translation-skills']:
    ALIAS[d] = 'latin'
for d in ['law-civil-law', 'law-criminal-law', 'law-english-legal-system', 'law-exam-technique',
          'law-general', 'law-justice-law-reform', 'law-rights-responsibilities']:
    ALIAS[d] = 'law'
for d in ['ms-creating-media', 'ms-key-concepts', 'ms-media-audiences', 'ms-media-forms',
          'ms-media-industries', 'ms-media-representations', 'media-studies-general']:
    ALIAS[d] = 'media-studies'
for d in ['mu-aos1-western-classical', 'mu-aos2-popular-music', 'mu-aos3-traditional-music',
          'mu-aos4-classical-since-1910', 'mu-composing', 'mu-elements', 'mu-performing',
          'music-general']:
    ALIAS[d] = 'music'
for d in ['applied-anatomy-physiology', 'health-fitness-wellbeing', 'movement-analysis', 'pe-general',
          'physical-training', 'socio-cultural-influences', 'sports-psychology']:
    ALIAS[d] = 'pe'
for d in ['ps-approaches', 'ps-cognition', 'ps-communication', 'ps-neuro', 'ps-problems',
          'ps-social', 'psychology-general']:
    ALIAS[d] = 'psychology'
for d in ['christianity-beliefs', 'christianity-practices', 'islam-beliefs', 'islam-practices',
          'religion-crime-punishment', 'religion-life', 'religion-peace-conflict',
          'religious-studies-general']:
    ALIAS[d] = 'religious-studies'
for d in ['so-crime', 'so-education', 'so-families', 'so-foundations', 'so-research-methods',
          'so-stratification', 'sociology-general']:
    ALIAS[d] = 'sociology'
ALIAS['spanish-general'] = 'spanish'
for d in ['sp-celebrity-culture', 'sp-customs-festivals', 'sp-education-work', 'sp-environment-living',
          'sp-free-time-activities', 'sp-grammar', 'sp-healthy-living', 'sp-identity-relationships',
          'sp-media-technology', 'sp-travel-tourism']:
    ALIAS[d] = 'spanish'
for d in ['stats-calculation', 'stats-collection', 'stats-exam-technique', 'stats-interpretation',
          'stats-planning', 'stats-presentation', 'statistics']:
    ALIAS[d] = 'statistics'
for d in ['algebra', 'geometry', 'number', 'probability', 'quantitative', 'ratio',
          'mathematics-general']:
    ALIAS[d] = 'mathematics'
for d in ['atomic-structure', 'atmosphere', 'bonding', 'chem-analysis', 'chem-general',
          'chemical-changes', 'energy-changes', 'organic', 'quantitative', 'rate', 'resources',
          'analysis']:
    ALIAS[d] = 'chemistry'
for d in ['bioenergetics', 'cell-biology', 'ecology', 'homeostasis', 'infection', 'inheritance',
          'organisation']:
    ALIAS[d] = 'biology'
for d in ['physics-atomic', 'physics-electricity', 'physics-energy', 'physics-forces',
          'physics-general', 'physics-magnetism', 'physics-particle', 'physics-waves']:
    ALIAS[d] = 'physics'

SPEC_CODES = {
    'biology': {'AQA': '8461', 'Edexcel': '1BI0', 'OCR': 'J247', 'CCEA': 'units'},
    'chemistry': {'AQA': '8462', 'Edexcel': '1CH0', 'OCR': 'J248', 'CCEA': 'units'},
    'physics': {'AQA': '8463', 'Edexcel': '1PH0', 'OCR': 'J249', 'CCEA': 'units'},
    'combined-science': {'AQA': '8464', 'Edexcel': '1SC0', 'OCR': 'J250', 'CCEA': 'units'},
    'mathematics': {'AQA': '8300', 'Edexcel': '1MA1', 'OCR': 'J560', 'Eduqas': 'C300', 'CCEA': 'M-units'},
    'english-language': {'AQA': '8700', 'Edexcel': '1EN0', 'OCR': 'J351', 'Eduqas': 'C700', 'CCEA': 'units'},
    'english-literature': {'AQA': '8702', 'Edexcel': '1ET0', 'OCR': 'J352', 'Eduqas': 'C720', 'CCEA': 'units'},
    'history': {'AQA': '8145', 'Edexcel': '1HI0', 'OCR': 'J410', 'Eduqas': 'routes', 'CCEA': 'units'},
    'geography': {'AQA': '8035', 'Edexcel': '1GB0', 'OCR': 'J384', 'Eduqas': 'A/B', 'CCEA': 'units'},
    'religious-studies': {'AQA': '8062', 'Edexcel': '1RB0', 'OCR': 'J625', 'Eduqas': 'A/B', 'CCEA': 'units'},
    'business': {'AQA': '8132', 'Edexcel': '1BS0', 'OCR': 'J204', 'Eduqas': 'comps', 'CCEA': 'units'},
    'economics': {'AQA': '8136', 'Edexcel': '1EC0', 'OCR': 'papers', 'CCEA': 'units'},
    'psychology': {'AQA': '8182', 'Edexcel': '1PS0', 'OCR': 'J203'},
    'sociology': {'AQA': '8192', 'Eduqas': 'comps', 'OCR': 'J696'},
    'citizenship-studies': {'AQA': '8100', 'Edexcel': '1CS0', 'OCR': 'J270'},
    'computer-science': {'AQA': '8525', 'Edexcel': '1CP2', 'OCR': 'J277', 'Eduqas': 'on-screen+theory'},
    'design-and-technology': {'AQA': '8552', 'Edexcel': '1DT0', 'OCR': 'J310', 'Eduqas': 'comps', 'CCEA': 'units'},
    'food-preparation-nutrition': {'AQA': '8585', 'Edexcel': '1FN0', 'OCR': 'J309', 'Eduqas': 'comps'},
    'pe': {'AQA': '8582', 'Edexcel': '1PE0', 'OCR': 'J587', 'Eduqas': 'comps', 'CCEA': 'units'},
    'music': {'AQA': '8271', 'Edexcel': '1MU0', 'OCR': 'J536', 'Eduqas': 'comps', 'CCEA': 'units'},
    'drama': {'AQA': '8261', 'Edexcel': '1DR0', 'OCR': 'J316', 'Eduqas': 'comps', 'CCEA': 'units'},
    'media-studies': {'AQA': '8572', 'Edexcel': '1MS0', 'OCR': 'J200', 'Eduqas': 'comps'},
    'art-and-design': {'AQA': '8201-06', 'Edexcel': '1AD0', 'OCR': 'J170', 'Eduqas': 'comps', 'CCEA': 'units'},
    'french': {'AQA': '8652', 'Edexcel': '1FR0', 'Eduqas': 'units', 'CCEA': 'units'},
    'spanish': {'AQA': '8692', 'Edexcel': '1SP0', 'Eduqas': 'units', 'CCEA': 'units'},
    'german': {'AQA': '8662', 'Edexcel': '1GN0', 'Eduqas': 'units', 'CCEA': 'units'},
    'latin': {'OCR': 'J282', 'Eduqas': 'language+literature', 'AQA': 'language+literature'},
    'law': {'AQA': '4160 (withdrawn - foundation content for A-Level Law)'},
    'ancient-history': {'OCR': 'J198'},
    'classical-civilisation': {'OCR': 'J199'},
    'astronomy': {'Edexcel': '1AS0'},
    'geology': {'Eduqas': 'GCSE Geology'},
    'electronics': {'Eduqas': 'GCSE Electronics'},
    'film-studies': {'Eduqas': 'GCSE Film Studies'},
    'dance': {'AQA': '8236'},
    'engineering': {'AQA': '8852', 'Edexcel': '1EG0', 'CCEA': 'units'},
    'statistics': {'AQA': '8382', 'Edexcel': '1ST0', 'CCEA': 'units'},
}
BOARDS_ORDER = ['AQA', 'Edexcel', 'OCR', 'Eduqas', 'CCEA']


def find_crosslink(subject, code):
    if not code:
        if os.path.exists(f'{GCSEREVISE}/{subject}.html'):
            return f'/gcserevise/{subject}.html', f'all {subject} topics'
        return None
    for hit in sorted(glob.glob(f'{GCSEREVISE}/topics/{subject}/*/{re.escape(code)}-*.html')):
        rel = os.path.relpath(hit, GCSEREVISE)
        return f'/gcserevise/{rel}', os.path.basename(hit)[:-5]
    if os.path.exists(f'{GCSEREVISE}/{subject}.html'):
        return f'/gcserevise/{subject}.html', f'all {subject} topics'
    return None


def main():
    subjects = json.load(open(os.path.join(ROOT, 'subjects.json')))['subjects']
    smeta = {s['id']: s for s in subjects}
    only = sys.argv[1:] or sorted(ALIAS)
    n = 0
    unresolved = []
    for unit in only:
        subj = ALIAS.get(unit)
        if not subj:
            unresolved.append(unit)
            continue
        boards = smeta.get(subj, {}).get('boards', BOARDS_ORDER)
        boards = [b for b in BOARDS_ORDER if b in boards] or boards
        codes = {b: SPEC_CODES.get(subj, {}).get(b) for b in boards}
        codes = {b: c for b, c in codes.items() if c}
        bl = ' | '.join(f'<strong>{b}</strong> {c}' if c else f'<strong>{b}</strong>'
                        for b, c in sorted(codes.items(), key=lambda kv: BOARDS_ORDER.index(kv[0])))
        for path in glob.glob(os.path.join(ROOT, 'topics', unit, '*.html')):
            base = os.path.basename(path)
            code = re.match(r'([A-Za-z]+\d+)-', base)
            link, label = find_crosslink(subj, code.group(1) if code else None)
            if not link:
                unresolved.append(unit + '/' + base)
                continue
            h = open(path, encoding='utf-8').read()
            if 'Board Notes & Revision Links' in h:
                continue
            box = ('<section class="section">\n<h2>Board Notes & Revision Links</h2>\n'
                   '<div class="board-diff">\n'
                   f'<p>This lesson is examined by: {bl}. Tier and paper details vary - always check '
                   'your board\'s current specification.</p>\n'
                   f'<p>Follow-up revision: <a href="{link}">{label}</a> on GCSE Revise '
                   '(notes, flashcards and auto-graded target tests for this exact topic).</p>\n'
                   '</div>\n</section>')
            m = re.search(r'<h2[^>]*>\s*Homework & Consolidation</h2>', h)
            if m:
                h = h[:m.start()] + box + '\n' + h[m.start():]
            else:
                i = h.find('</main>')
                if i == -1:
                    continue
                h = h[:i] + box + '\n' + h[i:]
            open(path, 'w', encoding='utf-8').write(h)
            n += 1
    print(f'board-notes boxes added: {n}')
    if unresolved:
        print('unresolved:', unresolved[:10])


if __name__ == '__main__':
    main()
