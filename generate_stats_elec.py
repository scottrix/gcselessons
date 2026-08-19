#!/usr/bin/env python3
"""Generate Statistics and Electronics landing pages and topic lesson pages."""

import os

# ============================================================
# STATISTICS DATA
# ============================================================
STATS_STRANDS = [
    {
        "id": "stats-calculation",
        "name": "Statistical Calculation",
        "icon": "📊",
        "description": "Master the calculations behind statistical analysis: measures of central tendency, spread, correlation, and probability distributions.",
        "lessons": [
            {"id": "ST1", "title": "Measures of Central Tendency", "desc": "Mean, median, mode - when to use each, calculating from raw and grouped data, weighted means."},
            {"id": "ST2", "title": "Measures of Spread", "desc": "Range, IQR, variance, standard deviation - calculation and interpretation, outliers detection."},
            {"id": "ST3", "title": "Correlation and Regression", "desc": "Scatter graphs, Pearson's r, Spearman's rho, line of best fit, prediction and interpolation/extrapolation."},
            {"id": "ST4", "title": "Probability Distributions", "desc": "Binomial, normal, Poisson distributions - properties, calculations, normal approximation to binomial."},
        ]
    },
    {
        "id": "stats-collection",
        "name": "Data Collection",
        "icon": "📋",
        "description": "Design effective data collection strategies: sampling methods, survey design, experiments, and observational studies.",
        "lessons": [
            {"id": "ST1", "title": "Sampling Methods", "desc": "Random, systematic, stratified, cluster, quota, opportunity sampling - advantages, disadvantages, bias."},
            {"id": "ST2", "title": "Designing Surveys and Questionnaires", "desc": "Question types, avoiding leading questions, pilot surveys, response rates, ethical considerations."},
            {"id": "ST3", "title": "Experiments and Observational Studies", "desc": "Control groups, randomisation, blinding, confounding variables, matched pairs, natural experiments."},
        ]
    },
    {
        "id": "stats-exam-technique",
        "name": "Exam Technique",
        "icon": "✏️",
        "description": "Targeted exam preparation: command words, mark scheme analysis, time management, and common pitfalls.",
        "lessons": [
            {"id": "ST1", "title": "Command Words and Mark Schemes", "desc": "Interpret 'calculate', 'compare', 'justify', 'evaluate' - what examiners look for, securing method marks."},
            {"id": "ST2", "title": "Time Management and Strategy", "desc": "Question prioritisation, showing working, checking answers, handling multi-part questions, calculator use."},
        ]
    },
    {
        "id": "stats-interpretation",
        "name": "Data Interpretation",
        "icon": "📈",
        "description": "Read, analyse, and draw conclusions from statistical outputs: tables, graphs, summaries, and real-world contexts.",
        "lessons": [
            {"id": "ST1", "title": "Reading Tables and Summary Statistics", "desc": "Frequency tables, grouped data tables, summary stats output - extracting key information, spotting anomalies."},
            {"id": "ST2", "title": "Interpreting Graphs and Charts", "desc": "Histograms, box plots, cumulative frequency, time series, choropleth maps - reading shape, spread, trends."},
            {"id": "ST3", "title": "Statistical Reports and Conclusions", "desc": "Evaluating claims, margin of error, confidence intervals, statistical vs practical significance, media literacy."},
        ]
    },
    {
        "id": "stats-planning",
        "name": "Statistical Enquiry Cycle",
        "icon": "🔄",
        "description": "The complete statistical enquiry process: defining problems, planning investigations, executing, and evaluating.",
        "lessons": [
            {"id": "ST1", "title": "The Statistical Enquiry Cycle (PPDAC)", "desc": "Problem, Plan, Data, Analysis, Conclusion - full cycle walkthrough with a mini-investigation."},
            {"id": "ST2", "title": "Planning an Investigation", "desc": "Defining hypotheses, choosing variables, sampling strategy, data collection plan, ethics, risk assessment."},
        ]
    },
    {
        "id": "stats-presentation",
        "name": "Data Presentation",
        "icon": "📊",
        "description": "Communicate data effectively: choosing appropriate charts, constructing accurate diagrams, and avoiding misleading displays.",
        "lessons": [
            {"id": "ST1", "title": "Choosing the Right Chart", "desc": "Bar charts, pie charts, histograms, line graphs, scatter plots - matching chart to data type and purpose."},
            {"id": "ST2", "title": "Constructing Accurate Diagrams", "desc": "Scaling, labelling, frequency density for histograms, cumulative frequency curves, stem-and-leaf diagrams."},
            {"id": "ST3", "title": "Misleading Graphs and Ethics", "desc": "Truncated axes, distorted scales, cherry-picking data, 3D effects - identifying and avoiding deception."},
            {"id": "ST4", "title": "Technology for Presentation", "desc": "Spreadsheets, statistical software, dynamic graphs, exporting for reports - tools and best practices."},
        ]
    },
]

# ============================================================
# ELECTRONICS DATA
# ============================================================
ELEC_STRANDS = [
    {
        "id": "elec-fundamentals",
        "name": "Fundamentals",
        "icon": "⚡",
        "description": "Core electrical concepts: current, voltage, resistance, power, energy, and the laws that govern them.",
        "lessons": [
            {"id": "EL1", "title": "Current, Voltage and Resistance", "desc": "Charge flow, potential difference, Ohm's law, series and parallel circuits, measuring with multimeters."},
            {"id": "EL2", "title": "Power and Energy", "desc": "Electrical power (P=VI, P=I²R, P=V²/R), energy transfer (E=Pt), kilowatt-hours, efficiency calculations."},
            {"id": "EL3", "title": "Component Characteristics", "desc": "IV characteristics of resistors, filament lamps, diodes, LEDs, LDRs, thermistors - ohmic vs non-ohmic."},
            {"id": "EL4", "title": "Circuit Laws and Analysis", "desc": "Kirchhoff's current and voltage laws, potential dividers, Wheatstone bridge, solving complex networks."},
        ]
    },
    {
        "id": "elec-analogue-systems",
        "name": "Analogue Systems",
        "icon": "📻",
        "description": "Continuous signal processing: amplifiers, filters, oscillators, sensors, and signal conditioning circuits.",
        "lessons": [
            {"id": "EL1", "title": "Operational Amplifiers", "desc": "Ideal op-amp properties, inverting/non-inverting amplifiers, voltage follower, gain calculations, bandwidth."},
            {"id": "EL2", "title": "Filters and Frequency Response", "desc": "Passive RC filters (low-pass, high-pass, band-pass), active filters, Bode plots, cutoff frequency, roll-off."},
            {"id": "EL3", "title": "Sensors and Signal Conditioning", "desc": "Thermistors, LDRs, strain gauges, Wheatstone bridge, instrumentation amplifiers, linearisation techniques."},
        ]
    },
    {
        "id": "elec-digital-systems",
        "name": "Digital Systems",
        "icon": "💻",
        "description": "Discrete signal processing: logic gates, combinational and sequential logic, microcontrollers, and digital communication.",
        "lessons": [
            {"id": "EL1", "title": "Logic Gates and Boolean Algebra", "desc": "NOT, AND, OR, NAND, NOR, XOR, XNOR - truth tables, Boolean expressions, De Morgan's laws, simplification."},
            {"id": "EL2", "title": "Combinational Logic Design", "desc": "Half/full adders, decoders, multiplexers, encoders, 7-segment displays, Karnaugh maps for minimisation."},
            {"id": "EL3", "title": "Sequential Logic", "desc": "Latches, flip-flops (SR, D, JK, T), counters, shift registers, state diagrams, synchronous vs asynchronous."},
            {"id": "EL4", "title": "Microcontrollers and Interfacing", "desc": "PIC/Arduino basics, GPIO, ADC, PWM, interrupts, I2C/SPI/UART, programming simple control systems."},
        ]
    },
    {
        "id": "elec-applications",
        "name": "Electronic Applications",
        "icon": "🔧",
        "description": "Real-world electronic systems: power supplies, audio, communications, control systems, and emerging technologies.",
        "lessons": [
            {"id": "EL1", "title": "Power Supply Circuits", "desc": "Rectification (half/full wave), smoothing, regulation (linear, switching), voltage references, protection circuits."},
            {"id": "EL2", "title": "Audio and Signal Processing", "desc": "Pre-amplifiers, power amplifiers, crossover networks, noise reduction, Class A/B/D amplifiers, distortion."},
            {"id": "EL3", "title": "Communication Systems", "desc": "Modulation (AM, FM), demodulation, antennas, wireless protocols (Bluetooth, WiFi, LoRa), signal-to-noise ratio."},
        ]
    },
    {
        "id": "elec-exam-technique",
        "name": "Exam Technique",
        "icon": "✏️",
        "description": "Electronics-specific exam skills: circuit analysis, calculation layout, diagram annotation, and practical write-ups.",
        "lessons": [
            {"id": "EL1", "title": "Circuit Analysis Questions", "desc": "Step-by-step circuit solving, showing working, unit consistency, significant figures, checking plausibility."},
            {"id": "EL2", "title": "Practical Write-ups and Diagrams", "desc": "Schematic drawing standards, results tables, graph plotting, uncertainty analysis, evaluation structure."},
        ]
    },
    {
        "id": "elec-practical-circuits",
        "name": "Practical Circuits",
        "icon": "🛠️",
        "description": "Hands-on circuit building: prototyping, testing, fault-finding, and required practicals for Eduqas Electronics.",
        "lessons": [
            {"id": "EL1", "title": "Breadboarding and Prototyping", "desc": "Breadboard layout, component placement, wiring techniques, power rails, testing with multimeter/oscilloscope."},
            {"id": "EL2", "title": "Required Practical: Potential Divider", "desc": "Build and test a potential divider circuit. Measure Vout vs Vin. Plot characteristic. Calculate resistor values.", "practical": True},
            {"id": "EL3", "title": "Required Practical: Transistor Switch", "desc": "Build a transistor switching circuit. Measure base/collector currents. Calculate current gain. Test with sensor input.", "practical": True},
        ]
    },
]

# ============================================================
# TEMPLATE FUNCTIONS
# ============================================================

def stats_landing_page():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GCSE Statistics - Lesson Plans</title>
<meta name="description" content="Free GCSE Statistics lesson plans for homeschooling across 6 strands: Statistical Calculation, Data Collection, Exam Technique, Data Interpretation, Statistical Enquiry Cycle, Data Presentation.">
<meta name="keywords" content="GCSE Statistics, homeschool, lesson plan, statistics, data analysis, probability, sampling, hypothesis testing">
<meta property="og:title" content="GCSE Statistics - Lesson Plans">
<meta property="og:description" content="Free GCSE Statistics lesson plans for homeschooling across 6 strands.">
<meta property="og:type" content="article">
<meta property="og:url" content="https://scottrix.github.io/gcselessons/statistics.html">
<link rel="canonical" href="https://scottrix.github.io/gcselessons/statistics.html">
<meta property="og:site_name" content="GCSE Lessons">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="GCSE Statistics - Lesson Plans">
<meta name="twitter:description" content="Free GCSE Statistics lesson plans for homeschooling across 6 strands.">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="site-header">
<div class="header-content">
<a href="./" class="logo">📖 GCSE Lessons</a>
<nav class="nav">
<a href="./#subjects">Subjects</a>
<a href="./">Home</a>
</nav>
<button id="theme-toggle" class="theme-btn">🌙</button>
</div>
</header>

<main class="topic-content">
<div class="disclaimer-banner"><strong>Homeschool Guide:</strong> These lesson plans are a guide for parents. Content may contain errors — always cross-reference with official exam board specifications.</div>

<nav class="breadcrumb">
<a href="./">Home</a> <span>›</span>
<span>Statistics</span>
</nav>

<article class="topic-header">
<h1>📊 GCSE Statistics</h1>
<div class="topic-meta">
<span class="badge foundation">Foundation</span>
<span class="badge higher">Higher</span>
<span class="badge">AQA, Edexcel, CCEA</span>
</div>
<p class="topic-desc">Complete lesson plans for GCSE Statistics covering all topics across 6 strands. Designed for homeschooling parents, with detailed teaching notes, activities, and assessment criteria for each lesson.</p>
</article>

<section class="section">
<h2>📊 Course Overview</h2>
<p>GCSE Statistics develops skills in data collection, processing, representation, and interpretation. It complements GCSE Mathematics and supports subjects like Geography, Psychology, and Science. Foundation tier covers grades 1-5; Higher tier covers grades 4-9. Assessment is typically two written papers.</p>
<table class="comparison-table">
<tr><th>Strand</th><th>Topics</th></tr>
      <tr><td><a href="#stats-calculation">Statistical Calculation</a></td><td>4</td></tr>
      <tr><td><a href="#stats-collection">Data Collection</a></td><td>3</td></tr>
      <tr><td><a href="#stats-exam-technique">Exam Technique</a></td><td>2</td></tr>
      <tr><td><a href="#stats-interpretation">Data Interpretation</a></td><td>3</td></tr>
      <tr><td><a href="#stats-planning">Statistical Enquiry Cycle</a></td><td>2</td></tr>
      <tr><td><a href="#stats-presentation">Data Presentation</a></td><td>4</td></tr>
</table>
</section>

{generate_stats_strands_sections()}

</main>

<footer class="site-footer">
<p>GCSE Lessons - Free lesson plans for homeschooling</p>
<p>Content for educational purposes only. Always cross-reference with official specifications.</p>
<p>© 2025 | <a href="privacy.html">Privacy Policy</a> | <a href="mailto:gcselessons@scott.scottrix.co.uk">Contact</a></p>
</footer>

<script>
document.getElementById("theme-toggle").addEventListener("click", function() {{
const root = document.documentElement;
if (root.classList.contains("light-mode")) {{
root.classList.remove("light-mode");
this.textContent = "🌙";
localStorage.setItem("gcselessons-theme", "dark");
}} else {{
root.classList.add("light-mode");
this.textContent = "☀️";
localStorage.setItem("gcselessons-theme", "light");
}}
}});
if (localStorage.getItem("gcselessons-theme") === "light") {{
document.documentElement.classList.add("light-mode");
document.getElementById("theme-toggle").textContent = "☀️";
}}
</script>
<script src="sidebar.js"></script>
</body>
</html>
'''

def generate_stats_strands_sections():
    sections = []
    for strand in STATS_STRANDS:
        lessons_html = ""
        for lesson in strand["lessons"]:
            lessons_html += f'''      <a href="topics/{strand["id"]}/{lesson["id"]}-{lesson["title"].lower().replace(" ", "-")}.html" class="topic-card">
        <span class="topic-id">{lesson["id"]}</span>
        <span class="topic-name">{lesson["title"]}</span>
      </a>
'''
        sections.append(f'''  <section id="{strand["id"]}" class="section">
    <h2>{strand["icon"]} {strand["name"]} ({len(strand["lessons"])} Topics)</h2>
    <div class="topics-grid">
{lessons_html}    </div>
  </section>''')
    return "\n\n".join(sections)

def elec_landing_page():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GCSE Electronics - Lesson Plans</title>
<meta name="description" content="Free GCSE Electronics lesson plans for homeschooling across 6 strands: Fundamentals, Analogue Systems, Digital Systems, Applications, Exam Technique, Practical Circuits. Includes required practicals.">
<meta name="keywords" content="GCSE Electronics, homeschool, lesson plan, circuits, components, schematics, practical, microcontrollers, logic gates">
<meta property="og:title" content="GCSE Electronics - Lesson Plans">
<meta property="og:description" content="Free GCSE Electronics lesson plans for homeschooling across 6 strands with required practicals.">
<meta property="og:type" content="article">
<meta property="og:url" content="https://scottrix.github.io/gcselessons/electronics.html">
<link rel="canonical" href="https://scottrix.github.io/gcselessons/electronics.html">
<meta property="og:site_name" content="GCSE Lessons">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="GCSE Electronics - Lesson Plans">
<meta name="twitter:description" content="Free GCSE Electronics lesson plans for homeschooling across 6 strands with required practicals.">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="site-header">
<div class="header-content">
<a href="./" class="logo">📖 GCSE Lessons</a>
<nav class="nav">
<a href="./#subjects">Subjects</a>
<a href="./">Home</a>
</nav>
<button id="theme-toggle" class="theme-btn">🌙</button>
</div>
</header>

<main class="topic-content">
<div class="disclaimer-banner"><strong>Homeschool Guide:</strong> These lesson plans are a guide for parents. Content may contain errors — always cross-reference with official exam board specifications.</div>

<nav class="breadcrumb">
<a href="./">Home</a> <span>›</span>
<span>Electronics</span>
</nav>

<article class="topic-header">
<h1>⚡ GCSE Electronics</h1>
<div class="topic-meta">
<span class="badge foundation">Foundation</span>
<span class="badge higher">Higher</span>
<span class="badge">Eduqas</span>
<span class="badge" style="background:#1565c0;color:white;">Practical Subject</span>
</div>
<p class="topic-desc">Complete lesson plans for GCSE Electronics (Eduqas) covering all topics across 6 strands. Includes required practicals for circuit building, schematics, components, and hands-on skills. Designed for homeschooling parents with detailed teaching notes, activities, and assessment criteria.</p>
</article>

<section class="section">
<h2>📊 Course Overview</h2>
<p>GCSE Electronics (Eduqas) develops understanding of electronic systems through theory and practical work. Students learn to design, build, and test circuits. The course includes required practicals that are assessed in written exams. Foundation tier covers grades 1-5; Higher tier covers grades 4-9. Assessment: two written papers (80%) and practical skills assessed within papers (20%).</p>
<table class="comparison-table">
<tr><th>Strand</th><th>Topics</th></tr>
      <tr><td><a href="#elec-fundamentals">Fundamentals</a></td><td>4</td></tr>
      <tr><td><a href="#elec-analogue-systems">Analogue Systems</a></td><td>3</td></tr>
      <tr><td><a href="#elec-digital-systems">Digital Systems</a></td><td>4</td></tr>
      <tr><td><a href="#elec-applications">Electronic Applications</a></td><td>3</td></tr>
      <tr><td><a href="#elec-exam-technique">Exam Technique</a></td><td>2</td></tr>
      <tr><td><a href="#elec-practical-circuits">Practical Circuits</a></td><td>3</td></tr>
</table>
</section>

{generate_elec_strands_sections()}

</main>

<footer class="site-footer">
<p>GCSE Lessons - Free lesson plans for homeschooling</p>
<p>Content for educational purposes only. Always cross-reference with official specifications.</p>
<p>© 2025 | <a href="privacy.html">Privacy Policy</a> | <a href="mailto:gcselessons@scott.scottrix.co.uk">Contact</a></p>
</footer>

<script>
document.getElementById("theme-toggle").addEventListener("click", function() {{
const root = document.documentElement;
if (root.classList.contains("light-mode")) {{
root.classList.remove("light-mode");
this.textContent = "🌙";
localStorage.setItem("gcselessons-theme", "dark");
}} else {{
root.classList.add("light-mode");
this.textContent = "☀️";
localStorage.setItem("gcselessons-theme", "light");
}}
}});
if (localStorage.getItem("gcselessons-theme") === "light") {{
document.documentElement.classList.add("light-mode");
document.getElementById("theme-toggle").textContent = "☀️";
}}
</script>
<script src="sidebar.js"></script>
</body>
</html>
'''

def generate_elec_strands_sections():
    sections = []
    for strand in ELEC_STRANDS:
        lessons_html = ""
        for lesson in strand["lessons"]:
            badge = '        <span class="badge" style="background:#1565c0;color:white;">Required Practical</span>\n' if lesson.get("practical") else ""
            lessons_html += f'''      <a href="topics/{strand["id"]}/{lesson["id"]}-{lesson["title"].lower().replace(" ", "-")}.html" class="topic-card">
        <span class="topic-id">{lesson["id"]}</span>
        <span class="topic-name">{lesson["title"]}</span>
{badge}      </a>
'''
        sections.append(f'''  <section id="{strand["id"]}" class="section">
    <h2>{strand["icon"]} {strand["name"]} ({len(strand["lessons"])} Topics)</h2>
    <div class="topics-grid">
{lessons_html}    </div>
  </section>''')
    return "\n\n".join(sections)

def stats_lesson_page(strand, lesson, lesson_num, total_lessons):
    prev_link = ""
    next_link = ""
    if lesson_num > 0:
        prev_lesson = strand["lessons"][lesson_num - 1]
        prev_link = f'<a href="{prev_lesson["id"]}-{prev_lesson["title"].lower().replace(" ", "-")}.html" class="nav-btn prev">← {prev_lesson["id"]}: {prev_lesson["title"]}</a>'
    if lesson_num < total_lessons - 1:
        next_lesson = strand["lessons"][lesson_num + 1]
        next_link = f'<a href="{next_lesson["id"]}-{next_lesson["title"].lower().replace(" ", "-")}.html" class="nav-btn next">{next_lesson["id"]}: {next_lesson["title"]} →</a>'
    
    nav_html = f'<div class="lesson-nav">{prev_link}{next_link}</div>' if (prev_link or next_link) else ""
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{lesson["id"]}: {lesson["title"]} - GCSE Statistics Lessons</title>
<meta name="description" content="{lesson["id"]} {lesson["title"]} - Detailed GCSE Statistics lesson plan for homeschooling">
<meta name="keywords" content="GCSE Statistics, homeschool, lesson plan, {lesson["title"].lower()}, statistics">
<meta property="og:title" content="{lesson["id"]}: {lesson["title"]} - GCSE Statistics Lessons">
<meta property="og:description" content="{lesson["id"]} {lesson["title"]} - Detailed GCSE Statistics lesson plan">
<meta property="og:type" content="article">
<link rel="canonical" href="https://scottrix.github.io/gcselessons/topics/{strand["id"]}/{lesson["id"]}-{lesson["title"].lower().replace(" ", "-")}.html">
<meta property="og:site_name" content="GCSE Lessons">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{lesson["id"]}: {lesson["title"]}">
<link rel="stylesheet" href="../../style.css">
</head>
<body>
<header class="site-header">
<div class="header-content">
<a href="../../" class="logo">📖 GCSE Lessons</a>
<nav class="nav"><a href="../../#subjects">Subjects</a> <a href="../../statistics.html">Statistics</a></nav>
<button id="theme-toggle" class="theme-btn">🌙</button>
</div>
</header>
<main class="topic-content">
<div class="disclaimer-banner"><strong>Homeschool Guide:</strong> These lesson plans are a guide for parents. Content may contain errors — always cross-reference with official exam board specifications.</div>

<nav class="breadcrumb"><a href="../../">Home</a> <span>›</span> <a href="../../statistics.html">Statistics</a> <span>›</span> <span>{strand["name"]}</span> <span>›</span> <span>{lesson["title"]}</span></nav>

<article class="topic-header">
<h1>{lesson["id"]}: {lesson["title"]}</h1>
<div class="topic-meta">
<span class="badge foundation">Foundation</span>
<span class="badge higher">Higher</span>
<span class="badge">AQA, Edexcel, CCEA</span>
</div>
<p class="topic-desc">{lesson["desc"]}</p>
</article>

{nav_html}

<section class="section">
<h2>Lesson Overview</h2>
<div class="key-point">
<strong>Estimated Lessons:</strong> 2-3<br>
<strong>Tier:</strong> Foundation and Higher<br>
<strong>Duration:</strong> 50 minutes per lesson<br>
<strong>Exam Boards:</strong> AQA, Edexcel, CCEA
</div>
</section>

<section class="section">
<h2>Learning Objectives</h2>
<ul>
<li>Understand the key concepts and terminology for {lesson["title"].lower()}</li>
<li>Apply {lesson["title"].lower()} techniques to solve statistical problems</li>
<li>Interpret results in context and communicate findings clearly</li>
<li>Identify common misconceptions and avoid typical errors</li>
</ul>
</section>

<section class="section">
<h2>Prerequisites</h2>
<ul>
<li>Basic arithmetic and algebraic manipulation</li>
<li>Understanding of data types (discrete, continuous, categorical)</li>
<li>Familiarity with statistical notation and terminology</li>
</ul>
</section>

<section class="section">
<h2>Materials & Equipment</h2>
<ul>
<li>Scientific calculator (statistics mode)</li>
<li>Graph paper / squared paper</li>
<li>Statistical tables (normal, t, chi-squared) or calculator functions</li>
<li>Spreadsheet software (Excel, Google Sheets) for demonstrations</li>
<li>Real-world datasets for practice (provided in resources)</li>
</ul>
</section>

<section class="section">
<h2>Lesson 1: Core Concepts</h2>
<div class="key-point"><strong>Duration:</strong> 50 minutes</div>

<h3>Starter Activity (5 minutes)</h3>
<div class="example">
<div class="example-title">Quick Recall</div>
<p>Rapid-fire questions on prerequisite knowledge relevant to {lesson["title"].lower()}. Use mini-whiteboards for immediate feedback.</p>
</div>

<h3>Main Content (35 minutes)</h3>
<div class="key-point">
<strong>Teaching Notes:</strong><br>
Introduce key concepts systematically. Use worked examples with real data. Emphasise:
• Definitions and notation<br>
• Step-by-step procedures<br>
• When to use each method<br>
• Interpreting calculator/computer output
</div>

<div class="example">
<div class="example-title">Worked Example</div>
<p>Detailed step-by-step solution demonstrating the key technique for {lesson["title"].lower()}. Include calculator keystrokes where applicable.</p>
</div>

<div class="formula-box">
Key formulae for {lesson["title"].lower()} — students should memorise or know how to derive.
</div>

<div class="misconception">
<h3>Common Misconception</h3>
<p><span class="wrong">A typical student error related to this topic.</span></p>
<p><span class="right">Correct understanding with explanation of why the misconception arises.</span></p>
</div>

<h3>Differentiation</h3>
<div class="key-point"><strong>Support:</strong><br>Provide structured worksheets with partially completed examples. Use visual aids and concrete examples. Allow calculator use for arithmetic.</div>
<div class="key-point"><strong>Stretch:</strong><br>Explore extensions: proof of formulae, comparison of methods, application to unfamiliar contexts, derivation of related results.</div>

<h3>Plenary (5 minutes)</h3>
<div class="example"><div class="example-title">Exit Question</div>
<p>A single focused question checking the core learning objective. Students write answer on exit slip.</p></div>

<h3>Assessment Criteria</h3>
<ul>
<li><strong>Got it:</strong> Accurately applies the method, interprets results correctly, communicates clearly.</li>
<li><strong>Getting there:</strong> Method mostly correct but minor errors in calculation or interpretation.</li>
<li><strong>Not yet:</strong> Fundamental misunderstanding of the concept. Reteach with alternative approach.</li>
</ul>
</section>

<section class="section">
<h2>Lesson 2: Application and Practice</h2>
<div class="key-point"><strong>Duration:</strong> 50 minutes</div>

<h3>Starter Activity (5 minutes)</h3>
<div class="example">
<div class="example-title">Error Analysis</div>
<p>Present a solution with deliberate errors. Students identify and correct them.</p>
</div>

<h3>Main Content (35 minutes)</h3>
<div class="key-point">
<strong>Teaching Notes:</strong><br>
Guided practice → independent practice → exam-style questions.<br>
Focus on: context interpretation, selecting appropriate methods, handling grouped data, technology use.
</div>

<div class="example">
<div class="example-title">Contextual Problem</div>
<p>Real-world scenario requiring {lesson["title"].lower()}. Students work through: identify variables, choose method, calculate, interpret, conclude.</p>
</div>

<div class="ao3-section">
<h3>AO3 Problem Solving</h3>
<p>Multi-step question requiring decision-making: which technique to use, handling imperfect data, justifying choices, evaluating limitations.</p>
</div>

<h3>Differentiation</h3>
<div class="key-point"><strong>Support:</strong><br>Scaffolded version with prompts: "What type of data is this?", "Which measure of spread is appropriate?", "What does the result tell you?"</div>
<div class="key-point"><strong>Stretch:</strong><br>Open-ended investigation: "Design a study to compare... using {lesson["title"].lower()}. Justify your choices."</div>

<h3>Plenary (5 minutes)</h3>
<div class="example"><div class="example-title">Summary Triangle</div>
<p>Students write: 3 key points, 2 connections to other topics, 1 question they still have.</p></div>

<h3>Assessment Criteria</h3>
<ul>
<li><strong>Got it:</strong> Selects and applies correct method independently, interprets in context, evaluates limitations.</li>
<li><strong>Getting there:</strong> Applies method with guidance, interprets partially.</li>
<li><strong>Not yet:</strong> Cannot select appropriate method. Reteach decision-making framework.</li>
</ul>
</section>

<section class="section">
<h2>Homework Suggestions</h2>
<ul>
<li>Complete practice questions from textbook/exam papers on {lesson["title"].lower()}</li>
<li>Find a real dataset (e.g., from ONS, data.gov.uk) and apply the technique</li>
<li>Create a one-page revision summary with key formulae, when to use, and a worked example</li>
<li>Use spreadsheet to generate data and verify calculations</li>
</ul>
</section>

<section class="section">
<h2>Resources</h2>
<ul>
<li><a href="https://www.aqa.org.uk/subjects/mathematics/gcse/statistics-8382" target="_blank" rel="noopener">AQA GCSE Statistics Specification</a></li>
<li><a href="https://qualifications.pearson.com/en/qualifications/edexcel-gcses/statistics-2017.html" target="_blank" rel="noopener">Edexcel GCSE Statistics Specification</a></li>
<li><a href="https://www.bbc.co.uk/bitesize/subjects/z38pycw" target="_blank" rel="noopener">BBC Bitesize - GCSE Statistics</a></li>
<li><a href="https://www.stem.org.uk/resources/collection/4037/gcse-statistics" target="_blank" rel="noopener">STEM Learning - Statistics Resources</a></li>
</ul>
</section>

</main>
<footer class="site-footer">
<p>GCSE Lessons - Free lesson plans for homeschooling</p>
<p>Content for educational purposes only. Always cross-reference with official specifications.</p>
<p>© 2025 | <a href="../../privacy.html">Privacy Policy</a> | <a href="mailto:gcselessons@scott.scottrix.co.uk">Contact</a></p>
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
</html>
'''

def elec_lesson_page(strand, lesson, lesson_num, total_lessons):
    prev_link = ""
    next_link = ""
    if lesson_num > 0:
        prev_lesson = strand["lessons"][lesson_num - 1]
        prev_link = f'<a href="{prev_lesson["id"]}-{prev_lesson["title"].lower().replace(" ", "-")}.html" class="nav-btn prev">← {prev_lesson["id"]}: {prev_lesson["title"]}</a>'
    if lesson_num < total_lessons - 1:
        next_lesson = strand["lessons"][lesson_num + 1]
        next_link = f'<a href="{next_lesson["id"]}-{next_lesson["title"].lower().replace(" ", "-")}.html" class="nav-btn next">{next_lesson["id"]}: {next_lesson["title"]} →</a>'
    
    nav_html = f'<div class="lesson-nav">{prev_link}{next_link}</div>' if (prev_link or next_link) else ""
    
    practical_badge = '<span class="badge" style="background:#1565c0;color:white;">Required Practical</span>' if lesson.get("practical") else ""
    practical_section = ""
    if lesson.get("practical"):
        practical_section = f'''
<section class="section required-practical">
<h3>🔬 Required Practical: {lesson["title"]}</h3>
<p>This is a required practical for Eduqas GCSE Electronics. It may be assessed in written examinations.</p>
<h4>Apparatus and Materials</h4>
<ul>
<li>Breadboard and jumper wires</li>
<li>Components per circuit diagram (resistors, transistors, sensors, power supply)</li>
<li>Multimeter (voltage, current, resistance ranges)</li>
<li>Oscilloscope or data logger (where applicable)</li>
<li>Component datasheets</li>
</ul>
<h4>Procedure</h4>
<ol>
<li>Study the schematic and identify all components and connections</li>
<li>Build the circuit on breadboard following the layout diagram</li>
<li>Verify connections with multimeter continuity test before powering</li>
<li>Apply power and measure key voltages/currents at test points</li>
<li>Record results in a structured table with units and uncertainties</li>
<li>Vary input parameters (e.g., sensor conditions, input voltage) and observe outputs</li>
<li>Plot characteristic graphs (e.g., Vout vs Vin, Ic vs Ib)</li>
<li>Compare experimental results with theoretical predictions</li>
</ol>
<h4>Key Measurements and Calculations</h4>
<ul>
<li>Measure: voltages at all nodes, currents in all branches</li>
<li>Calculate: voltage gain, current gain, power dissipation, efficiency</li>
<li>Analyse: linearity, threshold voltages, switching times, frequency response</li>
</ul>
<h4>Safety and Risk Assessment</h4>
<ul>
<li>Check component power ratings — do not exceed maximum voltage/current</li>
<li>Use current-limiting resistors with LEDs and transistors</li>
<li>Discharge capacitors before handling</li>
<li>Eye protection when clipping leads or testing high-energy circuits</li>
<li>Never work on mains-powered circuits without qualified supervision</li>
</ul>
<h4>Typical Exam Questions</h4>
<ul>
<li>Draw the circuit diagram from memory / description</li>
<li>Explain the function of each component in the circuit</li>
<li>Calculate expected readings for given component values</li>
<li>Analyse a results table: identify anomalies, calculate uncertainties</li>
<li>Suggest improvements to the experimental method</li>
<li>Explain how the circuit would behave if a component failed open/short</li>
</ul>
</section>
'''
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{lesson["id"]}: {lesson["title"]} - GCSE Electronics Lessons</title>
<meta name="description" content="{lesson["id"]} {lesson["title"]} - Detailed GCSE Electronics lesson plan for homeschooling">
<meta name="keywords" content="GCSE Electronics, homeschool, lesson plan, {lesson["title"].lower()}, circuits, components, practical">
<meta property="og:title" content="{lesson["id"]}: {lesson["title"]} - GCSE Electronics Lessons">
<meta property="og:description" content="{lesson["id"]} {lesson["title"]} - Detailed GCSE Electronics lesson plan">
<meta property="og:type" content="article">
<link rel="canonical" href="https://scottrix.github.io/gcselessons/topics/{strand["id"]}/{lesson["id"]}-{lesson["title"].lower().replace(" ", "-")}.html">
<meta property="og:site_name" content="GCSE Lessons">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{lesson["id"]}: {lesson["title"]}">
<link rel="stylesheet" href="../../style.css">
</head>
<body>
<header class="site-header">
<div class="header-content">
<a href="../../" class="logo">📖 GCSE Lessons</a>
<nav class="nav"><a href="../../#subjects">Subjects</a> <a href="../../electronics.html">Electronics</a></nav>
<button id="theme-toggle" class="theme-btn">🌙</button>
</div>
</header>
<main class="topic-content">
<div class="disclaimer-banner"><strong>Homeschool Guide:</strong> These lesson plans are a guide for parents. Content may contain errors — always cross-reference with official exam board specifications.</div>

<nav class="breadcrumb"><a href="../../">Home</a> <span>›</span> <a href="../../electronics.html">Electronics</a> <span>›</span> <span>{strand["name"]}</span> <span>›</span> <span>{lesson["title"]}</span></nav>

<article class="topic-header">
<h1>{lesson["id"]}: {lesson["title"]} {practical_badge}</h1>
<div class="topic-meta">
<span class="badge foundation">Foundation</span>
<span class="badge higher">Higher</span>
<span class="badge">Eduqas</span>
</div>
<p class="topic-desc">{lesson["desc"]}</p>
</article>

{nav_html}

<section class="section">
<h2>Lesson Overview</h2>
<div class="key-point">
<strong>Estimated Lessons:</strong> 2-3<br>
<strong>Tier:</strong> Foundation and Higher<br>
<strong>Duration:</strong> 50 minutes per lesson (+ practical time where applicable)<br>
<strong>Exam Board:</strong> Eduqas
</div>
</section>

<section class="section">
<h2>Learning Objectives</h2>
<ul>
<li>Understand the principles and theory behind {lesson["title"].lower()}</li>
<li>Analyse and design circuits involving {lesson["title"].lower()}</li>
<li>Build, test, and troubleshoot practical circuits</li>
<li>Apply relevant formulae and interpret results</li>
<li>Communicate technical information using standard symbols and notation
</ul>
</section>

<section class="section">
<h2>Prerequisites</h2>
<ul>
<li>Basic electrical quantities: charge, current, voltage, resistance, power</li>
<li>Ohm's law and Kirchhoff's laws</li>
<li>Component symbols and schematic reading</li>
<li>Use of multimeter and breadboard</li>
<li>For digital topics: binary, logic gates, truth tables
</ul>
</section>

<section class="section">
<h2>Materials & Equipment</h2>
<ul>
<li>Breadboards, jumper wires, wire strippers, cutters</li>
<li>Component kits: resistors (E12/E24 series), capacitors, diodes, transistors (BJT, MOSFET)</li>
<li>ICs: 555 timer, 741 op-amp, 7400/74LS00 series logic gates, microcontroller (Arduino/PIC)</li>
<li>Sensors: LDR, thermistor, LM35, microphone, IR receiver</li>
<li>Test equipment: multimeter, oscilloscope, function generator, logic probe</li>
<li>Power supplies: benchtop PSU, battery packs (5V, 9V, 12V)</li>
<li>PCB design software (KiCad, Eagle) and/or stripboard for permanent circuits
</ul>
</section>

<section class="section">
<h2>Lesson 1: Theory and Circuit Analysis</h2>
<div class="key-point"><strong>Duration:</strong> 50 minutes</div>

<h3>Starter Activity (5 minutes)</h3>
<div class="example">
<div class="example-title">Circuit Recognition</div>
<p>Show schematic fragments. Students identify: circuit type, key components, expected behaviour.</p>
</div>

<h3>Main Content (35 minutes)</h3>
<div class="key-point">
<strong>Teaching Notes:</strong><br>
Cover the theoretical foundation for {lesson["title"].lower()}:
• Underlying physics principles<br>
• Component models and characteristics<br>
• Key equations and design formulae<br>
• Standard circuit configurations<br>
• Performance metrics and limitations
</div>

<div class="example">
<div class="example-title">Worked Example: Circuit Analysis</div>
<p>Step-by-step analysis of a representative {lesson["title"].lower()} circuit. Calculate all node voltages, branch currents, power dissipation. Show multimeter/oscilloscope measurement points.</p>
</div>

<div class="formula-box">
Key design equations for {lesson["title"].lower()} — students must be able to select, rearrange, and apply.
</div>

<div class="misconception">
<h3>Common Misconception</h3>
<p><span class="wrong">A typical student error in circuit analysis or component behaviour.</span></p>
<p><span class="right">Correct understanding with reference to component physics and circuit laws.</span></p>
</div>

<h3>Differentiation</h3>
<div class="key-point"><strong>Support:</strong><br>Provide circuit templates with component values. Use circuit simulator (Falstad, EveryCircuit) for visualisation. Colour-code schematic by function.</div>
<div class="key-point"><strong>Stretch:</strong><br>Design a circuit to meet a specification. Compare topologies. Analyse tolerance effects. Simulate in SPICE.</div>

<h3>Plenary (5 minutes)</h3>
<div class="example"><div class="example-title">Circuit Function</div>
<p>Given a schematic, students write 3 sentences: what it does, how it works, one limitation.</p></div>

<h3>Assessment Criteria</h3>
<ul>
<li><strong>Got it:</strong> Explains operation, calculates correctly, predicts behaviour under changes.</li>
<li><strong>Getting there:</strong> Follows analysis steps but makes arithmetic or conceptual errors.</li>
<li><strong>Not yet:</strong> Cannot identify circuit type or apply basic laws. Reteach with simpler circuit.</li>
</ul>
</section>

<section class="section">
<h2>Lesson 2: Practical Implementation and Testing</h2>
<div class="key-point"><strong>Duration:</strong> 50-100 minutes (includes build time)</div>

<h3>Starter Activity (5 minutes)</h3>
<div class="example">
<div class="example-title">Component Check</div>
<p>Students identify components from a kit using colour codes, markings, and datasheets. Verify values with multimeter.</p>
</div>

<h3>Main Content (40-85 minutes)</h3>
<div class="key-point">
<strong>Teaching Notes:</strong><br>
Guided build → test → analyse cycle:<br>
1. <strong>Layout planning:</strong> Breadboard mapping, power rail assignment, signal flow<br>
2. <strong>Assembly:</strong> Component placement, lead forming, secure connections<br>
3. <strong>Pre-power check:</strong> Visual inspection, continuity, short-circuit test<br>
4. <strong>Power-up and measurement:</strong> Systematic testing at each test point<br>
5. <strong>Characterisation:</strong> Vary inputs, record outputs, plot graphs<br>
6. <strong>Fault finding:</strong> If not working — systematic debug (power, connections, component values, orientation)
</div>

<div class="example">
<div class="example-title">Build Guide: {lesson["title"]}</div>
<p>Schematic with breadboard layout overlay. Test point labels. Expected readings table. Troubleshooting checklist.</p>
</div>

<div class="maths-skill">
<h3>Maths Skills</h3>
<p>Relevant calculations: {lesson["title"].lower()} formulae, percentage error, uncertainty propagation, graph gradients, log scales.</p>
</div>

<h3>Differentiation</h3>
<div class="key-point"><strong>Support:</strong><br>Pre-cut wires, labelled breadboard template, step-by-step photo guide, buddy system with confident peer.</div>
<div class="key-point"><strong>Stretch:</strong><br>Modify circuit for new specification. Add indicator LED. Interface with microcontroller. Design PCB layout.</div>

<h3>Plenary (5 minutes)</h3>
<div class="example"><div class="example-title">Results Review</div>
<p>Compare experimental vs theoretical values. Discuss discrepancies: tolerance, temperature, measurement loading, breadboard parasitics.</p></div>

<h3>Assessment Criteria</h3>
<ul>
<li><strong>Got it:</strong> Circuit works, measurements accurate, results table complete, graphs plotted correctly, anomalies discussed.</li>
<li><strong>Getting there:</strong> Circuit functions with help, measurements mostly correct, minor recording errors.</li>
<li><strong>Not yet:</strong> Circuit doesn't function, cannot use test equipment. Revisit breadboarding basics.</li>
</ul>
</section>

{practical_section}

<section class="section">
<h2>Homework Suggestions</h2>
<ul>
<li>Complete textbook/exam questions on {lesson["title"].lower()}</li>
<li>Simulate the circuit in Falstad/EveryCircuit/LTSpice — vary parameters, observe effects</li>
<li>Design a circuit variant: change one component to achieve a different specification</li>
<li>Write a practical report: aim, method, results, analysis, conclusion, evaluation</li>
<li>Research a real-world application of {lesson["title"].lower()} — present as 3-slide summary
</ul>
</section>

<section class="section">
<h2>Resources</h2>
<ul>
<li><a href="https://www.eduqas.co.uk/qualifications/electronics-gcse/" target="_blank" rel="noopener">Eduqas GCSE Electronics Specification</a></li>
<li><a href="https://www.falstad.com/circuit/" target="_blank" rel="noopener">Falstad Circuit Simulator (browser-based)</a></li>
<li><a href="https://www.allaboutcircuits.com/" target="_blank" rel="noopener">All About Circuits - Textbook and Reference</a></li>
<li><a href="https://www.electronics-tutorials.ws/" target="_blank" rel="noopener">Electronics Tutorials - Component Guides</a></li>
<li><a href="https://www.nxp.com/docs/en/data-sheet/74HC_HCT00.pdf" target="_blank" rel="noopener">Example Datasheet: 74HC00 Quad NAND Gate</a></li>
</ul>
</section>

</main>
<footer class="site-footer">
<p>GCSE Lessons - Free lesson plans for homeschooling</p>
<p>Content for educational purposes only. Always cross-reference with official specifications.</p>
<p>© 2025 | <a href="../../privacy.html">Privacy Policy</a> | <a href="mailto:gcselessons@scott.scottrix.co.uk">Contact</a></p>
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
</html>
'''

def generate_all():
    base = "/home/scott/src/gcselessons"
    
    # Create Statistics landing page
    with open(os.path.join(base, "statistics.html"), "w") as f:
        f.write(stats_landing_page())
    print("Created statistics.html")
    
    # Create Electronics landing page
    with open(os.path.join(base, "electronics.html"), "w") as f:
        f.write(elec_landing_page())
    print("Created electronics.html")
    
    # Create Statistics topic directories and lessons
    for strand in STATS_STRANDS:
        dir_path = os.path.join(base, "topics", strand["id"])
        os.makedirs(dir_path, exist_ok=True)
        for i, lesson in enumerate(strand["lessons"]):
            filename = f"{lesson['id']}-{lesson['title'].lower().replace(' ', '-')}.html"
            filepath = os.path.join(dir_path, filename)
            with open(filepath, "w") as f:
                f.write(stats_lesson_page(strand, lesson, i, len(strand["lessons"])))
            print(f"Created {strand['id']}/{filename}")
    
    # Create Electronics topic directories and lessons
    for strand in ELEC_STRANDS:
        dir_path = os.path.join(base, "topics", strand["id"])
        os.makedirs(dir_path, exist_ok=True)
        for i, lesson in enumerate(strand["lessons"]):
            filename = f"{lesson['id']}-{lesson['title'].lower().replace(' ', '-')}.html"
            filepath = os.path.join(dir_path, filename)
            with open(filepath, "w") as f:
                f.write(elec_lesson_page(strand, lesson, i, len(strand["lessons"])))
            print(f"Created {strand['id']}/{filename}")

if __name__ == "__main__":
    generate_all()
    print("\nAll files generated successfully!")