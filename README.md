# 🧠 AuditAI — Agentic AI Website Auditor

An **Agentic AI-powered web application** built with **Streamlit** that audits any website and provides **SEO, performance, accessibility, and security insights**, along with **AI-generated fixes and optimized HTML**.

---

## 🚀 Demo
🔗 [Live App on Streamlit](https://auditai07.streamlit.app/)

## 🚀 Video Demo
[https://github.com/user-attachments/assets/1b2d5f1f-df86-4d24-a5c1-31b7d705ac9a](https://github.com/user-attachments/assets/07000346-7020-49b7-b4bd-30fbf6c649ac)

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

## 📸 Screenshots
### 🏠 Home Page
<img width="1887" height="754" alt="Screenshot 2026-01-31 184415" src="https://github.com/user-attachments/assets/2da141de-faf8-49d4-a3bf-30df7344460c" />

### ✅ Page 1
<img width="1880" height="803" alt="Screenshot 2026-01-31 184444" src="https://github.com/user-attachments/assets/90c03d12-2c95-465a-9d45-765ab34550ab" />

### ✅ Page 2
<img width="1906" height="820" alt="Screenshot 2026-01-31 184512" src="https://github.com/user-attachments/assets/9da20264-3848-4f27-ad50-a94fdb2bf7fb" />

### ✅ Page 3
<img width="1873" height="841" alt="Screenshot 2026-01-31 184550" src="https://github.com/user-attachments/assets/375cf176-758a-4025-8c93-910700a87f13" />

### ✅ Page 4
<img width="1879" height="787" alt="Screenshot 2026-01-31 184621" src="https://github.com/user-attachments/assets/4c89eb51-b91a-47e1-b487-1eb7e1d722f5" />

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

## 👨‍💻 Author
**Mirza Yasir Abdullah Baig**  

- 🌐 [Kaggle](https://www.kaggle.com/mirzayasirabdullah07)  
- 💼 [LinkedIn](https://www.linkedin.com/in/mirza-yasir-abdullah-baig/)  
- 💻 [GitHub](https://github.com/mirzayasirabdullahbaig07)  

---

## ⚠️ Disclaimer
This project is for **educational purposes only** and should **NOT** be used as a substitute for professional medical diagnosis.  

--- 

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/mirzayasirabdullahbaig07/AuditAI.git
cd AuditAI
