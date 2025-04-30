import streamlit as st
from PIL import Image

# Page setup
st.set_page_config(page_title="Minimum Wage in Europe", layout="centered")

# Load and display banner image (top, centered, larger)
image = Image.open("eu.jpg")  
st.image(image, use_container_width=True)

# Title and team
st.markdown("""
<h1 style='text-align: center; margin-top: 1.2rem;'>📊 Minimum Wage and Wage Growth Trends in Europe</h1>
<p style='text-align: center; font-size: 1rem; color: #444;'>👥 <b>Team Members:</b> Yongjun Zhu · Yue Wei · Lan Wang · Yuanjing Zhu</p>
<hr style='margin-top: 1.5rem;'>
""", unsafe_allow_html=True)

# ✨ Introduction
st.markdown("""
### Project Introduction

As the cost of living rises across Europe, minimum wage policies are under increasing scrutiny. Policymakers, researchers, and the public alike are asking:

- Are wage floors keeping up with inflation?
- Do wage increases correspond with real economic growth?
- How do wage policies differ across regions?

Our project answers these questions using **interactive visualizations** and data from **ILO**, **OECD**, and the **World Bank**.
""")

# ✨ Objectives
st.markdown("""
### Our Objectives

- Explore **trends in nominal and real minimum wages** from 2017–2023  
- Compare **minimum wages vs. actual income distributions**  
- Investigate the **relationship between GDP growth and wage change**  
- Visualize **geographic disparities** across European countries  
- Build an **interactive dashboard** to communicate these insights
""")

# ✨ Data & Methods
st.markdown("""
### Data & Methods

- **📚 Sources:** ILO Global Wage Report, OECD Minimum Wage Database, World Bank GDP  
- **🛠️ Preprocessing:** Standardized country names, harmonized inflation adjustments, handled missing data  
- **📊 Tools Used:**
    - `Seaborn` / `Matplotlib` – trend lines and comparisons  
    - `Folium` – choropleth maps for regional disparities  
    - `Plotly` – interactive scatter plots and animations
""")

# ✨ Summary line
st.markdown("""
This dashboard offers a **data-driven exploration of wage policy dynamics** across Europe, empowering users to compare regions and trends with clarity.
""")
