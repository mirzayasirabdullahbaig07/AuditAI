from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_with_ai(scan_data):
    """
    Returns:
    - issues: list of problems
    - suggestions: list of improvements
    - fix_snippets: code snippets for fixes
    - optimized_html: full HTML with improvements (agentic AI)
    - keywords: top keywords
    - headings_count: H1/H2/H3 count
    """
    # Generate dummy keywords from title
    keywords = re.findall(r'\b\w+\b', scan_data.get("title", ""))[:10]

    prompt = f"""
You are a website audit and optimization expert.
Analyze this website scan data and provide:
1) issues (list)
2) suggestions (list)
3) fix_snippets (list of HTML/SEO fixes)
4) optimized_html (full HTML content with improvements applied)
5) keywords (list)
6) headings_count (dict of H1, H2, H3 counts)

Respond ONLY in JSON format.

Scan Data:
{json.dumps(scan_data, indent=2)}
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a website audit and optimization expert"},
                {"role": "user", "content": prompt},
            ],
            temperature=0.5,
        )
        content = response.choices[0].message.content
        ai_report = json.loads(content)

        # Fallbacks
        ai_report.setdefault("keywords", keywords)
        ai_report.setdefault("headings_count", scan_data.get("headings_count", {}))
        ai_report.setdefault("fix_snippets", [])
        ai_report.setdefault("optimized_html", "")
        return ai_report

    except Exception as e:
        # Fallback
        return {
            "issues": [
                f"H1 tags found: {scan_data.get('h1_count',0)}",
                f"Images without ALT: {scan_data.get('images_without_alt',0)}",
                f"Page load time: {scan_data.get('load_time',0)}s"
            ],
            "suggestions": [
                "Add missing meta description",
                "Optimize images and include ALT text",
                "Improve page speed"
            ],
            "fix_snippets": [
                "<meta name='description' content='Your description here'>",
                "<img src='image.jpg' alt='Descriptive text'>"
            ],
            "optimized_html": "<!-- Add optimized HTML here -->",
            "keywords": keywords,
            "headings_count": scan_data.get("headings_count", {})
        }
