import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import json

BASE_URL = "https://www.angelone.in/support"
visited = set()
collected = []

def is_valid(url):
    return url.startswith(BASE_URL) and url not in visited and "javascript:void" not in url and 'hindi' not in url and '#' not in url

def clean_text(soup):
    for script in soup(["script", "style"]):
        script.decompose()
    return soup.get_text(separator="\n", strip=True)

def crawl(url):
    try:
        time.sleep(0.5)
        print(url)
        response = requests.get(url, timeout=10)
        print(response)
        if response.status_code != 200:
            return

        soup = BeautifulSoup(response.text, "html.parser")
        text = clean_text(soup)

        if len(text) > 100:
            collected.append({
                "url": url,
                "content": text
            })

        visited.add(url)

        for a_tag in soup.find_all("a", href=True):
            next_url = urljoin(url, a_tag['href'])
            if is_valid(next_url):
                crawl(next_url)

    except Exception as e:
        print(f"[!] Failed to crawl {url}: {e}")

if __name__ == "__main__":
    crawl(BASE_URL)

    with open("data/support_docs.json", "w", encoding="utf-8") as f:
        json.dump(collected, f, indent=2, ensure_ascii=False)

    print(f"\nCrawled {len(collected)} support pages.")

