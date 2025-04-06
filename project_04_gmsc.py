import streamlit as st

st.title("🏢 Team Task Manager")

teams = ["Development", "Design", "Sales", "Support", "Operations"]

member = st.text_input("Team Member Name")
team = st.selectbox("Select Team", teams)
task = st.text_area("Describe Task")

if st.button("Assign Task"):
    if member and task:
        st.success(f"✅ Task assigned to **{member}** in **{team}** team.")
    else:
        st.warning("⚠️ Please enter both team member name and task.")

st.write("📌 **Streamline your team’s workflow efficiently!**")
