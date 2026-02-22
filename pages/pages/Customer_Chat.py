import streamlit as st
from pages.utils_data import seed_state

seed_state(st)

st.title("Customer Chat")
st.caption(f"User: **{st.session_state.get('role','')}**")

left, right = st.columns([1.6, 1])

def ai_reply(text: str) -> str:
    t = text.lower()
    if "gluten" in t:
        return "We offer gluten-free crust in sizes up to medium. Would you like pickup or delivery?"
    if "vegan" in t or "dairy" in t:
        return "We can do veggie toppings; cheese alternatives depend by location. Want me to list popular options?"
    if "deal" in t or "coupon" in t:
        return "I can suggest today’s best value combos—how many people are you feeding?"
    if "track" in t or "where" in t:
        return "I can help track it—what’s the order number (e.g., DM-1003)?"
    return "Got it. Want recommendations, or should I start building your order?"

with left:
    st.subheader("Chat Window")
    chat_box = st.container(border=True)
    with chat_box:
        for m in st.session_state["messages"]:
            st.markdown(f"**{'Customer' if m['role']=='customer' else 'AI'}:** {m['content']}")

    msg = st.text_input("Type a customer message…", key="chat_input")
    if st.button("Send", type="primary") and msg.strip():
        st.session_state["messages"].append({"role": "customer", "content": msg.strip()})
        st.session_state["messages"].append({"role": "ai", "content": ai_reply(msg.strip())})
        st.session_state["chat_input"] = ""

    st.subheader("Quick Actions")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("Suggest Items"):
            st.session_state["messages"].append({"role": "ai", "content": "Suggestions: Medium GF crust + Pepperoni OR GF Veggie + extra sauce."})
    with c2:
        if st.button("Place Order"):
            st.session_state["messages"].append({"role": "ai", "content": "Order flow started: Confirm crust, size, toppings, and delivery method."})
    with c3:
        if st.button("Track Order"):
            st.session_state["messages"].append({"role": "ai", "content": "Tracking opened: Avg ETA currently ~29 min (queue elevated)."})


with right:
    st.subheader("Agent Assist")
    st.code("We have gluten-free crust up to medium. Want your usual toppings?")
    st.code("I can recommend popular combos—how many people are you feeding?")
    st.warning("If allergy-sensitive: mention cross-contamination may be possible in shared kitchens.")
