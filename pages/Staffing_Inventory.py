import streamlit as st
from pages.utils_data import seed_state

seed_state(st)

st.title("Staffing & Inventory")

inv = st.session_state["inventory"].copy()
inv["status"] = inv.apply(lambda r: "LOW" if r["on_hand"] < r["reorder_point"] else "OK", axis=1)

st.dataframe(inv, use_container_width=True, hide_index=True)
