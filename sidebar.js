// GCSE Lessons - Sidebar Navigation
(function() {
var SUBJ_DATA = [
{id:'mathematics',name:'Maths'},{id:'english-language',name:'English Lang'},
{id:'english-literature',name:'English Lit'},{id:'combined-science',name:'Combined Sci'},
{id:'biology',name:'Biology'},{id:'chemistry',name:'Chemistry'},
{id:'physics',name:'Physics'},{id:'computer-science',name:'Comp Sci'},
{id:'geography',name:'Geography'},{id:'history',name:'History'},
{id:'religious-studies',name:'Rel Studies'},{id:'french',name:'French'},
{id:'german',name:'German'},{id:'spanish',name:'Spanish'},
{id:'art-and-design',name:'Art & Design'},{id:'music',name:'Music'},
{id:'drama',name:'Drama'},{id:'design-and-technology',name:'D&T'},
{id:'pe',name:'PE'},{id:'business',name:'Business'},
{id:'economics',name:'Economics'},{id:'psychology',name:'Psychology'},
{id:'sociology',name:'Sociology'},{id:'citizenship-studies',name:'Citizenship'},
{id:'media-studies',name:'Media'},{id:'food-preparation-nutrition',name:'Food & Nutrition'},
{id:'latin',name:'Latin'},{id:'astronomy',name:'Astronomy'},
{id:'geology',name:'Geology'},{id:'ancient-history',name:'Ancient Hist'},
{id:'classical-civilisation',name:'Class Civ'},{id:'law',name:'Law'},
{id:'dance',name:'Dance'},{id:'film-studies',name:'Film'},
{id:'electronics',name:'Electronics'},{id:'engineering',name:'Engineering'},
{id:'statistics',name:'Statistics'}
];

// Subject-specific affiliate cards
var SUBJECT_AFFILIATES = {
    "mathematics": [
        {title:"Scientific Calculators", search:"scientific+calculator+GCSE", desc:"Essential for GCSE Maths exams"},
        {title:"Graph Paper Pads", search:"graph+paper+a4+pad", desc:"A4 squared paper for maths"},
        {title:"Maths Revision Guides", search:"GCSE+Maths+revision+guides", desc:"CGP and other revision guides"},
    ],
    "biology": [
        {title:"Biology Revision Guides", search:"GCSE+Biology+revision+guides", desc:"CGP, Oxford, and more"},
        {title:"Microscope Slides", search:"microscope+slides+prepared", desc:"Prepared slides for biology practicals"},
        {title:"Lab Coats", search:"lab+coat+student", desc:"Protection for practical work"},
    ],
    "chemistry": [
        {title:"Chemistry Revision Guides", search:"GCSE+Chemistry+revision+guides", desc:"CGP, Oxford, and more"},
        {title:"Molecular Model Kits", search:"molecular+model+kit+organic", desc:"Visualise chemical structures"},
        {title:"Periodic Table Posters", search:"periodic+table+poster+large", desc:"Wall reference for chemistry"},
    ],
    "physics": [
        {title:"Physics Revision Guides", search:"GCSE+Physics+revision+guides", desc:"CGP, Oxford, and more"},
        {title:"Data Loggers", search:"data+logger+physics+education", desc:"For required practicals"},
        {title:"Multimeters", search:"digital+multimeter+student", desc:"Essential for electricity practicals"},
    ],
    "english-language": [
        {title:"English Language Guides", search:"GCSE+English+Language+revision", desc:"CGP, York Notes, and more"},
        {title:"Set Text Editions", search:"GCSE+English+set+texts", desc:"Annotated editions for study"},
        {title:"Highlighters & Pens", search:"highlighter+pens+study", desc:"For text annotation"},
    ],
    "english-literature": [
        {title:"Literature Study Guides", search:"GCSE+English+Literature+guides", desc:"York Notes, CGP, and more"},
        {title:"Set Text Collections", search:"GCSE+English+Literature+set+texts", desc:"Complete play/novel editions"},
        {title:"Annotation Sticky Notes", search:"sticky+notes+annotation", desc:"For text analysis"},
    ],
    "combined-science": [
        {title:"Combined Science Guides", search:"GCSE+Combined+Science+revision", desc:"Trilogy and Synergy guides"},
        {title:"Science Revision Cards", search:"GCSE+science+flashcards", desc:"Quick revision cards"},
        {title:"Required Practical Workbooks", search:"GCSE+science+required+practical+workbook", desc:"Lab book for practicals"},
    ],
    "computer-science": [
        {title:"CS Revision Guides", search:"GCSE+Computer+Science+revision", desc:"CGP, PG Online, and more"},
        {title:"Python Books", search:"python+programming+GCSE", desc:"Beginner to advanced Python"},
        {title:"Raspberry Pi Kits", search:"raspberry+pi+starter+kit", desc:"For programming projects"},
    ],
    "history": [
        {title:"History Revision Guides", search:"GCSE+History+revision+guides", desc:"Topic-specific guides"},
        {title:"Timeline Wall Charts", search:"history+timeline+poster", desc:"Visual reference for chronology"},
        {title:"Source Analysis Workbooks", search:"GCSE+history+source+analysis", desc:"Practice source questions"},
    ],
    "geography": [
        {title:"Geography Revision Guides", search:"GCSE+Geography+revision+guides", desc:"CGP, Oxford, and more"},
        {title:"Atlas", search:"world+atlas+student", desc:"Essential for map skills"},
        {title:"Case Study Flashcards", search:"GCSE+geography+case+study+cards", desc:"Key facts for case studies"},
    ],
    "religious-studies": [
        {title:"RS Revision Guides", search:"GCSE+Religious+Studies+revision", desc:"Christianity, Islam, and more"},
        {title:"Holy Text Extracts", search:"bible+quran+extracts+study", desc:"For quotation learning"},
        {title:"Ethics Workbooks", search:"GCSE+religious+studies+ethics", desc:"Theme-based practice"},
    ],
    "french": [
        {title:"French Revision Guides", search:"GCSE+French+revision+guides", desc:"AQA, Edexcel, Eduqas"},
        {title:"French Dictionaries", search:"french+english+dictionary+student", desc:"Collins, Oxford, Larousse"},
        {title:"Verb Conjugation Books", search:"french+verb+conjugation+guide", desc:"Bescherelle and alternatives"},
    ],
    "spanish": [
        {title:"Spanish Revision Guides", search:"GCSE+Spanish+revision+guides", desc:"AQA, Edexcel, Eduqas"},
        {title:"Spanish Dictionaries", search:"spanish+english+dictionary+student", desc:"Collins, Oxford, Larousse"},
        {title:"Verb Practice Books", search:"spanish+verb+practice+GCSE", desc:"Conjugation drills"},
    ],
    "german": [
        {title:"German Revision Guides", search:"GCSE+German+revision+guides", desc:"AQA, Edexcel, Eduqas"},
        {title:"German Dictionaries", search:"german+english+dictionary+student", desc:"Collins, Oxford, Langenscheidt"},
        {title:"Grammar Workbooks", search:"german+grammar+workbook+GCSE", desc:"Cases, word order, verbs"},
    ],
    "latin": [
        {title:"Latin Revision Guides", search:"GCSE+Latin+revision+guides", desc:"OCR, Eduqas, Edexcel"},
        {title:"Latin Dictionaries", search:"latin+dictionary+student", desc:"Pocket Oxford, Cassell's"},
        {title:"Set Text Editions", search:"GCSE+Latin+set+texts+edition", desc:"Annotated Virgil, Cicero"},
    ],
    "art-and-design": [
        {title:"Art Sketchbooks", search:"A3+sketchbook+art+student", desc:"Quality paper for portfolio"},
        {title:"Drawing Pencils Set", search:"drawing+pencils+graphite+set", desc:"2H to 8B range"},
        {title:"Watercolour Sets", search:"watercolour+paint+set+student", desc:"Winsor & Newton, Daler-Rowney"},
    ],
    "music": [
        {title:"Music Theory Guides", search:"GCSE+Music+theory+guide", desc:"ABRSM, Trinity, GCSE"},
        {title:"Manuscript Paper", search:"music+manuscript+paper+a4", desc:"For composition practice"},
        {title:"Revision Audio", search:"GCSE+music+listening+revision", desc:"Set works recordings"},
    ],
    "drama": [
        {title:"Drama Revision Guides", search:"GCSE+Drama+revision+guides", desc:"Set text analysis, devising"},
        {title:"Script Collections", search:"plays+GCSE+drama+set+texts", desc:"Published play editions"},
        {title:"Performance Journals", search:"drama+rehearsal+journal", desc:"Track devising process"},
    ],
    "dance": [
        {title:"Dance Revision Guides", search:"GCSE+Dance+revision+guides", desc:"Anthology, choreography"},
        {title:"Dancewear", search:"dance+leotard+tights+student", desc:"Black leotard, footless tights"},
        {title:"Performance DVDs", search:"professional+dance+works+DVD", desc:"Anthology works recordings"},
    ],
    "design-and-technology": [
        {title:"DT Revision Guides", search:"GCSE+Design+Technology+revision", desc:"Core and specialist"},
        {title:"Sketching Pens", search:"fineliner+pens+technical+drawing", desc:"0.1mm to 0.8mm"},
        {title:"Model Making Materials", search:"foam+board+balsa+wood+modelling", desc:"For prototype making"},
    ],
    "food-preparation-nutrition": [
        {title:"Food Revision Guides", search:"GCSE+Food+Preparation+Nutrition+revision", desc:"Recipe, nutrition, science"},
        {title:"Digital Scales", search:"digital+kitchen+scales+accurate", desc:"Precise weighing for NEA"},
        {title:"Cooking Equipment", search:"student+cooking+utensils+set", desc:"Pans, knives, thermometers"},
    ],
    "pe": [
        {title:"PE Revision Guides", search:"GCSE+PE+revision+guides", desc:"Anatomy, training, psychology"},
        {title:"Heart Rate Monitors", search:"heart+rate+monitor+chest+strap", desc:"For training analysis"},
        {title:"Sports Science Books", search:"sports+science+introduction", desc:"Physiology, biomechanics"},
    ],
    "business": [
        {title:"Business Revision Guides", search:"GCSE+Business+revision+guides", desc:"CGP, Tutor2u, and more"},
        {title:"Case Study Books", search:"GCSE+business+case+studies", desc:"Real business examples"},
        {title:"Financial Calculators", search:"financial+calculator+student", desc:"For finance topics"},
    ],
    "economics": [
        {title:"Economics Revision Guides", search:"GCSE+Economics+revision+guides", desc:"Micro and macro"},
        {title:"Economics Textbooks", search:"GCSE+Economics+textbook", desc:"Core textbooks"},
        {title:"Graph Paper", search:"economics+graph+paper+a4", desc:"For diagrams"},
    ],
    "psychology": [
        {title:"Psychology Revision Guides", search:"GCSE+Psychology+revision+guides", desc:"Studies, theories, methods"},
        {title:"Research Methods Workbooks", search:"psychology+research+methods+GCSE", desc:"Experiments, ethics"},
        {title:"Study Cards", search:"psychology+flashcards+GCSE", desc:"Key studies and theories"},
    ],
    "sociology": [
        {title:"Sociology Revision Guides", search:"GCSE+Sociology+revision+guides", desc:"Families, education, crime"},
        {title:"Sociology Textbooks", search:"GCSE+Sociology+textbook", desc:"Core concepts and theorists"},
        {title:"Essay Planning Pads", search:"essay+planning+pad+a4", desc:"Structure long answers"},
    ],
    "citizenship-studies": [
        {title:"Citizenship Guides", search:"GCSE+Citizenship+revision+guides", desc:"Active citizenship, law"},
        {title:"Campaigning Guides", search:"how+to+campaign+guide", desc:"For active citizenship project"},
        {title:"UK Politics Books", search:"british+politics+introduction", desc:"Parliament, democracy"},
    ],
    "media-studies": [
        {title:"Media Revision Guides", search:"GCSE+Media+Studies+revision", desc:"Key concepts, industries"},
        {title:"Media Theory Books", search:"media+theory+introduction", desc:"Barthes, Baudrillard, etc."},
        {title:"Production Equipment", search:"video+camera+student+beginner", desc:"For NEA production"},
    ],
    "film-studies": [
        {title:"Film Revision Guides", search:"GCSE+Film+Studies+revision", desc:"US, UK, global film"},
        {title:"Film Analysis Books", search:"film+analysis+introduction", desc:"Mise-en-scène, editing"},
        {title:"Screenwriting Software", search:"screenwriting+software+student", desc:"Final Draft alternatives"},
    ],
    "engineering": [
        {title:"Engineering Revision Guides", search:"GCSE+Engineering+revision+guides", desc:"Materials, processes"},
        {title:"Technical Drawing Tools", search:"technical+drawing+set+student", desc:"Set squares, compasses"},
        {title:"CAD Software Guides", search:"fusion+360+tutorial+book", desc:"For CAD NEA"},
    ],
    "statistics": [
        {title:"Statistics Revision Guides", search:"GCSE+Statistics+revision+guides", desc:"Data, probability, inference"},
        {title:"Statistical Calculators", search:"scientific+calculator+statistics", desc:"With stats functions"},
        {title:"Graph Paper", search:"statistics+graph+paper+a4", desc:"For charts and diagrams"},
    ],
    "electronics": [
        {title:"Electronics Revision Guides", search:"GCSE+Electronics+revision+guides", desc:"Circuits, systems"},
        {title:"Component Kits", search:"electronics+component+kit+student", desc:"Resistors, capacitors, ICs"},
        {title:"Soldering Stations", search:"soldering+iron+station+student", desc:"For practical circuits"},
    ],
    "astronomy": [
        {title:"Astronomy Revision Guides", search:"GCSE+Astronomy+revision+guides", desc:"Edexcel specification"},
        {title:"Planispheres", search:"planisphere+star+chart", desc:"Night sky reference"},
        {title:"Binoculars", search:"astronomy+binoculars+10x50", desc:"For observation"},
    ],
    "geology": [
        {title:"Geology Revision Guides", search:"GCSE+Geology+revision+guides", desc:"Eduqas specification"},
        {title:"Rock/Mineral Kits", search:"rock+mineral+collection+kit", desc:"Hand specimens"},
        {title:"Field Equipment", search:"geology+hammer+hand+lens", desc:"For fieldwork"},
    ],
    "ancient-history": [
        {title:"Ancient History Guides", search:"GCSE+Ancient+History+revision", desc:"Greece, Rome, Persia"},
        {title:"Source Books", search:"ancient+history+source+book", desc:"Primary sources in translation"},
        {title:"Timeline Charts", search:"ancient+history+timeline+poster", desc:"Chronological reference"},
    ],
    "classical-civilisation": [
        {title:"Class Civ Guides", search:"GCSE+Classical+Civilisation+revision", desc:"Myth, religion, culture"},
        {title:"Homer Translations", search:"iliad+odyssey+translation+student", desc:"Penguin, Oxford Classics"},
        {title:"Mythology Guides", search:"greek+roman+mythology+guide", desc:"Gods, heroes, stories"},
    ],
    "law": [
        {title:"Law Revision Guides", search:"GCSE+Law+revision+guides", desc:"AQA specification"},
        {title:"Case Law Books", search:"english+legal+system+cases", desc:"Key cases and principles"},
        {title:"Statute Books", search:"statute+book+student", desc:"Key legislation"},
    ],
    "dance": [
        {title:"Dance Revision Guides", search:"GCSE+Dance+revision+guides", desc:"Anthology, performance"},
        {title:"Dancewear", search:"dance+leotard+student", desc:"Black leotard, tights"},
        {title:"Performance Recordings", search:"professional+dance+works+video", desc:"Anthology pieces"},
    ],
};

// Default affiliates
var DEFAULT_AFFILIATES = [
    {title:"GCSE Revision Guides", search:"GCSE+revision+guides", desc:"All subjects covered"},
    {title:"Study Stationery", search:"study+stationery+student", desc:"Pens, highlighters, flashcards"},
    {title:"Revision Timetable", search:"revision+timetable+planner", desc:"Plan your study schedule"},
];

function getAffiliates(subjectId) {
    return SUBJECT_AFFILIATES[subjectId] || DEFAULT_AFFILIATES;
}

function buildAdRightHtml(subjectId) {
    var affiliates = getAffiliates(subjectId);
    var html = '';
    affiliates.forEach(function(a) {
        html += '<a href="https://www.amazon.co.uk/s?k=' + a.search + '&tag=scottrix-21" class="affiliate-card" target="_blank" rel="nofollow noopener">' +
            '<div class="affiliate-card-title">' + a.title + '</div>' +
            '<div class="affiliate-card-desc">' + a.desc + '</div>' +
            '<div class="affiliate-card-store"><img src="../images/assets/amazon-smile.svg" alt="Amazon"> amazon.co.uk</div>' +
        '</a>';
    });
    // Add fixed affiliates
    html += '<a href="https://join.fastmail.com/0d63b2d52105" class="affiliate-card" target="_blank" rel="nofollow noopener">' +
        '<div class="affiliate-card-title">Fastmail \u2014 Private Email</div>' +
        '<div class="affiliate-card-desc">Privacy-first email with no ads and no tracking</div>' +
        '<div class="affiliate-card-store">fastmail.com</div>' +
    '</a>';
    html += '<a href="https://www.dynadot.com/?ref=scottrix" class="affiliate-card" target="_blank" rel="nofollow noopener">' +
        '<div class="affiliate-card-title">Dynadot \u2014 Domain Registration \u2192</div>' +
        '<div class="affiliate-card-desc">Register or transfer domains with free SSL and affordable pricing</div>' +
        '<div class="affiliate-card-store">dynadot.com</div>' +
    '</a>';
    html += '<a href="https://zen.mention-me.com/m/ol/yv3qsjix-scott-harrison" class="affiliate-card" target="_blank" rel="nofollow noopener">' +
        '<div class="affiliate-card-title">Zen Internet \u2014 UK Broadband \u2192</div>' +
        '<div class="affiliate-card-desc">Award-winning UK broadband with no data caps and great customer service</div>' +
        '<div class="affiliate-card-store">zen.co.uk</div>' +
    '</a>';
    return html;
}

var path = location.pathname;
var currentPage = path.split('/').pop().replace('.html','');
var isTopicPage = path.indexOf('/topics/') !== -1;
var isLandingPage = !isTopicPage && currentPage !== 'index' && currentPage !== '';
if (currentPage === 'index' || currentPage === '') return;

var nav = document.createElement('nav');
nav.className = 'sidebar';
nav.id = 'sidebar-nav';

var subjectSlug = '';

function subjectFromHref(href) {
if (!href) return '';
if (href.indexOf('#') !== -1) return '';
if (href.indexOf('index') !== -1) return '';
if (/(?:^|\/)\.?$/.test(href)) return '';
var m = /([a-z][a-z0-9-]+)\.html$/.exec(href);
return m ? m[1] : '';
}

if (isLandingPage) {
subjectSlug = currentPage;
nav.innerHTML = '<h3>Subjects</h3><ul>' +
SUBJ_DATA.map(function(s) {
var cls = s.id === currentPage ? ' class="active"' : '';
return '<li><a href="' + s.id + '.html"' + cls + '>' + s.name + '</a></li>';
}).join('') + '</ul>';
} else if (isTopicPage) {
var segs = path.split('/');
var bcLinks = document.querySelectorAll('.breadcrumb a');
for (var i = 0; i < bcLinks.length; i++) {
subjectSlug = subjectFromHref(bcLinks[i].getAttribute('href') || '');
if (subjectSlug) break;
}
if (!subjectSlug) {
var navLinks = document.querySelectorAll('header .nav a');
for (var j = 0; j < navLinks.length; j++) {
subjectSlug = subjectFromHref(navLinks[j].getAttribute('href') || '');
if (subjectSlug) break;
}
}
var prefix = '../../';
var landingHref = prefix + subjectSlug + '.html';
var currentTopicFile = segs[segs.length - 1];

if (!subjectSlug) {
nav.innerHTML = '<h3>Subjects</h3><ul>' +
SUBJ_DATA.map(function(s) {
return '<li><a href="' + s.id + '.html">' + s.name + '</a></li>';
}).join('') + '</ul>';
} else {
nav.innerHTML = '<h3>Lessons</h3><ul id="sidebar-topics"><li><a href="' + landingHref + '">&larr; ' + (subjectSlug.replace(/-/g,' ')) + '</a></li></ul>';

fetch(landingHref).then(function(r) { return r.text(); }).then(function(html) {
var parser = new DOMParser();
var doc = parser.parseFromString(html, 'text/html');
var cards = doc.querySelectorAll('a.topic-card');
var ul = document.getElementById('sidebar-topics');
if (!ul) return;
var items = '<li><a href="' + landingHref + '">&larr; ' + (subjectSlug.replace(/-/g,' ')) + '</a></li>';
cards.forEach(function(card) {
var href = card.getAttribute('href') || '';
var name = card.querySelector('.topic-name');
var id = card.querySelector('.topic-id');
var label = (id ? id.textContent.trim() + ': ' : '') + (name ? name.textContent.trim() : '');
var fullHref = prefix + href;
var isActive = href.indexOf(currentTopicFile) !== -1;
var cls = isActive ? ' class="active"' : '';
items += '<li><a href="' + fullHref + '"' + cls + '>' + label + '</a></li>';
});
ul.innerHTML = items;
}).catch(function(err) { console.error('Sidebar fetch failed:', landingHref, err); });
}
} else {
nav.innerHTML = '<h3>Subjects</h3><ul>' +
SUBJ_DATA.map(function(s) {
return '<li><a href="' + s.id + '.html">' + s.name + '</a></li>';
}).join('') + '</ul>';
}

document.body.appendChild(nav);

// Right-side ad rail
var adRail = document.createElement('aside');
adRail.className = 'ad-right';
adRail.id = 'ad-rail-right';
adRail.innerHTML = buildAdRightHtml(subjectSlug);
document.body.appendChild(adRail);

var btn = document.createElement('button');
btn.className = 'sidebar-toggle';
btn.textContent = '\u2630';
btn.id = 'sidebar-toggle-btn';
btn.setAttribute('aria-label', 'Toggle sidebar');
btn.addEventListener('click', function() {
nav.classList.toggle('open');
btn.textContent = nav.classList.contains('open') ? '\u2715' : '\u2630';
});
document.body.appendChild(btn);

document.addEventListener('click', function(e) {
if (nav.classList.contains('open') && !nav.contains(e.target) && e.target !== btn) {
nav.classList.remove('open');
btn.textContent = '\u2630';
}
});

})();
