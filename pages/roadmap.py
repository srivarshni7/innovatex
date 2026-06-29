import streamlit as st
from utils.ai_engine import get_ai_roadmap


def show_roadmap():

    st.title("🛣️ AI Roadmap Generator")

    if "project" not in st.session_state:
        st.warning("⚠️ Please evaluate a project first.")
        return

    project = st.session_state["project"]

    st.subheader(f"🚀 {project['title']}")

    if st.button("🤖 Generate AI Roadmap"):

        with st.spinner("Generating roadmap..."):

            roadmap = get_ai_roadmap(project)

        st.success("Your AI Roadmap")

        st.markdown(roadmap)