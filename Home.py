import streamlit as st
import os

# --- Page Config ---
st.set_page_config(page_title="European Wage Trends", page_icon="💶", layout="wide")

# --- Banner Image ---
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(CURRENT_DIR, "images", "banner_wage.jpg")
st.image(IMAGE_PATH, use_container_width=True)

# --- Main Title ---
st.markdown("""
# European Minimum Wages & Growth  
### 2017–2023 · A Data-Driven Exploration
""")

st.markdown("---")

# --- Project Introduction ---
st.subheader("📘 Project Introduction")
st.markdown("""
Europe’s labor markets are diverse and constantly evolving. In recent years, **minimum wages** have become a central topic of debate — not only as a tool for worker protection, but also as a reflection of economic strength and social policy.

This project investigates how **minimum wage policies** have shifted across European countries between 2017 and 2023.  
Our goal is to combine data analysis and visualization to provide a **comprehensive picture** of:
- Evolution of minimum wage(2017-2023)
- Wage growth trends (real vs. nominal)
- Economic growth (via GDP)
- Geographical disparities

By presenting interactive tools and clear visuals, we hope to make complex wage dynamics **accessible and actionable** for students, researchers, and policymakers alike.
""")

# --- Data & Methods Section ---
st.subheader("📊 Data & Methods")
st.markdown("""
**Sources**:  
- ILO Global Wage Database  
- OECD Minimum Wage Data  
- World Bank GDP Indicators  

**Goal**:  
Deliver a **clear, data-driven picture** of wage policies, economic trends, and regional disparities across Europe.
""")

st.markdown("---")

# --- Team Info ---
st.subheader("👥 Team members")
st.markdown("""
Group D · QMSS · Columbia University  
- **Yongjun Zhu**  
- **Yue Wei**  
- **Lan Wang**  
- **Yuanjing Zhu**
""")

# --- Footer ---
st.caption("© 2025 · Columbia University · QMSS Final Project")

