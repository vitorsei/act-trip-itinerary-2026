from html.parser import HTMLParser
from pathlib import Path

root = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.images = []
        self.days = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a':
            self.links.append(attrs.get('href', ''))
        if tag == 'img':
            self.images.append(attrs)
        if tag == 'article' and attrs.get('class') == 'day':
            self.days.append(attrs)

page = Page()
page.feed((root / 'index.html').read_text())
assert len(page.ids) == len(set(page.ids)), 'Duplicate anchors'
assert all(url[1:] in page.ids for url in page.links if url.startswith('#')), 'Broken internal link'
assert [d['id'] for d in page.days] == [f'day-{i}' for i in range(1, 8)], 'Expected seven chronological days'
assert all('hidden' not in d for d in page.days), 'All seven days must be visible'
assert all('alt' in img and img.get('src') for img in page.images), 'Missing image description/source'
assert all((root / name).is_file() for name in ['assets/styles.css', 'assets/app.js', 'assets/favicon.svg', 'assets/route-map.svg', '.nojekyll'])
print(f'Passed: seven-day / six-night route, unique IDs, internal links, {len(page.images)} described images and all static assets.')
