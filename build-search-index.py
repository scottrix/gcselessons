#!/usr/bin/env python3
"""Build search index for GCSE Lessons site."""

import json
import re
from pathlib import Path
from bs4 import BeautifulSoup

BASE = Path("/home/scott/src/gcselessons")

def extract_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Remove scripts and styles
    for tag in soup(['script', 'style']):
        tag.decompose()
    return soup.get_text(' ', strip=True)

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def parse_landing_page(filepath, subject_id):
    """Parse a subject landing page to extract topic cards."""
    html = filepath.read_text(encoding='utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    topics = []
    for card in soup.select('a.topic-card'):
        href = card.get('href', '')
        topic_id_el = card.select_one('.topic-id')
        topic_name_el = card.select_one('.topic-name')
        
        if not href or not topic_name_el:
            continue
            
        topic_id = topic_id_el.get_text(strip=True) if topic_id_el else ''
        topic_name = topic_name_el.get_text(strip=True)
        
        # Extract strand from href
        strand_match = re.search(r'topics/([^/]+)/', href)
        strand = strand_match.group(1) if strand_match else ''
        
        # Build search text
        search_parts = [topic_name, topic_id, strand]
        if subject_id:
            search_parts.append(subject_id.replace('-', ' '))
        search_text = ' '.join(search_parts).lower()
        
        topics.append({
            'id': topic_id,
            'name': topic_name,
            'url': href,
            'subjectId': subject_id,
            'subjectName': filepath.stem.replace('-', ' ').title(),
            'strandName': strand.replace('-', ' ').title(),
            'searchText': search_text
        })
    
    return topics

def parse_topic_page(filepath, subject_id):
    """Parse a topic lesson page."""
    html = filepath.read_text(encoding='utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    # Get topic title from h1
    h1 = soup.select_one('article.topic-header h1')
    if not h1:
        return None
    
    title = h1.get_text(strip=True)
    
    # Extract topic ID and name
    match = re.match(r'^([A-Z]\d+):\s*(.+)$', title)
    if match:
        topic_id, topic_name = match.groups()
    else:
        topic_id = ''
        topic_name = title
    
    # Get strand from path
    rel_path = filepath.relative_to(BASE)
    strand = rel_path.parts[1] if len(rel_path.parts) > 2 else ''
    
    # Get meta description
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    desc = meta_desc.get('content', '') if meta_desc else ''
    
    # Build search text
    search_parts = [topic_name, topic_id, strand, subject_id.replace('-', ' '), desc]
    search_text = ' '.join(search_parts).lower()
    
    return {
        'id': topic_id,
        'name': topic_name,
        'url': str(rel_path).replace('\\', '/'),
        'subjectId': subject_id,
        'subjectName': subject_id.replace('-', ' ').title(),
        'strandName': strand.replace('-', ' ').title(),
        'searchText': search_text
    }

def main():
    print("Building search index...")
    
    # Load subjects.json for subject list
    with open(BASE / 'subjects.json') as f:
        subjects_data = json.load(f)
    
    subjects = []
    all_topics = []
    
    # Process landing pages
    for subj in subjects_data['subjects']:
        sid = subj['id']
        landing_file = BASE / f"{sid}.html"
        if not landing_file.exists():
            print(f"  WARNING: Missing landing page for {sid}")
            continue
        
        # Add subject to index
        subjects.append({
            'id': sid,
            'name': subj['name'],
            'category': subj['category'],
            'url': f"{sid}.html",
            'boards': subj.get('boards', []),
            'papers': subj.get('papers', 0),
        })
        
        # Parse topics from landing page
        topics = parse_landing_page(landing_file, sid)
        all_topics.extend(topics)
        print(f"  {subj['name']}: {len(topics)} topics from landing page")
    
    # Also parse all topic lesson pages for richer search
    for topic_file in BASE.glob('topics/**/*.html'):
        # Extract subject from path
        rel = topic_file.relative_to(BASE)
        parts = rel.parts
        if len(parts) < 3:
            continue
        
        # Try to determine subject from strand directory
        # This is approximate - we'd need a mapping
        # For now, skip individual topic page parsing to avoid duplicates
        # The landing page extraction already gets all topics
        pass
    
    print(f"\nTotal subjects: {len(subjects)}")
    print(f"Total topics: {len(all_topics)}")
    
    # Write search index
    index = {
        'subjects': subjects,
        'topics': all_topics
    }
    
    with open(BASE / 'search-index.json', 'w') as f:
        json.dump(index, f, separators=(',', ':'))
    
    print(f"\nSearch index written to {BASE / 'search-index.json'}")
    print(f"Size: {(BASE / 'search-index.json').stat().st_size / 1024:.1f} KB")

if __name__ == '__main__':
    main()
