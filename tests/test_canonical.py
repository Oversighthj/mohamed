import re
from pathlib import Path


def test_og_url_contains_expected_domain():
    html = Path('index.html').read_text(encoding='utf-8')
    match = re.search(r'<meta\s+property="og:url"\s+content="([^"]+)"', html, re.IGNORECASE)
    assert match, 'og:url meta tag not found'
    url = match.group(1)
    assert url.startswith('https://cydstumpel.nl'), f'Unexpected og:url {url}'
