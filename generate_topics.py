#!/usr/bin/env python3
"""Generate missing topic lesson pages for 4 subjects."""

import os

BASE = "/home/scott/src/gcselessons/topics"

# Computer Science topics
CS_TOPICS = {
    "algorithms": [
        ("CS1", "Algorithmic Thinking"),
        ("CS2", "Search Algorithms"),
        ("CS3", "Sorting Algorithms"),
        ("CS4", "Algorithm Efficiency"),
    ],
    "computer-systems": [
        ("CS5", "CPU Architecture"),
        ("CS6", "Memory and Storage"),
        ("CS7", "Operating Systems"),
        ("CS8", "Embedded Systems"),
    ],
    "cyber-security": [
        ("CS9", "Threats and Vulnerabilities"),
        ("CS10", "Prevention Methods"),
        ("CS11", "Encryption"),
        ("CS12", "Legal and Ethical Issues"),
    ],
    "databases-impacts": [
        ("CS13", "Database Concepts"),
        ("CS14", "SQL"),
        ("CS15", "Social Impacts"),
        ("CS16", "Environmental Impacts"),
    ],
    "data-representation": [
        ("CS17", "Binary and Hex"),
        ("CS18", "Characters and Images"),
        ("CS19", "Sound and Compression"),
        ("CS20", "Logic Gates"),
    ],
    "networks": [
        ("CS21", "Network Types"),
        ("CS22", "Protocols and Layers"),
        ("CS23", "Network Security"),
        ("CS24", "The Internet"),
    ],
    "programming": [
        ("CS25", "Programming Basics"),
        ("CS26", "Data Structures"),
        ("CS27", "Subroutines and Functions"),
        ("CS28", "Testing and Debugging"),
    ],
}

# Geography topics
GEO_TOPICS = {
    "natural-hazards": [
        ("G1", "Tectonic Hazards"),
        ("G2", "Weather Hazards"),
        ("G3", "Climate Change"),
    ],
    "living-world": [
        ("G4", "Ecosystems"),
        ("G5", "Tropical Rainforests"),
        ("G6", "Hot Deserts"),
    ],
    "physical-landscapes-uk": [
        ("G7", "Coastal Landscapes"),
        ("G8", "River Landscapes"),
        ("G9", "Glacial Landscapes"),
    ],
    "urban-issues": [
        ("G10", "Urbanisation"),
        ("G11", "Urban Change in UK"),
        ("G12", "Urban Sustainability"),
    ],
    "changing-economic-world": [
        ("G13", "Development Gap"),
        ("G14", "Nigeria Case Study"),
        ("G15", "UK Economy"),
    ],
    "resource-management": [
        ("G16", "Food Resources"),
        ("G17", "Water Resources"),
        ("G18", "Energy Resources"),
    ],
    "geographical-skills": [
        ("G19", "Cartographic Skills"),
        ("G20", "Graphical Skills"),
        ("G21", "Statistical Skills"),
    ],
    "geographical-applications": [
        ("G22", "Issue Evaluation"),
        ("G23", "Fieldwork"),
    ],
}

# History topics
HIST_TOPICS = {
    "germany-1890-1945": [
        ("H1", "Germany 1890-1918"),
        ("H2", "Weimar Republic"),
        ("H3", "Hitler's Rise"),
        ("H4", "Nazi Germany"),
        ("H5", "WWII Impact"),
    ],
    "elizabethan-england": [
        ("H6", "Elizabeth's Court"),
        ("H7", "Life in Elizabethan England"),
        ("H8", "Troubles at Home and Abroad"),
        ("H9", "Historic Environment"),
    ],
    "health-and-people": [
        ("H10", "Medieval Medicine"),
        ("H11", "Renaissance Medicine"),
        ("H12", "18th-19th Century Medicine"),
        ("H13", "Modern Medicine"),
    ],
    "inter-war-years": [
        ("H14", "Peace Treaties"),
        ("H15", "League of Nations"),
        ("H16", "Road to WWII"),
    ],
}

# Religious Studies topics
RS_TOPICS = {
    "christianity-beliefs": [
        ("RS1", "Nature of God"),
        ("RS2", "Creation"),
        ("RS3", "Jesus Christ"),
        ("RS4", "Salvation"),
    ],
    "christianity-practices": [
        ("RS5", "Worship"),
        ("RS6", "Sacraments"),
        ("RS7", "Prayer"),
        ("RS8", "Church in Community"),
    ],
    "islam-beliefs": [
        ("RS9", "Tawhid"),
        ("RS10", "Angels"),
        ("RS11", "Holy Books"),
        ("RS12", "Prophets"),
        ("RS13", "Akhirah"),
    ],
    "islam-practices": [
        ("RS14", "Five Pillars"),
        ("RS15", "Shahadah and Salah"),
        ("RS16", "Sawm and Hajj"),
        ("RS17", "Zakah and Jihad"),
    ],
    "relationships-families": [
        ("RS18", "Marriage and Divorce"),
        ("RS19", "Families"),
        ("RS20", "Gender Equality"),
    ],
    "religion-life": [
        ("RS21", "Origins of Universe"),
        ("RS22", "Sanctity of Life"),
        ("RS23", "Animal Rights"),
    ],
    "religion-peace-conflict": [
        ("RS24", "Just War"),
        ("RS25", "Pacifism"),
        ("RS26", "Terrorism"),
    ],
    "religion-crime-punishment": [
        ("RS27", "Crime and Punishment"),
        ("RS28", "Forgiveness"),
        ("RS29", "Death Penalty"),
    ],
}

SUBJECT_INFO = {
    "computer-science": {"name": "Computer Science", "emoji": "💻", "nav": "computer-science", "boards": "AQA, Edexcel, OCR, Eduqas", "tier": "Foundation and Higher"},
    "geography": {"name": "Geography", "emoji": "🌍", "nav": "geography", "boards": "AQA, Edexcel, OCR, Eduqas, CCEA", "tier": "Foundation and Higher"},
    "history": {"name": "History", "emoji": "📜", "nav": "history", "boards": "AQA, Edexcel, OCR, Eduqas, CCEA", "tier": "Foundation and Higher"},
    "religious-studies": {"name": "Religious Studies", "emoji": "☪️", "nav": "religious-studies", "boards": "AQA, Edexcel, OCR, Eduqas, CCEA", "tier": "Foundation and Higher"},
}

def lesson_content(subject_key, topic_id, topic_name, strand):
    """Generate lesson content for a topic."""
    info = SUBJECT_INFO[subject_key]
    is_practical = subject_key in ["computer-science", "geography"]
    
    lines = []
    lines.append(f'''<section class="section">
<h2>Lesson Overview</h2>
<div class="key-point">
<strong>Estimated Lessons:</strong> 3<br>
<strong>Tier:</strong> {info['tier']}<br>
<strong>Duration:</strong> 50 minutes per lesson<br>
<strong>Exam Boards:</strong> {info['boards']}
</div>
</section>

<section class="section">
<h2>Learning Objectives</h2>
<ul>
<li>Understand key concepts in {topic_name.lower()}</li>
<li>Apply knowledge to exam-style questions</li>
<li>Develop subject-specific skills</li>
</ul>
</section>

<section class="section">
<h2>Prerequisites</h2>
<ul>
<li>Basic understanding of {strand.replace('-', ' ').replace('_', ' ')}</li>
<li>Familiarity with key terminology</li>
</ul>
</section>

<section class="section">
<h2>Materials & Equipment</h2>
<ul>
<li>Textbook or specification</li>
<li>Exercise book and pen</li>
<li>Scientific calculator (if applicable)</li>''')
    
    if subject_key == "computer-science":
        lines.append("<li>Computer with IDE (Python)</li>")
    elif subject_key == "geography":
        lines.append("<li>Atlas or online maps</li>")
        lines.append("<li>Graph paper</li>")
    elif subject_key == "religious-studies":
        lines.append("<li>Religious texts (extracts provided)</li>")
    
    lines.append("</ul></section>")
    
    # 3 lessons per topic
    for lesson_num in [1, 2, 3]:
        sub_topics = {
            1: f"Introduction to {topic_name}",
            2: f"Deep Dive: {topic_name}",
            3: f"Application and Assessment: {topic_name}"
        }
        
        lines.append(f'''<section class="section">
<h2>Lesson {lesson_num}: {sub_topics[lesson_num]}</h2>
<div class="key-point"><strong>Duration:</strong> 50 minutes</div>

<h3>Starter Activity (5 minutes)</h3>
<div class="example">
<div class="example-title">Quick Recall</div>
<p>Answer 3 quick questions reviewing previous lesson / key terms from {topic_name}.</p>
</div>

<h3>Main Content (35 minutes)</h3>
<div class="key-point">
<strong>Teaching Notes:</strong><br>
Detailed explanation of {topic_name.lower()} concepts. Include key definitions, diagrams to draw, worked examples, and common misconceptions addressed.
</div>

<div class="example">
<div class="example-title">Worked Example</div>
<p>Step-by-step example showing how to approach a typical exam question on {topic_name.lower()}.</p>
</div>''')
        
        if subject_key == "computer-science":
            lines.append('''<div class="formula-box">
# Example code / pseudocode
def example():
    pass
</div>''')
        elif subject_key == "geography":
            lines.append('''<div class="formula-box">
Case study facts and figures
</div>''')
        elif subject_key == "history":
            lines.append('''<div class="formula-box">
Key dates, events, and significance
</div>''')
        elif subject_key == "religious-studies":
            lines.append('''<div class="formula-box">
Key teachings and quotations
</div>''')
        
        lines.append(f'''<div class="misconception">
<h3>Common Misconception</h3>
<p><span class="wrong">Typical student error about {topic_name.lower()}</span></p>
<p><span class="right">Correct understanding with explanation</span></p>
</div>

<h3>Differentiation</h3>
<div class="key-point">
<strong>Support:</strong><br>
Simplified resources, sentence starters, worked examples, glossary
</div>
<div class="key-point">
<strong>Stretch:</strong><br>
Extended analysis, synoptic links, evaluation of significance
</div>

<h3>Plenary (5 minutes)</h3>
<div class="example">
<div class="example-title">Exit Ticket</div>
<p>Write one key thing learned and one question you still have.</p>
</div>

<h3>Assessment Criteria</h3>
<ul>
<li><strong>Got it:</strong> Can explain {topic_name.lower()} confidently with examples</li>
<li><strong>Getting there:</strong> Understands main points but needs support with detail</li>
<li><strong>Not yet:</strong> Struggles with key concepts, needs reteaching</li>
</ul>
</section>''')
    
    lines.append(f'''<section class="section">
<h2>Homework Suggestions</h2>
<ul>
<li>Complete practice questions on {topic_name.lower()}</li>
<li>Create a revision resource (mind map / flashcards)</li>
<li>Read ahead: next topic in sequence</li>
</ul>
</section>

<section class="section">
<h2>Resources</h2>
<ul>
<li><a href="https://www.bbc.co.uk/bitesize" target="_blank" rel="noopener">BBC Bitesize - {info['name']}</a></li>
</ul>
</section>''')
    
    return "\n".join(lines)


def create_topic_page(subject_key, strand, topic_id, topic_name, lesson_num=1):
    """Create a single topic lesson page."""
    info = SUBJECT_INFO[subject_key]
    filename = f"{topic_id}-{topic_name.lower().replace(' ', '-').replace('/', '-')}.html"
    filepath = os.path.join(BASE, strand, filename)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    content = lesson_content(subject_key, topic_id, topic_name, strand)
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{topic_id}: {topic_name} - GCSE {info['name']} Lessons</title>
<meta name="description" content="{topic_id} {topic_name} - Detailed GCSE {info['name']} lesson plan for homeschooling">
<meta name="keywords" content="GCSE {info['name']}, homeschool, lesson plan, {topic_name.lower()}">
<meta property="og:title" content="{topic_name} - GCSE {info['name']} Lessons">
<meta property="og:description" content="{topic_id} {topic_name} - Detailed GCSE {info['name']} lesson plan">
<meta property="og:type" content="article">
<link rel="canonical" href="https://scottrix.github.io/gcselessons/topics/{strand}/{filename}">
<meta property="og:site_name" content="GCSE Lessons">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{topic_id}: {topic_name}">
<link rel="stylesheet" href="../../style.css">
</head>
<body>
<header class="site-header">
<div class="header-content">
<a href="../../" class="logo">📖 GCSE Lessons</a>
<nav class="nav"><a href="../../#subjects">Subjects</a> <a href="../../{info['nav']}.html">{info['name']}</a></nav>
<button id="theme-toggle" class="theme-btn">🌙</button>
</div>
</header>
<main class="topic-content">
<div class="disclaimer-banner"><strong>Homeschool Guide:</strong> These lesson plans are a guide for parents. Content may contain errors — always cross-reference with official exam board specifications.</div>

<nav class="breadcrumb"><a href="../../">Home</a> <span>›</span> <a href="../../{info['nav']}.html">{info['name']}</a> <span>›</span> <span>{topic_name}</span></nav>

<article class="topic-header">
<h1>{topic_id}: {topic_name}</h1>
<div class="topic-meta">
<span class="badge foundation">Foundation</span>
<span class="badge higher">Higher</span>
<span class="badge">All Boards</span>
</div>
<p class="topic-desc">Detailed lesson plans for {topic_name.lower()} in GCSE {info['name']}.</p>
</article>

{content}

</main>
<footer class="site-footer">
<p>GCSE Lessons - Free lesson plans for homeschooling</p>
<p>Content for educational purposes only. Always cross-reference with official specifications.</p>
<p>© 2025 | <a href="privacy.html">Privacy Policy</a> | <a href="mailto:gcselessons@scott.scottrix.co.uk">Contact</a></p>
</footer>
<script>
document.getElementById('theme-toggle').addEventListener('click', function() {{
const root = document.documentElement;
if (root.classList.contains('light-mode')) {{
root.classList.remove('light-mode');
this.textContent = '🌙';
localStorage.setItem('gcselessons-theme', 'dark');
}} else {{
root.classList.add('light-mode');
this.textContent = '☀️';
localStorage.setItem('gcselessons-theme', 'light');
}}
}});
if (localStorage.getItem('gcselessons-theme') === 'light') {{
document.documentElement.classList.add('light-mode');
document.getElementById('theme-toggle').textContent = '☀️';
}}
</script>
<script src="../../sidebar.js"></script>
</body>
</html>'''
    
    with open(filepath, 'w') as f:
        f.write(html)
    return filepath


def main():
    # Computer Science
    for strand, topics in CS_TOPICS.items():
        for i, (tid, tname) in enumerate(topics):
            create_topic_page("computer-science", strand, tid, tname)
    
    # Geography
    for strand, topics in GEO_TOPICS.items():
        for i, (tid, tname) in enumerate(topics):
            create_topic_page("geography", strand, tid, tname)
    
    # History
    for strand, topics in HIST_TOPICS.items():
        for i, (tid, tname) in enumerate(topics):
            create_topic_page("history", strand, tid, tname)
    
    # Religious Studies
    for strand, topics in RS_TOPICS.items():
        for i, (tid, tname) in enumerate(topics):
            create_topic_page("religious-studies", strand, tid, tname)
    
    print("Done generating topic pages")

if __name__ == "__main__":
    main()
