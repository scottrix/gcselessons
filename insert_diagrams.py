#!/usr/bin/env python3
"""P0-2: Insert inline SVG diagrams + draw-along boxes into STEM lessons."""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

# ===== SVG generators =====

def svg_cell():
    return '''<svg viewBox="0 0 400 250" xmlns="http://www.w3.org/2000/svg" width="100%" max-width="400">
<style>text{font-family:sans-serif;font-size:11px;fill:#333} .lbl{font-weight:bold}</style>
<ellipse cx="200" cy="125" rx="170" ry="100" fill="#e8f5e9" stroke="#4caf50" stroke-width="2"/>
<ellipse cx="200" cy="125" rx="60" ry="45" fill="#bbdefb" stroke="#1565c0" stroke-width="2"/>
<circle cx="180" cy="115" r="15" fill="#1e88e5" stroke="#0d47a1" stroke-width="1"/>
<circle cx="220" cy="130" r="12" fill="#1e88e5" stroke="#0d47a1" stroke-width="1"/>
<circle cx="200" cy="140" r="14" fill="#1e88e5" stroke="#0d47a1" stroke-width="1"/>
<rect x="280" y="80" width="60" height="30" fill="#fff9c4" stroke="#f9a825" rx="5"/>
<rect x="90" y="150" width="50" height="25" fill="#fff9c4" stroke="#f9a825" rx="5"/>
<line x1="260" y1="125" x2="300" y2="125" stroke="#f9a825" stroke-width="3"/>
<line x1="260" y1="135" x2="290" y2="135" stroke="#f9a825" stroke-width="3"/>
<line x1="260" y1="115" x2="290" y2="115" stroke="#f9a825" stroke-width="3"/>
<text x="200" y="125" text-anchor="middle" class="lbl">Nucleus</text>
<text x="310" y="98" class="lbl">Mitochondria</text>
<text x="85" y="145" class="lbl">Ribosomes</text>
<text x="200" y="38" text-anchor="middle">Cell membrane</text>
<line x1="200" y1="30" x2="200" y2="24" stroke="#666"/>
<text x="200" y="225" text-anchor="middle">Cytoplasm</text>
</svg>'''

def svg_circuit():
    return '''<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg" width="100%" max-width="400">
<style>text{font-family:sans-serif;font-size:11px;fill:#333} .lbl{font-weight:bold}</style>
<rect x="40" y="40" width="320" height="120" fill="none" stroke="#333" stroke-width="2"/>
<rect x="170" y="30" width="60" height="20" fill="#fff" stroke="#333" stroke-width="2"/>
<text x="200" y="25" text-anchor="middle" class="lbl">Cell/Battery</text>
<circle cx="200" cy="160" r="20" fill="#fff" stroke="#333" stroke-width="2"/>
<line x1="186" y1="160" x2="200" y2="146" stroke="#333" stroke-width="2"/>
<line x1="200" y1="174" x2="214" y2="160" stroke="#333" stroke-width="2"/>
<text x="200" y="195" text-anchor="middle" class="lbl">Ammeter (A)</text>
<rect x="30" y="90" width="20" height="14" fill="#fff" stroke="#333" stroke-width="2"/>
<text x="15" y="100" text-anchor="end" class="lbl">Voltmeter</text>
<rect x="350" y="90" width="14" height="20" fill="#fff" stroke="#333" stroke-width="2"/>
<text x="370" y="105" class="lbl">Resistor</text>
<circle cx="40" cy="40" r="3" fill="#333"/><circle cx="360" cy="40" r="3" fill="#333"/>
<circle cx="40" cy="160" r="3" fill="#333"/><circle cx="360" cy="160" r="3" fill="#333"/>
</svg>'''

def svg_wave():
    return '''<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg" width="100%" max-width="400">
<style>text{font-family:sans-serif;font-size:11px;fill:#333} .lbl{font-weight:bold}</style>
<line x1="30" y1="100" x2="370" y2="100" stroke="#999" stroke-dasharray="5,5"/>
<path d="M30,100 Q80,20 130,100 T230,100 T330,100 T430,100" fill="none" stroke="#1565c0" stroke-width="2.5"/>
<line x1="30" y1="20" x2="30" y2="100" stroke="#e53935" stroke-width="1" stroke-dasharray="3,3"/>
<text x="35" y="18" fill="#e53935">Amplitude</text>
<line x1="30" y1="185" x2="230" y2="185" stroke="#2e7d32" stroke-width="1"/>
<line x1="30" y1="180" x2="30" y2="190" stroke="#2e7d32"/>
<line x1="230" y1="180" x2="230" y2="190" stroke="#2e7d32"/>
<text x="130" y="198" text-anchor="middle" fill="#2e7d32" class="lbl">Wavelength (λ)</text>
<text x="380" y="60" class="lbl">Crest</text>
<text x="180" y="150" class="lbl">Trough</text>
</svg>'''

def svg_force():
    return '''<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg" width="100%" max-width="400">
<style>text{font-family:sans-serif;font-size:11px;fill:#333} .lbl{font-weight:bold}</style>
<rect x="150" y="80" width="100" height="60" fill="#e3f2fd" stroke="#1565c0" stroke-width="2" rx="5"/>
<text x="200" y="115" text-anchor="middle">Object</text>
<line x1="150" y1="110" x2="60" y2="110" stroke="#e53935" stroke-width="3" marker-end="url(#arrR)"/>
<text x="55" y="100" text-anchor="end" fill="#e53935" class="lbl">Thrust 50N →</text>
<line x1="250" y1="110" x2="340" y2="110" stroke="#e53935" stroke-width="3"/>
<text x="345" y="100" fill="#e53935" class="lbl">← Friction 30N</text>
<line x1="200" y1="80" x2="200" y2="30" stroke="#2e7d32" stroke-width="3"/>
<text x="205" y="28" fill="#2e7d32" class="lbl">Normal ↑</text>
<line x1="200" y1="140" x2="200" y2="190" stroke="#f57f17" stroke-width="3"/>
<text x="205" y="195" fill="#f57f17" class="lbl">↓ Weight (mg)</text>
</svg>'''

def svg_atom():
    return '''<svg viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg" width="100%" max-width="300">
<style>text{font-family:sans-serif;font-size:11px;fill:#333} .lbl{font-weight:bold}</style>
<circle cx="150" cy="150" r="30" fill="#ffcc80" stroke="#e65100" stroke-width="2"/>
<text x="150" y="155" text-anchor="middle" class="lbl">Nucleus</text>
<text x="150" y="168" text-anchor="middle" font-size="9">p⁺ n⁰</text>
<circle cx="150" cy="150" r="80" fill="none" stroke="#90caf9" stroke-width="1.5" stroke-dasharray="6,3"/>
<circle cx="230" cy="150" r="6" fill="#1565c0"/>
<circle cx="70" cy="150" r="6" fill="#1565c0"/>
<circle cx="150" cy="70" r="6" fill="#1565c0"/>
<circle cx="150" cy="230" r="6" fill="#1565c0"/>
<text x="240" y="140" class="lbl">Electron e⁻</text>
<text x="150" y="285" text-anchor="middle">Electron shell</text>
</svg>'''

def svg_numberline():
    return '''<svg viewBox="0 0 400 80" xmlns="http://www.w3.org/2000/svg" width="100%" max-width="400">
<style>text{font-family:sans-serif;font-size:12px;fill:#333}</style>
<line x1="30" y1="40" x2="370" y2="40" stroke="#333" stroke-width="2"/>
<line x1="30" y1="34" x2="30" y2="46" stroke="#333"/><line x1="370" y1="34" x2="370" y2="46" stroke="#333"/>
<text x="30" y="60" text-anchor="middle">-5</text><text x="100" y="60" text-anchor="middle">-3</text>
<text x="170" y="60" text-anchor="middle">-1</text><text x="200" y="60" text-anchor="middle">0</text>
<text x="270" y="60" text-anchor="middle">2</text><text x="370" y="60" text-anchor="middle">5</text>
<line x1="100" y1="34" x2="100" y2="46" stroke="#333"/><line x1="170" y1="34" x2="170" y2="46" stroke="#333"/>
<line x1="200" y1="34" x2="200" y2="46" stroke="#333"/><line x1="270" y1="34" x2="270" y2="46" stroke="#333"/>
<circle cx="200" cy="40" r="5" fill="#1565c0"/>
</svg>'''

def svg_graph():
    return '''<svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg" width="100%" max-width="400">
<style>text{font-family:sans-serif;font-size:11px;fill:#333} .lbl{font-weight:bold}</style>
<line x1="50" y1="250" x2="370" y2="250" stroke="#333" stroke-width="2"/>
<line x1="50" y1="250" x2="50" y2="30" stroke="#333" stroke-width="2"/>
<text x="200" y="275" text-anchor="middle" class="lbl">x</text>
<text x="30" y="140" text-anchor="middle" class="lbl">y</text>
<path d="M50,250 Q210,20 370,250" fill="none" stroke="#1565c0" stroke-width="2.5"/>
<text x="210" y="40" fill="#1565c0" class="lbl">y = x²</text>
<circle cx="50" cy="250" r="4" fill="#e53935"/>
<text x="55" y="245" fill="#e53935">Origin (0,0)</text>
<line x1="50" y1="250" x2="370" y2="250" stroke="#999" stroke-dasharray="3,3"/>
</svg>'''

def svg_foodchain():
    return '''<svg viewBox="0 0 400 100" xmlns="http://www.w3.org/2000/svg" width="100%" max-width="400">
<style>text{font-family:sans-serif;font-size:11px;fill:#333}</style>
<rect x="20" y="30" width="80" height="40" fill="#c8e6c9" stroke="#4caf50" rx="5"/>
<text x="60" y="55" text-anchor="middle">Grass</text>
<rect x="140" y="30" width="80" height="40" fill="#fff9c4" stroke="#f9a825" rx="5"/>
<text x="180" y="55" text-anchor="middle">Rabbit</text>
<rect x="260" y="30" width="80" height="40" fill="#ffccbc" stroke="#e65100" rx="5"/>
<text x="300" y="55" text-anchor="middle">Fox</text>
<line x1="100" y1="50" x2="140" y2="50" stroke="#333" stroke-width="2" marker-end="url(#arr)"/>
<line x1="220" y1="50" x2="260" y2="50" stroke="#333" stroke-width="2" marker-end="url(#arr)"/>
<text x="120" y="42" text-anchor="middle" font-size="9">eaten by</text>
<text x="240" y="42" text-anchor="middle" font-size="9">eaten by</text>
<text x="60" y="85" text-anchor="middle" font-size="9">Producer</text>
<text x="180" y="85" text-anchor="middle" font-size="9">Primary consumer</text>
<text x="300" y="85" text-anchor="middle" font-size="9">Secondary consumer</text>
</svg>'''

def svg_punnett():
    return '''<svg viewBox="0 0 300 250" xmlns="http://www.w3.org/2000/svg" width="100%" max-width="300">
<style>text{font-family:sans-serif;font-size:12px;fill:#333} .lbl{font-weight:bold}</style>
<text x="90" y="25" text-anchor="middle" class="lbl">B</text>
<text x="170" y="25" text-anchor="middle" class="lbl">b</text>
<text x="30" y="65" text-anchor="middle" class="lbl">B</text>
<text x="30" y="135" text-anchor="middle" class="lbl">b</text>
<rect x="60" y="40" width="60" height="50" fill="#c8e6c9" stroke="#333"/>
<text x="90" y="70" text-anchor="middle" class="lbl">BB</text>
<rect x="140" y="40" width="60" height="50" fill="#fff9c4" stroke="#333"/>
<text x="170" y="70" text-anchor="middle" class="lbl">Bb</text>
<rect x="60" y="110" width="60" height="50" fill="#fff9c4" stroke="#333"/>
<text x="90" y="140" text-anchor="middle" class="lbl">Bb</text>
<rect x="140" y="110" width="60" height="50" fill="#ffccbc" stroke="#333"/>
<text x="170" y="140" text-anchor="middle" class="lbl">bb</text>
<text x="150" y="185" text-anchor="middle">B = dominant (brown eyes)</text>
<text x="150" y="200" text-anchor="middle">b = recessive (blue eyes)</text>
<text x="150" y="220" text-anchor="middle">Ratio: 3 brown : 1 blue</text>
</svg>'''

def svg_heart():
    return '''<svg viewBox="0 0 300 250" xmlns="http://www.w3.org/2000/svg" width="100%" max-width="300">
<style>text{font-family:sans-serif;font-size:11px;fill:#333} .lbl{font-weight:bold}</style>
<path d="M150,220 C100,180 60,140 60,100 C60,60 90,40 120,50 C140,55 150,70 150,80 C150,70 160,55 180,50 C210,40 240,60 240,100 C240,140 200,180 150,220 Z" fill="#ffcdd2" stroke="#c62828" stroke-width="2"/>
<line x1="150" y1="80" x2="150" y2="220" stroke="#c62828" stroke-width="1" stroke-dasharray="5,3"/>
<text x="100" y="90" text-anchor="middle" class="lbl" fill="#1565c0">Right side</text>
<text x="200" y="90" text-anchor="middle" class="lbl" fill="#c62828">Left side</text>
<text x="100" y="110" text-anchor="middle" font-size="10">RA</text>
<text x="200" y="110" text-anchor="middle" font-size="10">LA</text>
<text x="100" y="170" text-anchor="middle" font-size="10">RV</text>
<text x="200" y="170" text-anchor="middle" font-size="10">LV</text>
<text x="150" y="235" text-anchor="middle" font-size="10">LV wall is thicker (pumps to whole body)</text>
</svg>'''

def svg_ratiobar():
    return '''<svg viewBox="0 0 400 100" xmlns="http://www.w3.org/2000/svg" width="100%" max-width="400">
<style>text{font-family:sans-serif;font-size:12px;fill:#333} .lbl{font-weight:bold}</style>
<rect x="20" y="25" width="120" height="50" fill="#bbdefb" stroke="#1565c0"/>
<text x="80" y="55" text-anchor="middle" class="lbl">3 parts (£30)</text>
<rect x="140" y="25" width="200" height="50" fill="#c8e6c9" stroke="#4caf50"/>
<text x="240" y="55" text-anchor="middle" class="lbl">5 parts (£50)</text>
<text x="200" y="15" text-anchor="middle">Total: 8 parts = £80 → 1 part = £10</text>
<text x="200" y="90" text-anchor="middle">Ratio 3 : 5 → Amy gets £30, Ben gets £50</text>
</svg>'''

def svg_flowchart():
    return '''<svg viewBox="0 0 300 350" xmlns="http://www.w3.org/2000/svg" width="100%" max-width="300">
<style>text{font-family:sans-serif;font-size:10px;fill:#333}</style>
<rect x="100" y="20" width="100" height="35" fill="#e3f2fd" stroke="#1565c0" rx="5"/>
<text x="150" y="42" text-anchor="middle">START</text>
<line x1="150" y1="55" x2="150" y2="80" stroke="#333" marker-end="url(#arr)"/>
<polygon points="150,80 220,115 150,150 80,115" fill="#fff9c4" stroke="#f9a825"/>
<text x="150" y="112" text-anchor="middle">Condition</text>
<text x="150" y="125" text-anchor="middle">true?</text>
<line x1="80" y1="115" x2="30" y2="115" stroke="#333"/>
<line x1="30" y1="115" x2="30" y2="180" stroke="#333" marker-end="url(#arr)"/>
<text x="55" y="108" font-size="9">Yes</text>
<line x1="220" y1="115" x2="270" y2="115" stroke="#333"/>
<line x1="270" y1="115" x2="270" y2="180" stroke="#333" marker-end="url(#arr)"/>
<text x="240" y="108" font-size="9">No</text>
<rect x="5" y="180" width="90" height="35" fill="#c8e6c9" stroke="#4caf50"/>
<text x="50" y="200" text-anchor="middle">Do A</text>
<rect x="220" y="180" width="90" height="35" fill="#ffccbc" stroke="#e65100"/>
<text x="265" y="200" text-anchor="middle">Do B</text>
</svg>'''

def svg_greenhouse():
    return '''<svg viewBox="0 0 400 250" xmlns="http://www.w3.org/2000/svg" width="100%" max-width="400">
<style>text{font-family:sans-serif;font-size:10px;fill:#333}</style>
<rect x="0" y="0" width="400" height="250" fill="#e3f2fd"/>
<rect x="0" y="200" width="400" height="50" fill="#4caf50" opacity="0.3"/>
<circle cx="330" cy="50" r="30" fill="#fff176" stroke="#f9a825" stroke-width="2"/>
<text x="330" y="55" text-anchor="middle">Sun</text>
<line x1="305" y1="70" x2="200" y2="170" stroke="#f9a825" stroke-width="2"/>
<line x1="200" y1="170" x2="180" y2="100" stroke="#e53935" stroke-width="2" marker-end="url(#arrR)"/>
<text x="130" y="90" fill="#e53935">Infrared radiation</text>
<text x="130" y="105" fill="#e53935">(trapped by greenhouse gases)</text>
<text x="200" y="220" text-anchor="middle">Earth's surface</text>
<text x="200" y="35" text-anchor="middle" fill="#546e7a">Atmosphere</text>
</svg>'''

# ===== Diagram-type to SVG mapping =====
SVGS = {
    'cell-diagram': svg_cell, 'circuit-diagram': svg_circuit, 'wave-diagram': svg_wave,
    'force-diagram': svg_force, 'atom-diagram': svg_atom, 'atom-model': svg_atom,
    'number-line': svg_numberline, 'linear-graph': svg_graph, 'geometry-shapes': svg_graph,
    'food-chain': svg_foodchain, 'punnett-square': svg_punnett, 'heart-diagram': svg_heart,
    'ratio-bar': svg_ratiobar, 'flowchart': svg_flowchart, 'greenhouse-effect': svg_greenhouse,
    'mole-diagram': svg_atom, 'bonding-diagram': svg_atom, 'energy-level': svg_graph,
    'molecule-structure': svg_atom, 'chromatography': svg_flowchart, 'reaction-diagram': svg_graph,
    'pathogen-diagram': svg_cell, 'organ-system': svg_heart, 'nervous-system': svg_flowchart,
    'ecosystem': svg_foodchain, 'river-landscape': svg_wave, 'urban-model': svg_graph,
    'plate-boundaries': svg_force, 'lever-diagram': svg_force, 'energy-transfer': svg_graph,
    'magnetic-field': svg_force, 'particle-model': svg_atom, 'probability-tree': svg_flowchart,
    'mole-calculation': svg_atom, 'rate-graph': svg_graph, 'periodic-table': svg_atom,
    'binary-diagram': svg_numberline,
}

DRAWALONG = {
    'cell-diagram': 'Draw a large oval (the cell membrane). Inside, draw a circle (nucleus) and label it. Add 3–4 bean shapes (mitochondria). Label the cytoplasm (the space around organelles).',
    'circuit-diagram': 'Draw a rectangle of connecting wire. Break the top wire and insert a battery symbol (two parallel lines). Break the bottom wire and add an ammeter circle (A). Add a resistor (rectangle) on the right side.',
    'wave-diagram': 'Draw a horizontal dashed line (rest position). Draw a smooth sine wave above and below it. Label the height from rest to crest as "amplitude". Label the distance between two crests as "wavelength (λ)".',
    'force-diagram': 'Draw a rectangle (the object). Draw arrows outward from each side: up (normal force), down (weight = mg), right (thrust), left (friction). Label each arrow with its force name and value in newtons.',
    'atom-diagram': 'Draw a central circle (nucleus) and write p+ and n0 inside. Draw a dashed circle around it (first shell). Place 2 electrons on the shell. For the second shell, place up to 8 electrons.',
    'number-line': 'Draw a horizontal line with arrowheads. Add tick marks at equal intervals. Label integers from negative (left) to positive (right). Zero is always in the middle. Mark your numbers with filled circles (≤/≥) or open circles (</>).',
    'linear-graph': 'Draw L-shaped axes. Label the x-axis (horizontal) and y-axis (vertical). Plot points from your table. Draw a straight line through them with a ruler. Label the line with its equation.',
    'geometry-shapes': 'Draw the shape using a ruler. Label all sides with their lengths. Mark equal angles with arcs. Add any parallel-line arrows. Write the formula you will use inside the shape.',
    'food-chain': 'Draw boxes left to right: producer first (green), then herbivore, then carnivore. Draw arrows BETWEEN them pointing in the direction energy flows (from eaten to eater). Label each level.',
    'punnett-square': 'Draw a 2×2 grid. Put one parent\u2019s alleles across the top (B, b). Put the other parent\u2019s alleles down the side. Fill each box by combining the row and column letters. Count the ratio of outcomes.',
    'heart-diagram': 'Draw a rough heart shape. Draw a vertical dashed line dividing left and right. Label four chambers: RA, RV (right); LA, LV (left). Note that the LV wall is thicker (pumps to the whole body).',
    'ratio-bar': 'Draw a bar divided into parts proportional to the ratio. Label each part with its value. Write the total above. The ratio tells you how many parts each person gets.',
    'greenhouse-effect': 'Draw the Earth\u2019s surface at the bottom, the atmosphere above, and the sun in the corner. Draw incoming solar radiation (yellow arrow). Draw outgoing infrared (red arrow) being trapped and re-radiated back down.',
    'flowchart': 'Draw an oval (START/END), rectangles (processes), diamonds (decisions). Connect with arrows. Decisions need Yes/No labels on the outgoing arrows.',
}


def drawalong_generic(subject):
    return (f'Draw the key diagram for {subject}: start with the main structure, add labels with arrows, '
            'then annotate with the key facts from the lesson. Use a ruler for straight lines.')


# ===== unit → diagram-type mapping =====
UNIT_MAP = {
    'cell-biology': 'cell-diagram', 'infection': 'pathogen-diagram', 'organisation': 'organ-system',
    'bioenergetics': 'photosynthesis-diagram', 'homeostasis': 'nervous-system', 'inheritance': 'punnett-square',
    'ecology': 'food-chain', 'atomic-structure': 'atom-diagram', 'bonding': 'bonding-diagram',
    'quantitative': 'mole-calculation', 'chemical-changes': 'reaction-diagram', 'energy-changes': 'energy-level',
    'atmosphere': 'greenhouse-effect', 'organic': 'molecule-structure', 'chem-analysis': 'chromatography',
    'rate': 'rate-graph', 'resources': 'water-cycle', 'chem-general': 'periodic-table',
    'physics-forces': 'force-diagram', 'physics-energy': 'energy-transfer', 'physics-waves': 'wave-diagram',
    'physics-electricity': 'circuit-diagram', 'physics-magnetism': 'magnetic-field', 'physics-atomic': 'atom-model',
    'physics-particle': 'particle-model', 'geometry': 'geometry-shapes', 'algebra': 'linear-graph',
    'probability': 'probability-tree', 'number': 'number-line', 'ratio': 'ratio-bar',
    'natural-hazards': 'plate-boundaries', 'living-world': 'ecosystem',
    'physical-landscapes-uk': 'river-landscape', 'urban-issues': 'urban-model',
    'combined-biology': 'cell-diagram', 'combined-chemistry': 'atom-diagram', 'combined-physics': 'circuit-diagram',
    'applied-anatomy-physiology': 'heart-diagram', 'movement-analysis': 'lever-diagram',
    'data-representation': 'binary-diagram', 'programming': 'flowchart',
}


def main():
    n_svg = n_da = 0
    for unit, dtype in UNIT_MAP.items():
        svg_fn = SVGS.get(dtype)
        da_text = DRAWALONG.get(dtype, drawalong_generic(unit))
        for path in sorted(glob.glob(f'topics/{unit}/*.html')):
            h = open(path, encoding='utf-8', errors='replace').read()
            if 'draw-along' in h or '<svg' in h:
                continue
            # build insertion
            svg_html = ''
            if svg_fn:
                svg = svg_fn()
                svg_html = (f'<section class="section">\n<h2>📐 Reference Diagram</h2>\n'
                            f'<div style="text-align:center">{svg}</div>\n</section>')
                n_svg += 1
            da_html = (f'<section class="section">\n<h2>✏️ Draw-Along Instructions</h2>\n'
                       f'<div class="key-point"><p><strong>Parent/teacher:</strong> {da_text}</p>'
                       '<p>Display the reference diagram (or draw it live) while pupils copy. '
                       'Check each label as it is added.</p></div>\n</section>')
            n_da += 1
            insert = svg_html + '\n' + da_html if svg_html else da_html
            # insert after the first "Main Content" h2 or after the Board Notes section
            m = re.search(r'(<h2[^>]*>\s*(?:Main Content \(35 minutes\)|Board Notes))', h)
            if m:
                # find the end of that section
                sec_end = h.find('</section>', m.start())
                if sec_end != -1:
                    h = h[:sec_end+10] + '\n' + insert + h[sec_end+10:]
            else:
                i = h.find('</main>')
                if i != -1:
                    h = h[:i] + insert + '\n' + h[i:]
            open(path, 'w', encoding='utf-8').write(h)
    print(f'SVG diagrams inserted: {n_svg} | Draw-along boxes inserted: {n_da}')


if __name__ == '__main__':
    main()
