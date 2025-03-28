import json
import httpx
from urllib.parse import urlparse, urlsplit

with open( 'guide-links.json', 'r') as f:
    guide_links = json.load( f )
    urls = [ link['url'] for link in guide_links ]

for url in urls:
    page_content = httpx.get( url )
    page_name = urlparse( url ).path.split('/')[ -1 ]

    with open( page_name, 'w', encoding='utf-8') as f:
        f.write( page_content.text )
