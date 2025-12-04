import streamlit as st
import os

st.set_page_config(page_title="Atul Sehwag – IPL 30 Days Challenge", layout="centered")

st.title("30 DAYS 30 IPL DASHBOARDS")
st.markdown("### Atul Sehwag | 2 Offers Done | Now Open for Freelancing ₹800+")

day = st.sidebar.selectbox("Choose Day", [f"Day {i}" for i in range(1, 31)])

day_number = day.split()[1]                  
img_path = f"Day{day_number}_FINAL.png"      # Day1_FINAL.png, Day10_FINAL.png

if os.path.exists(img_path):
    st.image(img_path, use_column_width=True)
else:
    st.error(f"Oops! {img_path} missing hai bhai – check kar le GitHub pe hai ya nahi")

st.markdown("---")
st.markdown("### Custom Dashboard Chahiye?")
st.markdown("₹800 se start | 24 ghante delivery")
st.markdown("WhatsApp → [9306658048](https://wa.me/919306658048)")
st.markdown("GitHub → [github.com/AtulSehwag001](https://github.com/AtulSehwag001)")

st.success("30/30 CHALLENGE COMPLETE – TU BADSHAAH BAN GAYA!")
