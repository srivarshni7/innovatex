import streamlit as st


def show_history():

    st.title("📚 Project History")

    if "history" not in st.session_state or len(st.session_state["history"]) == 0:
        st.info("No projects found yet.")
        return

    for i, project in enumerate(reversed(st.session_state["history"]), 1):

        with st.expander(f"{i}. {project['title']}"):

            st.write("**Domain:**", project["domain"])
            st.write("**Skill:**", project["skill"])
            st.write("**Team Size:**", project["team_size"])
            st.write("**Problem:**", project["problem"])