import streamlit as st
import matplotlib.pyplot as plt
from pages.utils_data import seed_state, staffing_recommendation

seed_state(st)

st.title("AI Insights")

forecast = st.session_state["forecast"]
orders = st.session_state["orders"]
rec = staffing_recommendation(orders, forecast)

c1, c2, c3 = st.columns(3)
c1.metric("Predicted Peak Orders", rec["peak_predicted_orders"])
c2.metric("Suggested Staff Increase", f"+{rec['suggested_additional_drivers']} Drivers")
c3.metric("Queued Orders", rec["queued"])

st.markdown("---")
st.subheader("Predicted Busy Window (Next 12 Hours)")

fig = plt.figure()
plt.plot(forecast["hour"], forecast["predicted_orders"])
plt.xticks(rotation=30)
plt.ylabel("Predicted Orders / Hour")
plt.xlabel("Hour")
st.pyplot(fig)
