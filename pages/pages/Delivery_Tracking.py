import streamlit as st
from pages.utils_data import seed_state

seed_state(st)

st.title("Delivery Tracking")

drivers = st.session_state["drivers"]
orders = st.session_state["orders"]

c1, c2, c3 = st.columns(3)
c1.metric("Drivers Active", int((drivers["status"]=="On Delivery").sum()))
c2.metric("Orders Out", int((orders["status"]=="Out for Delivery").sum()))
c3.metric("Late Risk (High)", int((drivers["late_risk"]=="High").sum()))

st.markdown("---")
st.subheader("Drivers")
st.dataframe(drivers, use_container_width=True, hide_index=True)
