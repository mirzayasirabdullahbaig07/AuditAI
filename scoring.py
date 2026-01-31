def calculate_score(scan_data):
    score = 0
    score += 15 if scan_data.get("https") else 0

    load_time = scan_data.get("load_time", 5)
    if load_time <= 1: score += 15
    elif load_time <= 3: score += 10
    else: score += 5

    score += 10 if scan_data.get("title") != "Missing" else 0
    score += 10 if scan_data.get("meta_description") else 0
    score += 10 if scan_data.get("h1_count", 0) >= 1 else 5

    missing_alt = scan_data.get("images_without_alt", 0)
    score += max(0, 10 - missing_alt*2)

    score += min(5, scan_data.get("links_count", 0)*0.1)
    score += min(5, scan_data.get("scripts_count", 0)*0.1)

    paragraphs = scan_data.get("paragraph_count", 0)
    score += 10 if paragraphs >= 3 else max(0, paragraphs*3)

    score += 10 if scan_data.get("status_code") == 200 else 0

    return round(min(score, 100), 2)
