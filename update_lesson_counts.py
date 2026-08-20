#!/usr/bin/env python3
"""Update landing pages to show lesson counts instead of paper counts."""

import os
import re

BASE = "/home/scott/src/gcselessons"

LESSON_COUNTS = {
    "english-language": 69,
    "english-literature": 75,
    "mathematics": 237,
    "biology": 114,
    "chemistry": 102,
    "physics": 87,
    "combined-science": 225,
    "computer-science": 99,
    "history": 63,
    "geography": 111,
    "religious-studies": 108,
    "french": 117,
    "spanish": 117,
    "german": 117,
    "art-and-design": 90,
    "music": 105,
    "drama": 90,
    "design-and-technology": 48,
    "pe": 75,
    "business": 78,
    "economics": 78,
    "psychology": 60,
    "sociology": 60,
    "citizenship-studies": 60,
    "media-studies": 72,
    "food-preparation-nutrition": 72,
    "latin": 72,
    "astronomy": 78,
    "geology": 78,
    "ancient-history": 78,
    "classical-civilisation": 78,
    "law": 60,
    "dance": 90,
    "film-studies": 72,
    "electronics": 57,
    "engineering": 60,
    "statistics": 54,
}

def update_index():
    """Update index.html subject cards to show lessons."""
    path = os.path.join(BASE, "index.html")
    with open(path) as f:
        content = f.read()
    
    def replace_papers(match, count):
        return match.group(1) + str(count) + " lessons" + match.group(3)
    
    for sid, count in LESSON_COUNTS.items():
        card_pattern = rf'(<a href="{re.escape(sid)}\.html" class="subject-card"[^>]*>.*?<div class="paper-count">)(\d+ paper[^<]*)(</div>)'
        content = re.sub(card_pattern, lambda m: replace_papers(m, count), content, flags=re.DOTALL)
    
    with open(path, 'w') as f:
        f.write(content)
    print("Updated index.html")

def update_landing_pages():
    """Update individual subject landing pages."""
    for sid, count in LESSON_COUNTS.items():
        path = os.path.join(BASE, f"{sid}.html")
        if not os.path.exists(path):
            continue
        with open(path) as f:
            content = f.read()
        
        # Replace "X papers" with lesson count
        content = re.sub(r'<div class="paper-count">\d+ papers?</div>', 
                        f'<div class="paper-count">{count} lessons</div>', content)
        
        with open(path, 'w') as f:
            f.write(content)
    
    print("Updated all landing pages")

def rebuild_search_index():
    import subprocess
    subprocess.run(["python3", "build-search-index.py"], cwd=BASE)

if __name__ == '__main__':
    update_index()
    update_landing_pages()
    rebuild_search_index()
