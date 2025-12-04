import streamlit as st
import os

st.set_page_config(page_title="Atul Sehwag – IPL 30 Days Challenge", layout="centered")

st.title("30 DAYS 30 IPL DASHBOARDS")
st.markdown("### Atul Sehwag | 2 Offers Done | Now Open for Freelancing ₹800+")

day = st.sidebar.selectbox("Choose Day", [f"Day {i}" for i in range(1, 31)])

# TERE PNGs ka exact naam → DAY1_FINAL.png (capital DAY)
img_path = f"DAY{day.split()[1]}_FINAL.png"     # ← YE WAALA LINE SABSE IMPORTANT HAI

if os.path.exists(img_path):
    st.image(img_path, use_column_width=True)
else:
    st.error(f"Missing → {img_path}")

st.markdown("---")
st.markdown("### Custom Dashboard Chahiye?")
st.markdown("₹800 se start | 24 ghante delivery")
st.markdown("WhatsApp → [9306658048](https://wa.me/919306658048)")
st.markdown("GitHub → [github.com/AtulSehwag001](https://github.com/AtulSehwag001)")

st.success("30/30 CHALLENGE COMPLETE – TU BADSHAAH BAN GAYA!")
