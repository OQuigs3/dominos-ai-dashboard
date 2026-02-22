import streamlit as st

st.set_page_config(
    page_title="Domino’s AI Operations Dashboard (Prototype)",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("Domino’s (Prototype)")
st.sidebar.caption("AI Operations Dashboard")

role = st.sidebar.radio("User Role", ["Store Manager / Shift Lead", "Customer Service Agent"], index=0)
st.session_state["role"] = role

st.sidebar.markdown("---")
st.sidebar.success("Status: Deployed")
st.sidebar.caption("Use the Pages list below to navigate modules.")

st.title("Domino’s AI Operations Dashboard (Prototype)")
st.caption(f"Active user: **{role}**")

st.markdown(
    """
This is a **medium-fidelity interactive prototype** demonstrating how a Domino’s store could use an AI-enhanced dashboard
to manage customer chat, orders, delivery tracking, AI insights, staffing, inventory, and reporting.

Use the Pages in the left sidebar to navigate.
"""
)

col1, col2, col3 = st.columns(3)
with col1:
    st.info("Customer Chat + Quick Actions")
with col2:
    st.info("Orders + Delivery Tracking")
with col3:
    st.info("AI Insights + Staffing & Inventory")

st.markdown("---")
st.subheader("How to Demo This App")
st.markdown(
    """
1. Go to Customer Chat → ask a question  
2. Go to AI Insights → review busy-time prediction  
3. Go to Staffing & Inventory → view low stock alerts  
4. Go to Reports → download CSV data
"""
)
