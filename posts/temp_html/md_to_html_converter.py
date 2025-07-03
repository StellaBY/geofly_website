#!/usr/bin/env python3
import argparse
import os
import math
import re
import glob
import pathlib
from datetime import datetime
import frontmatter
import markdown
from jinja2 import Template

# Constants
WORDS_PER_MINUTE = 200
DATE_PATTERN = re.compile(r"(\d{4}-\d{2}-\d{2})")
# Match Markdown images with optional attribute blocks
IMAGE_MD_PATTERN = re.compile(r'!\[([^\]]*)\]\(([^)]+?)\)(?:\s*\{:[^}]+\})?')
# Jekyll prefix pattern
JEKYLL_PREFIX_PATTERN = re.compile(r'\{\{\s*site\.url\s*\}\}\s*\{\{\s*site\.baseurl\s*\}\}')
# Match HTML <img> tags
HTML_IMG_PATTERN = re.compile(r'<img\s+([^>]*?)src="([^"]+)"([^>]*?)>')


def estimate_reading_time(text):
    words = len(text.split())
    minutes = max(1, math.ceil(words / WORDS_PER_MINUTE))
    return f"{minutes} minute{'s' if minutes > 1 else ''} read"


def extract_date_from_filename(fn):
    m = DATE_PATTERN.search(fn)
    if m:
        return datetime.strptime(m.group(1), "%Y-%m-%d")
    return None


def load_template(path):
    return Template(pathlib.Path(path).read_text(encoding='utf-8'))


def convert_file(md_path, template, output_dir):
    # Resolve and load Markdown
    md_file = pathlib.Path(md_path).expanduser().resolve()
    if not md_file.exists():
        raise FileNotFoundError(f"{md_file} does not exist.")
    raw = md_file.read_text(encoding='utf-8')

    # Parse frontmatter
    post = frontmatter.loads(raw)

    # Title extraction
    title = post.get('title') or next((line[2:].strip() for line in raw.splitlines() if line.startswith('# ')), md_file.stem)

    # Rewrite Markdown image paths and strip attribute blocks
    content_md = post.content
    def rewrite_md_img(match):
        alt, path = match.group(1), match.group(2)
        # Remove Jekyll prefix
        clean_path = JEKYLL_PREFIX_PATTERN.sub('', path)
        filename = os.path.basename(clean_path)
        return f'![{alt}](images/{filename})'
    content_md = IMAGE_MD_PATTERN.sub(rewrite_md_img, content_md)

    # Convert Markdown to HTML
    content_html = markdown.markdown(content_md, extensions=['fenced_code', 'tables'])

    # Rewrite HTML <img> tags: remove jekyll prefix, strip style/attribute blocks, keep alt if present
    def rewrite_html_img(match):
        before_attrs = match.group(1)
        src = match.group(2)
        after_attrs = match.group(3)
        # Clean Jekyll variables
        clean_src = JEKYLL_PREFIX_PATTERN.sub('', src)
        filename = os.path.basename(clean_src)
        # Extract alt attribute
        alt_match = re.search(r'alt="([^"]*)"', before_attrs + after_attrs)
        alt_text = alt_match.group(1) if alt_match else ''
        alt_attr = f' alt="{alt_text}"' if alt_text else ''
        return f'<img src="images/{filename}"{alt_attr}>'
    content_html = HTML_IMG_PATTERN.sub(rewrite_html_img, content_html)

    # Estimate reading time from original content
    reading_time = estimate_reading_time(post.content)

    # Format updated date
    date = extract_date_from_filename(md_file.name)
    updated = date.strftime('%B %d, %Y') if date else ''

    # Render with template
    html = template.render(
        title=title,
        reading_time=reading_time,
        content=content_html,
        updated=updated
    )

    # Write output
    out_fn = md_file.with_suffix('.html').name
    out_path = pathlib.Path(output_dir) / out_fn
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding='utf-8')
    print(f"✅ Converted {md_file.name} -> {out_path}")


def main():
    parser = argparse.ArgumentParser(description='Convert Markdown files to HTML with metadata.')
    parser.add_argument('--input-dir', required=True, help='Directory containing Markdown files')
    parser.add_argument('--output-dir', required=True, help='Directory to write HTML files')
    parser.add_argument('--template', required=True, help='Path to Jinja2 HTML template')
    args = parser.parse_args()

    template = load_template(args.template)
    pattern = os.path.join(args.input_dir, '**', '*.md')
    for md_path in glob.glob(pattern, recursive=True):
        try:
            convert_file(md_path, template, args.output_dir)
        except Exception as e:
            print(f"❌ Skipping {md_path!r}: {e}")

if __name__ == '__main__':
    main()
