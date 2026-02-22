import streamlit as st

st.set_page_config(page_title="Domino's AI Dashboard", layout="wide")

# ----- Sidebar -----
st.sidebar.title("Domino's")
st.sidebar.caption("AI Operations Dashboard")

menu = [
    "Customer Chat",
    "Orders",
    "Delivery Tracking",
    "AI Insights",
    "Staffing & Inventory",
    "Reports",
]
page = st.sidebar.radio("Sidebar Menu", menu, index=3)

# ----- Header -----
colA, colB, colC = st.columns([2, 1, 1])
with colA:
    st.title("Main Panel")
    st.caption("User: Store Manager / Shift Lead")
with colB:
    st.info("Store: Belleville")
with colC:
    st.success("AI: Online")

st.divider()

# ----- State -----
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "customer", "content": "What are your gluten-free options?"},
        {"role": "ai", "content": "We offer gluten-free crust in sizes up to medium."},
    ]

if "busy_window" not in st.session_state:
    st.session_state.busy_window = "6:00 PM - 9:00 PM"
if "driver_increase" not in st.session_state:
    st.session_state.driver_increase = 3
if "low_stock" not in st.session_state:
    st.session_state.low_stock = ["Mozzarella Cheese", "Gluten-Free Crust"]

# ----- Layout -----
left, right = st.columns([1.6, 1])

# ===== Left column: Chat + Quick Actions =====
with left:
    st.subheader("Customer Chat")

    chat_box = st.container(border=True)
    with chat_box:
        for m in st.session_state.messages:
            if m["role"] == "customer":
                st.markdown(f"**Customer:** {m['content']}")
            else:
                st.markdown(f"**AI:** {m['content']}")

    user_input = st.text_input("Type a message to assist the customer…", key="chat_input")

    def ai_reply(text: str) -> str:
        t = text.lower()
        if "gluten" in t:
            return "We offer gluten-free crust in sizes up to medium."
        if "vegan" in t or "dairy free" in t:
            return "We can suggest veggie toppings; cheese alternatives depend on location. Want me to check current options?"
        if "hours" in t or "open" in t:
            return "I can check store hours—what location are you ordering from?"
        return "Got it—want me to recommend popular items or start an order?"

    if st.button("Send", type="primary"):
        if user_input.strip():
            st.session_state.messages.append({"role": "customer", "content": user_input.strip()})
            st.session_state.messages.append({"role": "ai", "content": ai_reply(user_input.strip())})
            st.session_state.chat_input = ""

    st.subheader("Quick Actions")
    qa = st.container(border=True)
    with qa:
        c1, c2, c3 = st.columns(3)

        with c1:
            if st.button("Suggest Items"):
                st.session_state.messages.append(
                    {"role": "ai", "content": "Suggestions: Medium GF crust + Pepperoni; or GF Veggie + extra sauce."}
                )
        with c2:
            if st.button("Place Order"):
                st.session_state.messages.append(
                    {"role": "ai", "content": "Order flow started: Confirm crust + size + toppings + pickup/delivery."}
                )
        with c3:
            if st.button("Track Order"):
                st.session_state.messages.append(
                    {"role": "ai", "content": "Tracking opened: Current ETA 29 min (queue is elevated)."}
                )

# ===== Right column: AI Insights + Staffing & Inventory + Delivery Snapshot =====
with right:
    st.subheader("AI Insights")
    ai_card = st.container(border=True)
    with ai_card:
        st.write(f"**Predicted Busy Time:** {st.session_state.busy_window}")
        st.write(f"**Suggested Staff Increase:** +{st.session_state.driver_increase} Drivers")
        st.warning("Priority Alert: Delivery ETAs trending up")

        with st.expander("Adjust AI settings (for demo/testing)"):
            st.session_state.busy_window = st.text_input("Busy time window", st.session_state.busy_window)
            st.session_state.driver_increase = st.slider("Suggested driver increase", 0, 8, st.session_state.driver_increase)

    st.subheader("Staffing & Inventory")
    inv_card = st.container(border=True)
    with inv_card:
        st.write("**Low Stock Alerts:**")
        for item in st.session_state.low_stock:
            st.error(f"{item} — Reorder recommended")

        with st.expander("Update inventory alerts"):
            new_item = st.text_input("Add low-stock item")
            if st.button("Add Item"):
                if new_item.strip():
                    st.session_state.low_stock.append(new_item.strip())

            remove_item = st.selectbox("Remove item", ["(none)"] + st.session_state.low_stock)
            if st.button("Remove Selected"):
                if remove_item != "(none)":
                    st.session_state.low_stock = [x for x in st.session_state.low_stock if x != remove_item]

        st.write("**Suggested Actions:**")
        st.write("- Auto-create purchase order draft")
        st.write("- Adjust prep plan for peak window")

    st.subheader("Delivery Tracking Snapshot")
    deliv = st.container(border=True)
    with deliv:
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Orders in Queue", 14)
        with c2:
            st.metric("Avg ETA (min)", 29)

        st.progress(0.62, text="On-time deliveries (last 60 min): 62%")

st.caption("Prototype fidelity: Medium (interactive demo). Data shown is illustrative for the MIS project.")
