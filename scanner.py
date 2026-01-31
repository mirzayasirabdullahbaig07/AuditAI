from bs4 import BeautifulSoup
import time
from utils import safe_request

def scan_website(url):
    data = {}

    response = safe_request(url)
    if not response:
        return {"error": "Unable to fetch URL", "score": 0}

    start = time.time()
    soup = BeautifulSoup(response.text, "html.parser")
    load_time = round(time.time() - start, 2)

    # Page size in MB
    page_size_mb = len(response.content) / (1024*1024)

    # Count internal vs external links
    internal_links = 0
    external_links = 0
    for link in soup.find_all("a", href=True):
        href = link.get("href")
        if href.startswith("http") and url.split("//")[1] in href:
            internal_links += 1
        elif href.startswith("http"):
            external_links += 1

    # Heading counts
    headings_count = {
        "H1": len(soup.find_all("h1")),
        "H2": len(soup.find_all("h2")),
        "H3": len(soup.find_all("h3"))
    }

    data.update({
        "status_code": response.status_code,
        "load_time": load_time,
        "https": url.startswith("https"),
        "title": soup.title.string if soup.title else "Missing",
        "meta_description": bool(soup.find("meta", attrs={"name": "description"})),
        "h1_count": headings_count["H1"],
        "h2_count": headings_count["H2"],
        "h3_count": headings_count["H3"],
        "headings_count": headings_count,
        "images_without_alt": len([img for img in soup.find_all("img") if not img.get("alt")]),
        "links_count": len(soup.find_all("a")),
        "internal_links": internal_links,
        "external_links": external_links,
        "scripts_count": len(soup.find_all("script")),
        "paragraph_count": len(soup.find_all("p")),
        "page_size_mb": page_size_mb
    })

    return data
