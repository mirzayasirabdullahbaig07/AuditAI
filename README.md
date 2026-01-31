# 🧠 AuditAI — Agentic AI Website Auditor

An **Agentic AI-powered web application** built with **Streamlit** that audits any website and provides **SEO, performance, accessibility, and security insights**, along with **AI-generated fixes and optimized HTML**.

---

## 🚀 Demo
🔗 *Live Demo:* _(Coming Soon / Local Deployment)_  

---

## 📌 Features

- 🔍 **Website Scanning**
  - Page load time
  - HTTPS detection
  - Page size analysis
  - Internal vs external links
  - Headings structure (H1, H2, H3)
  - Images without ALT attributes
  - Scripts, paragraphs, and links count

- 🤖 **Agentic AI Analysis**
  - Automatically detects website issues
  - Provides actionable AI-powered suggestions
  - Generates **HTML & SEO fix snippets**
  - Produces **fully optimized HTML**
  - Extracts top SEO keywords
  - Analyzes heading hierarchy

- 📊 **Interactive Dashboard**
  - Overall website score
  - SEO, Performance, Accessibility & Security scores
  - Gauge & radar charts
  - Bar charts & pie charts
  - Keyword word cloud
  - Heading hierarchy treemap
  - Page element heatmap

- ⬇️ **Download Optimized HTML**
  - One-click download of AI-improved webpage

---

## 🔍 Usage

1. Run the app locally using Streamlit.
2. Enter a valid website URL.
3. Click **Scan Website**.
4. View:
   - ⚠️ Detected issues
   - ✅ AI-generated suggestions
   - 📊 Visual audit dashboard
   - 🤖 Agentic AI fixes
5. Download the **optimized HTML** if available.

---

## 📊 How It Works

1. The app scans the website using **BeautifulSoup & Requests**.
2. Raw metrics are calculated (SEO, performance, accessibility).
3. Scan data is sent to **OpenAI** for agentic analysis.
4. AI returns:
   - Issues
   - Suggestions
   - Fix snippets
   - Optimized HTML
5. Results are visualized in a rich Streamlit dashboard.

---

## ⚙️ Tech Stack

- **Python 3.9+**
- **Streamlit** — Web UI
- **OpenAI API** — Agentic AI analysis
- **BeautifulSoup** — HTML parsing
- **Requests** — Web scraping
- **Plotly & Matplotlib** — Interactive charts
- **WordCloud** — Keyword visualization
- **dotenv** — Environment variables

---

## 📂 Project Structure


---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/mirzayasirabdullahbaig07/AuditAI.git
cd AuditAI
