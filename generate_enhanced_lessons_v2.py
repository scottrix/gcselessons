#!/usr/bin/env python3
"""Generate enhanced detailed lesson pages - all subjects."""

import os
import re

BASE = "/home/scott/src/gcselessons"

LESSON_COUNTS = {
    "english-language": 69, "english-literature": 75, "mathematics": 237,
    "biology": 114, "chemistry": 102, "physics": 87, "combined-science": 225,
    "computer-science": 99, "history": 63, "geography": 111,
    "religious-studies": 108, "french": 117, "spanish": 117, "german": 117,
    "art-and-design": 90, "music": 105, "drama": 90, "design-and-technology": 48,
    "pe": 75, "business": 78, "economics": 78, "psychology": 60,
    "sociology": 60, "citizenship-studies": 60, "media-studies": 72,
    "food-preparation-nutrition": 72, "latin": 72, "astronomy": 78,
    "geology": 78, "ancient-history": 78, "classical-civilisation": 78,
    "law": 60, "dance": 90, "film-studies": 72, "electronics": 57,
    "engineering": 60, "statistics": 54,
}

# All subject configs
SUBJECT_CONFIGS = {
    "biology": {"name": "Biology", "nav": "biology", "boards": "AQA, Edexcel, OCR, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 5},
    "chemistry": {"name": "Chemistry", "nav": "chemistry", "boards": "AQA, Edexcel, OCR, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 5},
    "physics": {"name": "Physics", "nav": "physics", "boards": "AQA, Edexcel, OCR, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 5},
    "mathematics": {"name": "Mathematics", "nav": "mathematics", "boards": "AQA, Edexcel, OCR, Eduqas, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "english-language": {"name": "English Language", "nav": "english-language", "boards": "AQA, Edexcel, OCR, Eduqas, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "english-literature": {"name": "English Literature", "nav": "english-literature", "boards": "AQA, Edexcel, OCR, Eduqas, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "combined-science": {"name": "Combined Science", "nav": "combined-science", "boards": "AQA, Edexcel, OCR, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "computer-science": {"name": "Computer Science", "nav": "computer-science", "boards": "AQA, Edexcel, OCR, Eduqas", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "history": {"name": "History", "nav": "history", "boards": "AQA, Edexcel, OCR, Eduqas, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "geography": {"name": "Geography", "nav": "geography", "boards": "AQA, Edexcel, OCR, Eduqas, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "religious-studies": {"name": "Religious Studies", "nav": "religious-studies", "boards": "AQA, Edexcel, OCR, Eduqas, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "french": {"name": "French", "nav": "french", "boards": "AQA, Edexcel, Eduqas, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "spanish": {"name": "Spanish", "nav": "spanish", "boards": "AQA, Edexcel, Eduqas, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "german": {"name": "German", "nav": "german", "boards": "AQA, Edexcel, Eduqas, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "latin": {"name": "Latin", "nav": "latin", "boards": "Edexcel, OCR, Eduqas", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "art-and-design": {"name": "Art and Design", "nav": "art-and-design", "boards": "AQA, Edexcel, OCR, Eduqas, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "music": {"name": "Music", "nav": "music", "boards": "AQA, Edexcel, OCR, Eduqas, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "drama": {"name": "Drama", "nav": "drama", "boards": "AQA, Edexcel, OCR, Eduqas, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "dance": {"name": "Dance", "nav": "dance", "boards": "AQA", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "design-and-technology": {"name": "Design and Technology", "nav": "design-and-technology", "boards": "AQA, Edexcel, OCR, Eduqas, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "food-preparation-nutrition": {"name": "Food Preparation and Nutrition", "nav": "food-preparation-nutrition", "boards": "AQA, Edexcel, OCR, Eduqas", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "pe": {"name": "Physical Education", "nav": "pe", "boards": "AQA, Edexcel, OCR, Eduqas, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "business": {"name": "Business Studies", "nav": "business", "boards": "AQA, Edexcel, OCR, Eduqas, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "economics": {"name": "Economics", "nav": "economics", "boards": "AQA, Edexcel, OCR, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "psychology": {"name": "Psychology", "nav": "psychology", "boards": "AQA, Edexcel, OCR", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "sociology": {"name": "Sociology", "nav": "sociology", "boards": "AQA, Edexcel, Eduqas", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "citizenship-studies": {"name": "Citizenship Studies", "nav": "citizenship-studies", "boards": "AQA, Edexcel, OCR", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "media-studies": {"name": "Media Studies", "nav": "media-studies", "boards": "AQA, Edexcel, OCR, Eduqas", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "film-studies": {"name": "Film Studies", "nav": "film-studies", "boards": "Eduqas", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "astronomy": {"name": "Astronomy", "nav": "astronomy", "boards": "Edexcel", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "geology": {"name": "Geology", "nav": "geology", "boards": "Eduqas", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "ancient-history": {"name": "Ancient History", "nav": "ancient-history", "boards": "OCR", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "classical-civilisation": {"name": "Classical Civilisation", "nav": "classical-civilisation", "boards": "OCR", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "law": {"name": "Law", "nav": "law", "boards": "AQA", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "electronics": {"name": "Electronics", "nav": "electronics", "boards": "Eduqas", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "engineering": {"name": "Engineering", "nav": "engineering", "boards": "AQA, Edexcel, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 4},
    "statistics": {"name": "Statistics", "nav": "statistics", "boards": "AQA, Edexcel, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 4},
}

DEFAULT_CONFIG = {"name": "Subject", "nav": "", "boards": "AQA, Edexcel, OCR, Eduqas, CCEA", "tier": "Foundation and Higher", "lessons_per_topic": 4}

def get_subject_config(subject_id):
    return SUBJECT_CONFIGS.get(subject_id, DEFAULT_CONFIG)

THEME_SCRIPT = """document.getElementById('theme-toggle').addEventListener('click', function() {{const root=document.documentElement;if(root.classList.contains('light-mode')){{root.classList.remove('light-mode');this.textContent='🌙';localStorage.setItem('gcselessons-theme','dark');}}else{{root.classList.add('light-mode');this.textContent='☀️';localStorage.setItem('gcselessons-theme','light');}}});if(localStorage.getItem('gcselessons-theme')==='light'){{document.documentElement.classList.add('light-mode');document.getElementById('theme-toggle').textContent='☀️';}}"""

def get_subject_config(subject_id):
    return SUBJECT_CONFIGS.get(subject_id, DEFAULT_CONFIG)

def generate_lesson_content(topic_id, topic_name, subject_id, lesson_num, total_lessons):
    config = get_subject_config(subject_id)
    titles = ["Introduction", "Core Concepts", "Application & Practice", "Exam Technique", "Mastery & Extension", "Review & Assessment"]
    lesson_title = titles[min(lesson_num-1, len(titles)-1)]
    
    return f'''<h3>Starter Activity (5 minutes)</h3>
<div class="example">
<div class="example-title">{"Quick Recall" if lesson_num==1 else "Review Previous Lesson"}</div>
<p>{"3 quick questions to activate prior knowledge about " + topic_name.lower() if lesson_num==1 else "Quick recap: write 3 key points from last lesson on " + topic_name.lower()}. Use mini-whiteboard or paper.</p>
</div>

<h3>Main Content (35 minutes)</h3>

<div class="key-point">
<strong>Parent/Teacher Guide:</strong><br>
<strong>Before lesson:</strong> Read script below. Prepare materials. Pre-teach key vocab: [bolded terms].<br>
<strong>If stuck:</strong> See Troubleshooting below. Break into smaller steps.<br>
<strong>Extension:</strong> See Stretch & Challenge section.
</div>

<div class="key-point">
<strong>Teaching Script (35 mins):</strong><br>
<strong>Mins 0-5 - Hook:</strong> "Today: {topic_name}. Goal: [specific outcome]. Connects to [prior topic] because [link]."<br>
<strong>Mins 5-15 - Direct Instruction:</strong> 1) Define: "{topic_name} is..." 2) Key principle: "Most important:..." 3) Draw diagram, label live. 4) Real example: "Like [everyday example]..."<br>
<strong>Mins 15-25 - Guided Practice:</strong> Ex1: Teacher models. Ex2: Student tries with guidance. Ex3: Student independent.<br>
<strong>Mins 25-35 - Independent Practice:</strong> 3-5 questions. Immediate feedback.
</div>

<div class="example">
<div class="example-title">Worked Example 1: Basic</div>
<p><strong>Q:</strong> [Typical exam question on {topic_name.lower()}]</p>
<ol><li><strong>What is asked?</strong> [Command word]</li><li><strong>Recall knowledge:</strong> [Key facts]</li><li><strong>Apply:</strong> [Working]</li><li><strong>Check:</strong> [Units/sense]</li><li><strong>Answer:</strong> [With units]</li></ol>
<p><strong>Tip:</strong> "Show working - method marks > answer marks."</p>
</div>

<div class="example">
<div class="example-title">Worked Example 2: Multi-step</div>
<p><strong>Q:</strong> [Harder question linking {topic_name.lower()} + related topic]</p>
<ol><li><strong>Break down:</strong> Separate parts?</li><li><strong>Solve each:</strong> [Detail]</li><li><strong>Combine:</strong> [How they fit]</li><li><strong>Final answer:</strong> [Complete]</li></ol>
</div>

<div class="example">
<div class="example-title">Worked Example 3: Data/Application</div>
<p><strong>Q:</strong> [Graph/table interpretation]</p>
<ol><li><strong>Read data:</strong> Axes, units, scale</li><li><strong>Patterns:</strong> Trends, anomalies</li><li><strong>Explain:</strong> Why? Using {topic_name.lower()}</li><li><strong>Conclude:</strong> Evidence-based</li></ol>
</div>

<div class="misconception">
<h3>Common Questions & Troubleshooting</h3>
<div class="key-point"><strong>Q: "Why does [concept] work this way?"</strong><br>A: Analogy: "[Relevant analogy]". Try [hands-on activity].</div>
<div class="key-point"><strong>Q: "Wrong answers on calculations."</strong><br>A: Checklist: units? formula? calculator mode? sig figs?</div>
<div class="key-point"><strong>Q: "Can't remember key terms."</strong><br>A: Flashcards (term front, def+diagram back). Spaced repetition: day 1, 3, 7.</div>
<div class="key-point"><strong>Q: "Exam wording confuses me."</strong><br>A: Commands: Describe=what you see; Explain=reasons; Evaluate=pros/cons+judgement; Calculate=working+units.</div>
<div class="key-point"><strong>Q: "Running out of time."</strong><br>A: 1 mark/min. Skip hard, return. Attempt all - partial marks count.</div>
</div>

<h3>Assessment & Model Answers</h3>
<div class="key-point"><strong>Mastery Checklist:</strong>
<ul><li>[ ] Define {topic_name} in own words</li><li>[ ] Identify features in diagram</li><li>[ ] Explain process step-by-step</li><li>[ ] Apply to unfamiliar context</li><li>[ ] Score 80%+ on past paper question</li></ul>
</div>

<div class="extended-question">
<h3>Model Answer: Past Paper Question</h3>
<p><strong>Q:</strong> [Exam question - {config["boards"].split(",")[0]} style]</p>
<div class="model-answer">
<ul>
<li>1 mark: [Key terminology]</li><li>1 mark: [Mechanism/process]</li><li>1 mark: [Application/example]</li><li>1 mark: [Evaluation - Higher]</li>
</ul>
<p><strong>Model response:</strong> "[Complete answer with expected detail/terminology]"</p>
<p><strong>Why full marks:</strong> [What makes this strong]</p>
</div>
</div>

<div class="key-point" style="background: linear-gradient(135deg, #2d1a4a, #1a0d33); border-left-color: #bb86fc;">
<strong>Stretch & Challenge (Grade 8-9):</strong>
<ul><li>Synoptic links: Connect to [prev/next topic]</li><li>Real-world: Research use in [industry/medicine]</li><li>Advanced calc: Try [harder type]</li><li>Critical: "Evaluate limitations of today's model"</li><li>Research: Recent discovery on {topic_name.lower()}, summarise 100 words</li></ul>
</div>

<h3>Plenary (5 mins)</h3>
<div class="example"><div class="example-title">{"Label the Diagram" if lesson_num<=2 else "Exam Question Speed Round"}</div>
<p>{"Unlabelled diagram - write all parts in 1 min" if lesson_num<=2 else "5 quick questions, 1 min each. Mark together."}</p>
</div>

<h3>Assessment Criteria</h3>
<ul><li><strong>Got it:</strong> Confident explanation + correct worked examples</li><li><strong>Getting there:</strong> Main points OK, needs support with detail</li><li><strong>Not yet:</strong> Confused on key concepts, needs reteaching</li></ul>'''

def generate_topic_page(subject_id, topic_id, topic_name, strand):
    config = get_subject_config(subject_id)
    subject_name = config["name"]
    lessons_per_topic = config.get("lessons_per_topic", 4)
    
    all_lessons = ""
    for i in range(1, lessons_per_topic + 1):
        lesson_content = generate_lesson_content(topic_id, topic_name, subject_id, i, lessons_per_topic)
        all_lessons += f'''
<section class="section">
<h2>Lesson {i}: {["Introduction", "Core Concepts", "Application", "Exam Practice", "Mastery", "Review"][min(i-1,5)]}: {topic_name}</h2>
<div class="key-point"><strong>Duration:</strong> 50 minutes</div>
{lesson_content}
</section>'''
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{topic_id}: {topic_name} - GCSE {subject_name} Lessons</title>
<meta name="description" content="{topic_id} {topic_name} - {lessons_per_topic} detailed 50-min GCSE {subject_name} lessons for homeschooling with teaching scripts, worked examples, parent guides.">
<meta name="keywords" content="GCSE {subject_name}, homeschool, lesson plan, {topic_name.lower()}, self-teaching, parent guide">
<meta property="og:title" content="{topic_name} - GCSE {subject_name} Lessons">
<meta property="og:description" content="{topic_id} {topic_name} - {lessons_per_topic} detailed lessons with teaching scripts">
<meta property="og:type" content="article">
<link rel="canonical" href="https://scottrix.github.io/gcselessons/topics/{strand}/{topic_id.lower().replace(' ', '-')}-{topic_name.lower().replace(' ', '-')}.html">
<meta property="og:site_name" content="GCSE Lessons">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{topic_id}: {topic_name}">
<link rel="stylesheet" href="../../style.css">
</head>
<body>
<header class="site-header"><div class="header-content"><a href="../../" class="logo">📖 GCSE Lessons</a><nav class="nav"><a href="../../#subjects">Subjects</a> <a href="../../{config['nav']}.html">{subject_name}</a></nav><button id="theme-toggle" class="theme-btn">🌙</button></div></header>
<main class="topic-content">
<div class="disclaimer-banner"><strong>Homeschool Guide:</strong> These lesson plans are a guide for parents. Content may contain errors — always cross-reference with official exam board specifications.</div>
<nav class="breadcrumb"><a href="../../">Home</a> <span>›</span> <a href="../../{config['nav']}.html">{subject_name}</a> <span>›</span> <span>{topic_name}</span></nav>
<article class="topic-header"><h1>{topic_id}: {topic_name}</h1><div class="topic-meta"><span class="badge foundation">Foundation</span><span class="badge higher">Higher</span><span class="badge">All Boards</span></div><p class="topic-desc">{lessons_per_topic} detailed 50-minute lessons with teaching scripts, worked examples, parent guides, and assessment criteria.</p></article>
<a class="fastmail-topbar" data-banner="fastmail" href="https://join.fastmail.com/0d63b2d52105" target="_blank" rel="noopener"><img src="../../images/assets/FM Billboard 970x250.png" alt="Fastmail" loading="lazy"></a><a class="fastmail-topbar" data-banner="dynadot" href="https://www.dynadot.com/?ref=scottrix" target="_blank" rel="nofollow noopener" hidden><img src="../../images/assets/dynadot-banner.jpg" alt="Dynadot" loading="lazy" onerror="this.parentElement.style.display='none';document.querySelector('[data-banner=fastmail]').hidden=false"></a><script>(function(){{var fm=document.querySelector('[data-banner=fastmail]');var dd=document.querySelector('[data-banner=dynadot]');if(Math.random()<0.5){{fm.hidden=true;dd.hidden=false}}}})();</script>

<section class="section"><h2>Lesson Overview</h2><div class="key-point"><strong>Total Lessons:</strong> {lessons_per_topic}<br><strong>Tier:</strong> {config['tier']}<br><strong>Duration:</strong> 50 minutes per lesson ({lessons_per_topic * 50} minutes total)<br><strong>Exam Boards:</strong> {config['boards']}</div></section>

<section class="section"><h2>Learning Objectives</h2><ul><li>Master core concepts of {topic_name.lower()}</li><li>Apply to exam questions confidently</li><li>Develop independent study skills</li><li>Build cross-topic connections</li></ul></section>

<section class="section"><h2>Prerequisites</h2><ul><li>Review [prerequisite from spec]</li><li>Key vocab: [terms to pre-teach]</li><li>Basic skills: [maths/literacy/practical]</li></ul></section>

<section class="section"><h2>Materials & Equipment</h2><ul><li>Exercise book, coloured pens</li><li>Scientific calculator</li><li>Ruler, protractor, compass (if needed)</li><li>Printed spec/textbook reference</li><li>Internet for videos (see Resources)</li></ul></section>

{all_lessons}

<section class="section"><h2>Homework & Consolidation</h2><ul><li><strong>Consolidation:</strong> Textbook end-of-topic questions (30 mins)</li><li><strong>Retrieval:</strong> 10 flashcards for key terms (15 mins)</li><li><strong>Exam practice:</strong> 2 past paper questions (20 mins)</li><li><strong>Extension:</strong> Research real-world application (optional, 30 mins)</li></ul></section>

<section class="section"><h2>Recommended Resources</h2><ul><li><a href="https://www.bbc.co.uk/bitesize" target="_blank" rel="noopener">BBC Bitesize - {subject_name}</a></li><li><a href="https://www.youtube.com" target="_blank" rel="noopener">YouTube: "{topic_name} GCSE"</a></li><li><a href="https://www.physicsandmathstutor.com" target="_blank" rel="noopener">Physics & Maths Tutor</a> (science/maths)</li></ul></section>

</main>
<footer class="site-footer"><p>GCSE Lessons - Free lesson plans for homeschooling</p><p>Content for educational purposes only. Always cross-reference with official specifications.</p><p>This site contains affiliate links. We may earn a commission if you purchase through these links.</p><p>© 2025 | <a href="privacy.html">Privacy Policy</a> | <a href="mailto:gcselessons@scott.scottrix.co.uk">Contact</a></p></footer>
<script>{THEME_SCRIPT}</script>
<script src="../../sidebar.js"></script><script src="../../affiliate-images.js"></script>
</body></html>'''

def regenerate_all():
    strand_to_subject = {}
    for sid in LESSON_COUNTS.keys():
        landing = os.path.join(BASE, f"{sid}.html")
        if os.path.exists(landing):
            with open(landing) as f:
                content = f.read()
            matches = re.findall(r'href="topics/([^/]+)/[^"]+\.html"', content)
            for strand in matches:
                strand_to_subject[strand] = sid
    
    count = 0
    for root, dirs, files in os.walk(os.path.join(BASE, "topics")):
        for f in files:
            if f.endswith('.html'):
                strand = os.path.basename(root)
                subject_id = strand_to_subject.get(strand)
                if not subject_id:
                    continue
                match = re.match(r'([A-Z]\d+)-(.+)\.html$', f)
                if not match:
                    match = re.match(r'([A-Z]{2}\d+)-(.+)\.html$', f)
                if not match:
                    continue
                topic_id, topic_name_kebab = match.groups()
                topic_name = topic_name_kebab.replace('-', ' ').title()
                filepath = os.path.join(root, f)
                
                new_html = generate_topic_page(subject_id, topic_id, topic_name, strand)
                with open(filepath, 'w') as f:
                    f.write(new_html)
                
                count += 1
                if count % 100 == 0:
                    print(f"Regenerated {count} topic pages...")
    
    print(f"Total regenerated: {count}")

if __name__ == '__main__':
    regenerate_all()
