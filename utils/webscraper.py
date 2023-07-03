```python
import requests
from bs4 import BeautifulSoup

def scrape_web(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None
    except Exception as err:
        print(f'Other error occurred: {err}')
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.prettify()
```