import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def show_dashboard(scan_data, ai_report, history=None):
    st.subheader("📊 Website Metrics Dashboard")

    # --- Top Metric Cards ---
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Overall Score", scan_data.get("overall_score", 0))
    col2.metric("SEO Score", scan_data.get("seo_score", 0))
    col3.metric("Performance Score", scan_data.get("performance_score", 0))
    col4.metric("Accessibility Score", scan_data.get("accessibility_score", 0))
    col5.metric("Security Score", scan_data.get("security_score", 0))

    # --- Gauge Chart ---
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=scan_data.get("overall_score", 50),
        title={'text': "Overall Score"},
        gauge={'axis': {'range': [0, 100]},
               'bar': {'color': "orange"},
               'steps': [
                   {'range': [0, 50], 'color': "red"},
                   {'range': [50, 80], 'color': "yellow"},
                   {'range': [80, 100], 'color': "green"}]}
    ))
    st.plotly_chart(fig_gauge, use_container_width=True)

    # --- SEO Metrics ---
    seo_data = pd.DataFrame({
        "Metric": ["H1", "H2", "H3", "Meta Description", "Images without ALT", "Links"],
        "Value": [
            scan_data.get("h1_count",0),
            scan_data.get("h2_count",0),
            scan_data.get("h3_count",0),
            1 if scan_data.get("meta_description") else 0,
            scan_data.get("images_without_alt",0),
            scan_data.get("links_count",0)
        ]
    })
    fig_seo = px.bar(seo_data, x="Metric", y="Value", text="Value", color="Value",
                     color_continuous_scale=px.colors.sequential.Oranges, title="SEO Metrics")
    st.plotly_chart(fig_seo, use_container_width=True)

    # --- Performance Metrics ---
    perf_data = pd.DataFrame({
        "Metric": ["Load Time (s)", "Scripts", "Paragraphs", "Page Size (MB)"],
        "Value": [
            scan_data.get("load_time",0),
            scan_data.get("scripts_count",0),
            scan_data.get("paragraph_count",0),
            round(scan_data.get("page_size_mb",0),2)
        ]
    })
    fig_perf = px.bar(perf_data, x="Metric", y="Value", text="Value", color="Value",
                      color_continuous_scale=px.colors.sequential.Teal, title="Performance Metrics")
    st.plotly_chart(fig_perf, use_container_width=True)

    # --- HTTPS Pie ---
    https_data = pd.DataFrame({
        "Metric": ["HTTPS", "Non-HTTPS"],
        "Value": [1 if scan_data.get("https") else 0, 0 if scan_data.get("https") else 1]
    })
    fig_https = px.pie(https_data, names="Metric", values="Value", color="Metric",
                       color_discrete_map={"HTTPS":"green","Non-HTTPS":"red"}, title="HTTPS Status")
    st.plotly_chart(fig_https, use_container_width=True)

    # --- Internal vs External Links Pie ---
    link_data = pd.DataFrame({
        "Metric": ["Internal", "External"],
        "Value": [scan_data.get("internal_links",0), scan_data.get("external_links",0)]
    })
    fig_links = px.pie(link_data, names="Metric", values="Value", color="Metric",
                       color_discrete_map={"Internal":"blue","External":"purple"}, title="Link Types")
    st.plotly_chart(fig_links, use_container_width=True)

    # --- Radar Chart: AI Scores ---
    categories = ["SEO","Performance","Accessibility","Security"]
    values = [
        scan_data.get("seo_score",50),
        scan_data.get("performance_score",50),
        scan_data.get("accessibility_score",50),
        scan_data.get("security_score",50)
    ]
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(r=values, theta=categories, fill='toself', name="AI Audit"))
    fig_radar.update_layout(polar=dict(radialaxis=dict(range=[0,100])), title="AI Audit Radar")
    st.plotly_chart(fig_radar, use_container_width=True)

    # --- Word Cloud ---
    st.subheader("🔑 Top Keywords")
    if ai_report.get("keywords"):
        text = " ".join(ai_report["keywords"])
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        plt.figure(figsize=(10,5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt)
    else:
        st.write("No keywords detected")

    # --- Heading Tree Map ---
    st.subheader("📝 Heading Structure")
    headings = ai_report.get("headings_count", {"H1":0,"H2":0,"H3":0})
    heading_data = pd.DataFrame({"Heading":list(headings.keys()), "Count":list(headings.values())})
    fig_tree = px.treemap(heading_data, path=["Heading"], values="Count", title="Headings Hierarchy")
    st.plotly_chart(fig_tree, use_container_width=True)

    # --- Heatmap ---
    st.subheader("🔥 Page Element Heatmap")
    heat_data = pd.DataFrame({
        "Element": ["Images w/o ALT","Links","Paragraphs","Scripts"],
        "Count": [scan_data.get("images_without_alt",0),
                  scan_data.get("links_count",0),
                  scan_data.get("paragraph_count",0),
                  scan_data.get("scripts_count",0)]
    })
    fig_heat = px.imshow([heat_data["Count"]], labels=dict(x="Element", y="Count"), text_auto=True,
                         title="Element Density Heatmap")
    st.plotly_chart(fig_heat, use_container_width=True)

    # --- AI Issues & Suggestions ---
    st.subheader("⚠️ AI Detected Issues")
    for i in ai_report.get("issues",[]):
        st.write("•", i)
    st.subheader("✅ AI Suggestions")
    for s in ai_report.get("suggestions",[]):
        st.write("•", s)

    # --- Historical Trend (Optional) ---
    if history:
        st.subheader("📈 Historical Score Trend")
        hist_df = pd.DataFrame(history)
        fig_trend = px.line(hist_df, x="date", y="overall_score", markers=True)
        st.plotly_chart(fig_trend, use_container_width=True)
