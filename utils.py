import re
import requests

def normalize_url(url):
    if not url.startswith(("http://", "https://")):
        return "https://" + url
    return url

def is_valid_url(url):
    regex = re.compile(
        r'^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([\/\w .-]*)*\/?$'
    )
    return re.match(regex, url) is not None

def safe_request(url, timeout=10):
    try:
        response = requests.get(
            url,
            timeout=timeout,
            headers={"User-Agent": "AI-Site-Auditor"}
        )
        return response
    except requests.exceptions.RequestException:
        return None
