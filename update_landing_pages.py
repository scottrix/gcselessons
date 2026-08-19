#!/usr/bin/env python3
"""Update all subject landing pages with affiliate content."""

import os
import re

BASE = "/home/scott/src/gcselessons"

# Subject-specific Amazon search terms
SUBJECT_AFFILIATES = {
    "mathematics": [
        ("Scientific Calculators", "scientific+calculator+GCSE", "Essential for GCSE Maths exams"),
        ("Graph Paper Pads", "graph+paper+a4+pad", "A4 squared paper for maths"),
        ("Maths Revision Guides", "GCSE+Maths+revision+guides", "CGP and other revision guides"),
    ],
    "biology": [
        ("Biology Revision Guides", "GCSE+Biology+revision+guides", "CGP, Oxford, and more"),
        ("Microscope Slides", "microscope+slides+prepared", "Prepared slides for biology practicals"),
        ("Lab Coats", "lab+coat+student", "Protection for practical work"),
    ],
    "chemistry": [
        ("Chemistry Revision Guides", "GCSE+Chemistry+revision+guides", "CGP, Oxford, and more"),
        ("Molecular Model Kits", "molecular+model+kit+organic", "Visualise chemical structures"),
        ("Periodic Table Posters", "periodic+table+poster+large", "Wall reference for chemistry"),
    ],
    "physics": [
        ("Physics Revision Guides", "GCSE+Physics+revision+guides", "CGP, Oxford, and more"),
        ("Data Loggers", "data+logger+physics+education", "For required practicals"),
        ("Multimeters", "digital+multimeter+student", "Essential for electricity practicals"),
    ],
    "english-language": [
        ("English Language Guides", "GCSE+English+Language+revision", "CGP, York Notes, and more"),
        ("Set Text Editions", "GCSE+English+set+texts", "Annotated editions for study"),
        ("Highlighters & Pens", "highlighter+pens+study", "For text annotation"),
    ],
    "english-literature": [
        ("Literature Study Guides", "GCSE+English+Literature+guides", "York Notes, CGP, and more"),
        ("Set Text Collections", "GCSE+English+Literature+set+texts", "Complete play/novel editions"),
        ("Annotation Sticky Notes", "sticky+notes+annotation", "For text analysis"),
    ],
    "combined-science": [
        ("Combined Science Guides", "GCSE+Combined+Science+revision", "Trilogy and Synergy guides"),
        ("Science Revision Cards", "GCSE+science+flashcards", "Quick revision cards"),
        ("Required Practical Workbooks", "GCSE+science+required+practical+workbook", "Lab book for practicals"),
    ],
    "computer-science": [
        ("CS Revision Guides", "GCSE+Computer+Science+revision", "CGP, PG Online, and more"),
        ("Python Books", "python+programming+GCSE", "Beginner to advanced Python"),
        ("Raspberry Pi Kits", "raspberry+pi+starter+kit", "For programming projects"),
    ],
    "history": [
        ("History Revision Guides", "GCSE+History+revision+guides", "Topic-specific guides"),
        ("Timeline Wall Charts", "history+timeline+poster", "Visual reference for chronology"),
        ("Source Analysis Workbooks", "GCSE+history+source+analysis", "Practice source questions"),
    ],
    "geography": [
        ("Geography Revision Guides", "GCSE+Geography+revision+guides", "CGP, Oxford, and more"),
        ("Atlas", "world+atlas+student", "Essential for map skills"),
        ("Case Study Flashcards", "GCSE+geography+case+study+cards", "Key facts for case studies"),
    ],
    "religious-studies": [
        ("RS Revision Guides", "GCSE+Religious+Studies+revision", "Christianity, Islam, and more"),
        ("Holy Text Extracts", "bible+quran+extracts+study", "For quotation learning"),
        ("Ethics Workbooks", "GCSE+religious+studies+ethics", "Theme-based practice"),
    ],
    "french": [
        ("French Revision Guides", "GCSE+French+revision+guides", "AQA, Edexcel, Eduqas"),
        ("French Dictionaries", "french+english+dictionary+student", "Collins, Oxford, Larousse"),
        ("Verb Conjugation Books", "french+verb+conjugation+guide", "Bescherelle and alternatives"),
    ],
    "spanish": [
        ("Spanish Revision Guides", "GCSE+Spanish+revision+guides", "AQA, Edexcel, Eduqas"),
        ("Spanish Dictionaries", "spanish+english+dictionary+student", "Collins, Oxford, Larousse"),
        ("Verb Practice Books", "spanish+verb+practice+GCSE", "Conjugation drills"),
    ],
    "german": [
        ("German Revision Guides", "GCSE+German+revision+guides", "AQA, Edexcel, Eduqas"),
        ("German Dictionaries", "german+english+dictionary+student", "Collins, Oxford, Langenscheidt"),
        ("Grammar Workbooks", "german+grammar+workbook+GCSE", "Cases, word order, verbs"),
    ],
    "latin": [
        ("Latin Revision Guides", "GCSE+Latin+revision+guides", "OCR, Eduqas, Edexcel"),
        ("Latin Dictionaries", "latin+dictionary+student", "Pocket Oxford, Cassell's"),
        ("Set Text Editions", "GCSE+Latin+set+texts+edition", "Annotated Virgil, Cicero"),
    ],
    "art-and-design": [
        ("Art Sketchbooks", "A3+sketchbook+art+student", "Quality paper for portfolio"),
        ("Drawing Pencils Set", "drawing+pencils+graphite+set", "2H to 8B range"),
        ("Watercolour Sets", "watercolour+paint+set+student", "Winsor & Newton, Daler-Rowney"),
    ],
    "music": [
        ("Music Theory Guides", "GCSE+Music+theory+guide", "ABRSM, Trinity, GCSE"),
        ("Manuscript Paper", "music+manuscript+paper+a4", "For composition practice"),
        ("Revision Audio", "GCSE+music+listening+revision", "Set works recordings"),
    ],
    "drama": [
        ("Drama Revision Guides", "GCSE+Drama+revision+guides", "Set text analysis, devising"),
        ("Script Collections", "plays+GCSE+drama+set+texts", "Published play editions"),
        ("Performance Journals", "drama+rehearsal+journal", "Track devising process"),
    ],
    "dance": [
        ("Dance Revision Guides", "GCSE+Dance+revision+guides", "Anthology, choreography"),
        ("Dancewear", "dance+leotard+tights+student", "Black leotard, footless tights"),
        ("Performance DVDs", "professional+dance+works+DVD", "Anthology works recordings"),
    ],
    "design-and-technology": [
        ("DT Revision Guides", "GCSE+Design+Technology+revision", "Core and specialist"),
        ("Sketching Pens", "fineliner+pens+technical+drawing", "0.1mm to 0.8mm"),
        ("Model Making Materials", "foam+board+balsa+wood+modelling", "For prototype making"),
    ],
    "food-preparation-nutrition": [
        ("Food Revision Guides", "GCSE+Food+Preparation+Nutrition+revision", "Recipe, nutrition, science"),
        ("Digital Scales", "digital+kitchen+scales+accurate", "Precise weighing for NEA"),
        ("Cooking Equipment", "student+cooking+utensils+set", "Pans, knives, thermometers"),
    ],
    "pe": [
        ("PE Revision Guides", "GCSE+PE+revision+guides", "Anatomy, training, psychology"),
        ("Heart Rate Monitors", "heart+rate+monitor+chest+strap", "For training analysis"),
        ("Sports Science Books", "sports+science+introduction", "Physiology, biomechanics"),
    ],
    "business": [
        ("Business Revision Guides", "GCSE+Business+revision+guides", "CGP, Tutor2u, and more"),
        ("Case Study Books", "GCSE+business+case+studies", "Real business examples"),
        ("Financial Calculators", "financial+calculator+student", "For finance topics"),
    ],
    "economics": [
        ("Economics Revision Guides", "GCSE+Economics+revision+guides", "Micro and macro"),
        ("Economics Textbooks", "GCSE+Economics+textbook", "Core textbooks"),
        ("Graph Paper", "economics+graph+paper+a4", "For diagrams"),
    ],
    "psychology": [
        ("Psychology Revision Guides", "GCSE+Psychology+revision+guides", "Studies, theories, methods"),
        ("Research Methods Workbooks", "psychology+research+methods+GCSE", "Experiments, ethics"),
        ("Study Cards", "psychology+flashcards+GCSE", "Key studies and theories"),
    ],
    "sociology": [
        ("Sociology Revision Guides", "GCSE+Sociology+revision+guides", "Families, education, crime"),
        ("Sociology Textbooks", "GCSE+Sociology+textbook", "Core concepts and theorists"),
        ("Essay Planning Pads", "essay+planning+pad+a4", "Structure long answers"),
    ],
    "citizenship-studies": [
        ("Citizenship Guides", "GCSE+Citizenship+revision+guides", "Active citizenship, law"),
        ("Campaigning Guides", "how+to+campaign+guide", "For active citizenship project"),
        ("UK Politics Books", "british+politics+introduction", "Parliament, democracy"),
    ],
    "media-studies": [
        ("Media Revision Guides", "GCSE+Media+Studies+revision", "Key concepts, industries"),
        ("Media Theory Books", "media+theory+introduction", "Barthes, Baudrillard, etc."),
        ("Production Equipment", "video+camera+student+beginner", "For NEA production"),
    ],
    "film-studies": [
        ("Film Revision Guides", "GCSE+Film+Studies+revision", "US, UK, global film"),
        ("Film Analysis Books", "film+analysis+introduction", "Mise-en-scène, editing"),
        ("Screenwriting Software", "screenwriting+software+student", "Final Draft alternatives"),
    ],
    "engineering": [
        ("Engineering Revision Guides", "GCSE+Engineering+revision+guides", "Materials, processes"),
        ("Technical Drawing Tools", "technical+drawing+set+student", "Set squares, compasses"),
        ("CAD Software Guides", "fusion+360+tutorial+book", "For CAD NEA"),
    ],
    "statistics": [
        ("Statistics Revision Guides", "GCSE+Statistics+revision+guides", "Data, probability, inference"),
        ("Statistical Calculators", "scientific+calculator+statistics", "With stats functions"),
        ("Graph Paper", "statistics+graph+paper+a4", "For charts and diagrams"),
    ],
    "electronics": [
        ("Electronics Revision Guides", "GCSE+Electronics+revision+guides", "Circuits, systems"),
        ("Component Kits", "electronics+component+kit+student", "Resistors, capacitors, ICs"),
        ("Soldering Stations", "soldering+iron+station+student", "For practical circuits"),
    ],
    "astronomy": [
        ("Astronomy Revision Guides", "GCSE+Astronomy+revision+guides", "Edexcel specification"),
        ("Planispheres", "planisphere+star+chart", "Night sky reference"),
        ("Binoculars", "astronomy+binoculars+10x50", "For observation"),
    ],
    "geology": [
        ("Geology Revision Guides", "GCSE+Geology+revision+guides", "Eduqas specification"),
        ("Rock/Mineral Kits", "rock+mineral+collection+kit", "Hand specimens"),
        ("Field Equipment", "geology+hammer+hand+lens", "For fieldwork"),
    ],
    "ancient-history": [
        ("Ancient History Guides", "GCSE+Ancient+History+revision", "Greece, Rome, Persia"),
        ("Source Books", "ancient+history+source+book", "Primary sources in translation"),
        ("Timeline Charts", "ancient+history+timeline+poster", "Chronological reference"),
    ],
    "classical-civilisation": [
        ("Class Civ Guides", "GCSE+Classical+Civilisation+revision", "Myth, religion, culture"),
        ("Homer Translations", "iliad+odyssey+translation+student", "Penguin, Oxford Classics"),
        ("Mythology Guides", "greek+roman+mythology+guide", "Gods, heroes, stories"),
    ],
    "law": [
        ("Law Revision Guides", "GCSE+Law+revision+guides", "AQA specification"),
        ("Case Law Books", "english+legal+system+cases", "Key cases and principles"),
        ("Statute Books", "statute+book+student", "Key legislation"),
    ],
    "dance": [
        ("Dance Revision Guides", "GCSE+Dance+revision+guides", "Anthology, performance"),
        ("Dancewear", "dance+leotard+student", "Black leotard, tights"),
        ("Performance Recordings", "professional+dance+works+video", "Anthology pieces"),
    ],
    "film-studies": [
        ("Film Revision Guides", "GCSE+Film+Studies+revision", "US, UK, global film"),
        ("Film Analysis Books", "film+analysis+introduction", "Mise-en-scène, editing"),
        ("Screenwriting Software", "screenwriting+software+student", "Final Draft alternatives"),
    ],
}

# Default affiliates for subjects not in the dict
DEFAULT_AFFILIATES = [
    ("GCSE Revision Guides", "GCSE+revision+guides", "All subjects covered"),
    ("Study Stationery", "study+stationery+student", "Pens, highlighters, flashcards"),
    ("Revision Timetable", "revision+timetable+planner", "Plan your study schedule"),
]

def get_affiliates(subject_id):
    return SUBJECT_AFFILIATES.get(subject_id, DEFAULT_AFFILIATES)

def build_affiliate_cards(subject_id):
    affiliates = get_affiliates(subject_id)
    cards = []
    for title, search, desc in affiliates:
        cards.append(f'''                <a href="https://www.amazon.co.uk/s?k={search}&tag=scottrix-21" class="affiliate-card" target="_blank" rel="nofollow noopener">
                    <div class="affiliate-card-title">{title}</div>
                    <div class="affiliate-card-desc">{desc}</div>
                    <div class="affiliate-card-store"><img src="../images/assets/amazon-smile.svg" alt="Amazon"> amazon.co.uk</div>
                </a>''')
    return "\n".join(cards)

def build_ad_right_sidebar(subject_id):
    affiliates = get_affiliates(subject_id)
    cards = []
    for title, search, desc in affiliates[:3]:  # Only 3 for sidebar
        cards.append(f'''        <a href="https://www.amazon.co.uk/s?k={search}&tag=scottrix-21" class="affiliate-card" target="_blank" rel="nofollow noopener">
        <div class="affiliate-card-title">{title}</div>
        <div class="affiliate-card-desc">{desc}</div>
        <div class="affiliate-card-store"><img src="../images/assets/amazon-smile.svg" alt="Amazon"> amazon.co.uk</div>
        </a>''')
    return "\n".join(cards)

def update_landing_page(filepath, subject_id):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # 1. Add fastmail/dynadot topbar after hero section (after </section> of hero)
    # Find the hero section end
    fastmail_topbar = '''
<a class="fastmail-topbar" data-banner="fastmail" href="https://join.fastmail.com/0d63b2d52105" target="_blank" rel="noopener"><img src="../images/assets/FM Billboard 970x250.png" alt="Fastmail" loading="lazy"></a>
<a class="fastmail-topbar" data-banner="dynadot" href="https://www.dynadot.com/?ref=scottrix" target="_blank" rel="nofollow noopener" hidden><img src="../images/assets/dynadot-banner.jpg" alt="Dynadot — register a new domain, web hosting, SSL" loading="lazy" onerror="this.parentElement.style.display='none';document.querySelector('[data-banner=fastmail]').hidden=false"></a>
<script>(function(){var fm=document.querySelector('[data-banner=fastmail]');var dd=document.querySelector('[data-banner=dynadot]');if(Math.random()<0.5){fm.hidden=true;dd.hidden=false}})();</script>'''
    
    # Insert after hero section (look for </section> after hero)
    # Hero section has class="hero"
    hero_end = content.find('</section>', content.find('class="hero"'))
    if hero_end != -1:
        insert_pos = hero_end + len('</section>')
        content = content[:insert_pos] + fastmail_topbar + content[insert_pos:]
    
    # 2. Add affiliate CTA section before </main>
    affiliate_cta = f'''
    <section class="section affiliate-cta-end">
    <h3>Support Your Teaching</h3>
    <p>Find essential resources for teaching {subject_id.replace('-', ' ').title()} at home.</p>
    <div class="cta-links">
        <a href="https://www.amazon.co.uk/s?k=GCSE+{subject_id.replace('-', '+')}+books&tag=scottrix-21" class="cta-link" target="_blank" rel="nofollow noopener">GCSE {subject_id.replace('-', ' ').title()} Books →</a>
        <a href="https://www.amazon.co.uk/s?k=GCSE+{subject_id.replace('-', '+')}+revision&tag=scottrix-21" class="cta-link" target="_blank" rel="nofollow noopener">Revision Guides →</a>
    </div>
    </section>'''
    
    main_end = content.find('</main>')
    if main_end != -1:
        content = content[:main_end] + affiliate_cta + content[main_end:]
    
    # 3. Add ad-right sidebar before </main> (after affiliate-cta-end)
    ad_right = f'''
    <aside class="ad-right">
{build_ad_right_sidebar(subject_id)}
        <a href="https://join.fastmail.com/0d63b2d52105" class="affiliate-card" target="_blank" rel="nofollow noopener">
        <div class="affiliate-card-title">Fastmail — Private Email</div>
        <div class="affiliate-card-desc">Privacy-first email with no ads and no tracking</div>
        <div class="affiliate-card-store">fastmail.com</div>
        </a>
        <a href="https://www.dynadot.com/?ref=scottrix" class="affiliate-card" target="_blank" rel="nofollow noopener">
        <div class="affiliate-card-title">Dynadot — Domain Registration →</div>
        <div class="affiliate-card-desc">Register or transfer domains with free SSL and affordable pricing</div>
        <div class="affiliate-card-store">dynadot.com</div>
        </a>
        <a href="https://zen.mention-me.com/m/ol/yv3qsjix-scott-harrison" class="affiliate-card" target="_blank" rel="nofollow noopener">
        <div class="affiliate-card-title">Zen Internet — UK Broadband →</div>
        <div class="affiliate-card-desc">Award-winning UK broadband with no data caps and great customer service</div>
        <div class="affiliate-card-store">zen.co.uk</div>
        </a>
    </aside>'''
    
    main_end = content.find('</main>')
    if main_end != -1:
        content = content[:main_end] + ad_right + content[main_end:]
    
    # 4. Add affiliate-images.js script before </body>
    body_end = content.find('</body>')
    if body_end != -1:
        content = content[:body_end] + '<script src="../affiliate-images.js"></script>\n' + content[body_end:]
    
    # 5. Add affiliate disclaimer to footer
    footer_affiliate = '<p>This site contains affiliate links. We may earn a commission if you purchase through these links.</p>'
    footer_pos = content.find('<footer class="site-footer">')
    if footer_pos != -1:
        # Find first </p> in footer
        footer_end = content.find('</p>', footer_pos)
        if footer_end != -1:
            insert_pos = footer_end + len('</p>')
            content = content[:insert_pos] + footer_affiliate + content[insert_pos:]
    
    with open(filepath, 'w') as f:
        f.write(content)

def main():
    for filename in os.listdir(BASE):
        if filename.endswith('.html') and filename not in ['index.html', 'privacy.html']:
            subject_id = filename[:-5]
            filepath = os.path.join(BASE, filename)
            update_landing_page(filepath, subject_id)
            print(f"Updated {filename}")

if __name__ == '__main__':
    main()
