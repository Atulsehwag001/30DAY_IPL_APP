import streamlit as st
import os

st.set_page_config(page_title="Atul Sehwag – IPL 30 Days Challenge", layout="centered")

st.title("30 DAYS 30 IPL DASHBOARDS")
st.markdown("### Atul Sehwag | 2 Offers Done | Now Open for Freelancing ₹800+")

# Sidebar
day = st.sidebar.selectbox("Choose Day", [f"Day {i}" for i in range(1, 31)])

# Correct PNG name banao → Day 1 → Day1_FINAL.png
day_number = day.split()[1]                  # "Day 1" → "1"
if len(day_number) == 1:
    day_number = "0" + day_number            # Day 1 → Day01 (optional, tere pas Day1 hai toh chalega)
img_path = f"Day{day_number}_FINAL.png"      # Day1_FINAL.png, Day10_FINAL.png etc.

if os.path.exists(img_path):
    st.image(img_path, use_column_width=True)
else:
    st.error(f"Oops! {img_path} missing hai bhai – check kar le folder mein hai ya nahi")

st.markdown("---")
st.markdown("### Custom Dashboard Chahiye?")
st.markdown("₹800 se start | 24 ghante delivery")
st.markdown("WhatsApp → [9306658048](https://wa.me/919306658048)")
st.markdown("GitHub → [github.com/AtulSehwag001](https://github.com/AtulSehwag001)")

st.success("30/30 CHALLENGE COMPLETE – TU LEGEND BAN GAYA!")
