```python
import requests
from bs4 import BeautifulSoup

def search_google(query):
    GOOGLE_SEARCH_URL = "https://www.google.com/search"
    HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    params = {"q": query}
    
    response = requests.get(GOOGLE_SEARCH_URL, headers=HEADERS, params=params)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        results = []
        for g in soup.find_all('div', class_='g'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3').text
                item = {
                    "title": title,
                    "link": link
                }
                results.append(item)
        return results
    else:
        return None
```