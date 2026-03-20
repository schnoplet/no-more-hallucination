import requests
from bs4 import BeautifulSoup
from cache_utils import load_cache, save_cache
from config import RETRIEVE_TOP_K

WIKI_API = "https://en.wikipedia.org/w/api.php"

def retrieve_docs(query: str):
    cache = load_cache(query)
    if cache:
        return cache

    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": query,
        "srlimit": RETRIEVE_TOP_K
    }
    resp = requests.get(WIKI_API, params=params).json()
    docs = []
    for item in resp.get("query", {}).get("search", []):
        page_title = item["title"]
        page_resp = requests.get(f"https://en.wikipedia.org/wiki/{page_title.replace(' ', '_')}")
        soup = BeautifulSoup(page_resp.text, "html.parser")
        text = " ".join([p.text for p in soup.find_all("p")])
        docs.append(text[:2000])  # truncate for efficiency
    save_cache(query, docs)
    return docs