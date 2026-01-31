import streamlit as st
from scanner import scan_website
from ai_analyzer import analyze_with_ai
from utils import normalize_url, is_valid_url
from scoring import calculate_score
from dashboard import show_dashboard

st.set_page_config(page_title="AI Website Auditor - Agentic", layout="wide")
st.title("🧠 AI Website Auditor - Agentic Edition")
st.write("Paste a website URL to scan, analyze, and get **AI-generated fixes** and optimized HTML!")

url = st.text_input("Enter Website URL")

if st.button("Scan Website"):
    if not url or not is_valid_url(url):
        st.warning("Please enter a valid URL")
    else:
        url = normalize_url(url)
        with st.spinner("Scanning website..."):
            scan_data = scan_website(url)

        if "error" in scan_data:
            st.error(scan_data["error"])
        else:
            with st.spinner("Analyzing with AI..."):
                ai_report = analyze_with_ai(scan_data)

            # Scores
            overall_score = calculate_score(scan_data)
            scan_data["overall_score"] = overall_score
            scan_data["seo_score"] = max(0, 100 - scan_data.get("images_without_alt",0)*5)
            scan_data["performance_score"] = max(0, 100 - scan_data.get("load_time",5)*10)
            scan_data["accessibility_score"] = max(0, 100 - scan_data.get("images_without_alt",0)*5)
            scan_data["security_score"] = 100 if scan_data.get("https") else 50

            # --- Dashboard (handles metrics and charts) ---
            show_dashboard(scan_data, ai_report)

            # --- Agentic AI Actions ---
            st.subheader("🤖 Agentic AI Actions")

            # Show fix snippets
            if ai_report.get("fix_snippets"):
                st.write("### Suggested Fix Snippets")
                for snippet in ai_report["fix_snippets"]:
                    st.code(snippet, language="html")

            # Download optimized HTML
            if ai_report.get("optimized_html"):
                st.write("### Download Optimized HTML")
                st.download_button(
                    label="Download Optimized HTML",
                    data=ai_report["optimized_html"],
                    file_name="optimized_page.html",
                    mime="text/html"
                )

            # Optional: View full AI suggestions
            st.subheader("⚠️ AI Suggestions & Issues")
            for issue in ai_report.get("issues", []):
                st.write("•", issue)
            for tip in ai_report.get("suggestions", []):
                st.write("•", tip)
