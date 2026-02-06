import streamlit as st
import time
import random

st.set_page_config(page_title="Confidential Audit", page_icon="📊")

# SESSION STATE
if "started" not in st.session_state:
    st.session_state.started = False
if "decision" not in st.session_state:
    st.session_state.decision = None

st.title("Confidential Relationship Audit")
st.caption("Authorized CA Access Only")

st.write("Client: Us")
st.write("Lead Auditor: Her (Future CA)")
st.write("---")

# BEGIN BUTTON
if not st.session_state.started:
    if st.button("Begin Audit"):
        st.session_state.started = True
        st.rerun()

# MAIN AUDIT SCREEN
if st.session_state.started:

    st.subheader("Balance Sheet")

    assets = [
        "Laughter",
        "Food dates",
        "My attempt to be vegetarian 🥦",
        "K-pop playlist exposure 🎧",
        "Taylor Swift emotional bonding 🎤",
        "Care & support",
        "Future plans"
    ]

    liabilities = [
        "My overthinking",
        "Busy schedules",
        "Me not being a K-pop fan 😭"
    ]

    st.write("### Assets")
    for a in assets:
        st.write(f"✔ {a}")

    st.write("### Liabilities")
    for l in liabilities:
        st.write(f"• {l}")

    score = random.randint(97,100)
    st.metric("Net Relationship Worth", f"{score}%")

    st.write("---")
    st.subheader("Final Question")
    st.write("**Will you be my Valentine? 💖**")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Approve 💖"):
            st.session_state.decision = "yes"
            st.rerun()

    with col2:
        if st.button("Reject ❌"):
            st.session_state.decision = "no"
            st.rerun()

# YES RESULT
if st.session_state.decision == "yes":
    st.balloons()
    st.success("Audit Approved.")
    st.write("Valentine’s Date Confirmed 🌹")
    st.write("Preparing K-pop + Taylor Swift playlist…")

# NO RESULT
if st.session_state.decision == "no":
    st.error("Audit Rejection Submitted")

    with st.spinner("Re-auditing decision..."):
        time.sleep(2)

    st.write("Reviewing Taylor Swift heartbreak protocol…")
    time.sleep(1)
    st.write("Checking K-pop emotional damage index…")
    time.sleep(1)

    st.warning("System Notice:")
    st.write(
        "Rejection requires Form 143-Love, "
        "3 emotional audits, and one sad Taylor Swift playlist."
    )

    st.success(
        "Rejection classified as accounting error. "
        "Please re-evaluate and submit again."
    )