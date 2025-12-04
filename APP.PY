# app.py  ← is naam se save kar

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Atul Sehwag – IPL 30 Days Challenge", layout="centered")

st.title("30 DAYS 30 IPL DASHBOARDS")
st.markdown("### Atul Sehwag | 2 Offers Done | Now Open for Freelancing ₹800+")

# Sidebar menu
day = st.sidebar.selectbox("Choose Day", [f"Day {i}" for i in range(1,31)])

# PNG load karo
img_path = f"{day.replace(' ', '')}_FINAL.png"   # Day20 → Day20_FINAL.png
if os.path.exists(img_path):
    st.image(img_path, use_column_width=True)
else:
    st.info("Ye wala abhi upload kar raha hoon – 2 min me aa jayega!")

# Contact section
st.markdown("---")
st.markdown("### Custom Dashboard Chahiye?")
st.markdown("₹800 se start | 24 ghante delivery")
st.markdown("WhatsApp → [9306658048](https://wa.me/919306658048)")
st.markdown("GitHub → [github.com/AtulSehwag001/Ipl_data_analysis](https://github.com/AtulSehwag001/Ipl_data_analysis)")

st.success("30/30 COMPLETE – AB TERA TIME AAYA HAI!")