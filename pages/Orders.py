import streamlit as st
from pages.utils_data import seed_state

seed_state(st)
orders = st.session_state["orders"].copy()

st.title("Orders")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Active", len(orders))
c2.metric("Queued", int((orders["status"]=="Queued").sum()))
c3.metric("Out for Delivery", int((orders["status"]=="Out for Delivery").sum()))
c4.metric("Avg ETA (min)", int(orders["eta_min"].mean()))

st.markdown("---")

status_filter = st.multiselect(
    "Filter by status",
    sorted(orders["status"].unique()),
    default=sorted(orders["status"].unique())
)
channel_filter = st.multiselect(
    "Filter by channel",
    sorted(orders["channel"].unique()),
    default=sorted(orders["channel"].unique())
)

view = orders[
    (orders["status"].isin(status_filter)) &
    (orders["channel"].isin(channel_filter))
].sort_values("created_min_ago", ascending=False)

st.dataframe(view, use_container_width=True, hide_index=True)
