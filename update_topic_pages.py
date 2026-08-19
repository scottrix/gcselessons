#!/usr/bin/env python3
"""Update all topic pages with affiliate topbar and script."""

import os
import re

BASE = "/home/scott/src/gcselessons/topics"

fastmail_topbar = '''
<a class="fastmail-topbar" data-banner="fastmail" href="https://join.fastmail.com/0d63b2d52105" target="_blank" rel="noopener"><img src="../../images/assets/FM Billboard 970x250.png" alt="Fastmail" loading="lazy"></a>
<a class="fastmail-topbar" data-banner="dynadot" href="https://www.dynadot.com/?ref=scottrix" target="_blank" rel="nofollow noopener" hidden><img src="../../images/assets/dynadot-banner.jpg" alt="Dynadot — register a new domain, web hosting, SSL" loading="lazy" onerror="this.parentElement.style.display='none';document.querySelector('[data-banner=fastmail]').hidden=false"></a>
<script>(function(){var fm=document.querySelector('[data-banner=fastmail]');var dd=document.querySelector('[data-banner=dynadot]');if(Math.random()<0.5){fm.hidden=true;dd.hidden=false}})();</script>'''

def update_topic_page(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # 1. Add fastmail/dynadot after topic-header article
    article_end = content.find('</article>')
    if article_end != -1:
        insert_pos = article_end + len('</article>')
        # Check if already has fastmail-topbar
        if 'fastmail-topbar' not in content:
            content = content[:insert_pos] + fastmail_topbar + content[insert_pos:]
    
    # 2. Add affiliate-images.js before </body>
    if 'affiliate-images.js' not in content:
        body_end = content.find('</body>')
        if body_end != -1:
            content = content[:body_end] + '<script src="../../affiliate-images.js"></script>\n' + content[body_end:]
    
    with open(filepath, 'w') as f:
        f.write(content)

def main():
    count = 0
    for root, dirs, files in os.walk(BASE):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                update_topic_page(filepath)
                count += 1
                if count % 200 == 0:
                    print(f"Processed {count} topic pages...")
    print(f"Total topic pages updated: {count}")

if __name__ == '__main__':
    main()
