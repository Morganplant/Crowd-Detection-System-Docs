import os
import urllib.parse
from panflute import Image

# Set a default value for the image directory
DEFAULT_IMAGE_DIR = "./attachments"

def action(elem, doc):
    if isinstance(elem, Image):
        url = elem.url.strip()

        if os.path.isabs(url):
            url = '/'.join(url.split(':')[1:]).replace('\\', '/')
        
        url = urllib.parse.unquote(url)
        abs_path = os.path.abspath(os.path.join(os.getcwd(), url.replace('/', '\\')))
        elem.url = os.path.join(os.path.dirname(abs_path), DEFAULT_IMAGE_DIR, os.path.basename(abs_path))

        return elem

if __name__ == '__main__':
    from panflute import run_filter
    run_filter(action)