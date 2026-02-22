import streamlit as st
from pages.utils_data import seed_state

seed_state(st)

st.title("Reports")

orders = st.session_state["orders"]
inv = st.session_state["inventory"]
forecast = st.session_state["forecast"]

st.download_button("Download Orders CSV", orders.to_csv(index=False), file_name="orders.csv", mime="text/csv")
st.download_button("Download Inventory CSV", inv.to_csv(index=False), file_name="inventory.csv", mime="text/csv")
st.download_button("Download Forecast CSV", forecast.to_csv(index=False), file_name="forecast.csv", mime="text/csv")
