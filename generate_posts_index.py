#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import pathlib
import re
from datetime import datetime
from bs4 import BeautifulSoup  # required: pip install beautifulsoup4
from jinja2 import Template

# ==== SETTING SECTION ======================================================
# 1. posts_dir:
posts_dir = 'posts'  # posts/*.html

# 2. output_path：
output_path = 'post.html'

# 3. posts_list_template_path: templates/posts_list.html
posts_list_template_path = 'templates/posts_list.html'

# 4. snippet_words：
snippet_words = 100
# ==============================================================


# Helper function: grab the date from the file name
def extract_date(fn):
    m = re.search(r'(\d{4}-\d{2}-\d{2})', fn)
    return datetime.strptime(m.group(1), '%Y-%m-%d') if m else None

# Helper function: Extract <h1> tags from HTML files
def parse_post(fpath):
    soup = BeautifulSoup(open(fpath, encoding='utf-8'), 'html.parser')
    # Title from first <h1>
    h1 = soup.find('h1')
    title = h1.get_text(strip=True) if h1 else os.path.basename(fpath)

    # Reading time
    rt = soup.find('p', class_='reading-time')
    reading_time = rt.get_text(strip=True) if rt else ''

    # Snippet: first paragraph excluding reading-time
    paragraphs = [p for p in soup.find_all('p') if 'reading-time' not in p.get('class', [])]
    if paragraphs:
        text = paragraphs[0].get_text(separator=' ', strip=True)
        words = text.split()
        snippet = ' '.join(words[:snippet_words])
    else:
        snippet = ''

    # Image: first image, use absolute path to /posts/images/
    img = soup.find('img')
    if img and img.has_attr('src'):
        image_name = os.path.basename(img['src'])
        image_url = f"./{posts_dir}/images/{image_name}"
    else:
        image_url = ''

    # URL to the post
    url = os.path.join(posts_dir, os.path.basename(fpath)).replace('\\', '/')

    # Date
    date = extract_date(os.path.basename(fpath))
    date_formatted = date.strftime('%B %d, %Y') if date else ''

    return {
        'title': title,
        'reading_time': reading_time,
        'snippet': snippet,
        'image_url': image_url,
        'url': url,
        'date': date,
        'date_formatted': date_formatted,
    }

# ---------------------------------------
def main():
    # 1. Reading Templates
    tpl = Template(open(posts_list_template_path, encoding='utf-8').read())

    # 2. Scan All .html
    files = glob.glob(os.path.join(posts_dir, '*.html'))
    posts = [parse_post(f) for f in files if extract_date(os.path.basename(f))]

    # 3. Sort by date descending
    posts.sort(key=lambda x: x['date'], reverse=True)

    # 4. Render and write output
    out = tpl.render(posts=posts)
    pathlib.Path(output_path).write_text(out, encoding='utf-8')
    print(f"✅ Generated {output_path} with {len(posts)} posts")

if __name__ == '__main__':
    main()
