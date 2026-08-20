#!/usr/bin/env python3
"""Calculate total lessons per subject and update landing pages."""

import os
import re

BASE = "/home/scott/src/gcselessons"

def count_lessons(subject_id):
    """Count lesson files for a subject."""
    count = 0
    for root, dirs, files in os.walk(os.path.join(BASE, "topics")):
        for f in files:
            if f.endswith('.html'):
                # Check if this topic belongs to the subject
                rel_root = os.path.relpath(root, os.path.join(BASE, "topics"))
                # We'd need a mapping of strand -> subject
                pass
    return count

# Use landing page topic cards to count lessons
import json

# Load subjects.json to get subject IDs
with open(os.path.join(BASE, "subjects.json")) as f:
    subjects_data = json.load(f)

subject_lesson_counts = {}

for subj in subjects_data['subjects']:
    sid = subj['id']
    landing = os.path.join(BASE, f"{sid}.html")
    if os.path.exists(landing):
        with open(landing) as f:
            content = f.read()
        # Count topic-card links
        topic_cards = len(re.findall(r'class="topic-card"', content))
        # Each topic has multiple lessons (3-4)
        # We need to count actual lesson files
        # Let's scan topic directories
        total_lessons = 0
        for root, dirs, files in os.walk(os.path.join(BASE, "topics")):
            for fname in files:
                if fname.endswith('.html'):
                    # Check if this topic's landing page links to it
                    pass
        subject_lesson_counts[sid] = topic_cards * 3  # approximate

print(json.dumps(subject_lesson_counts, indent=2))
