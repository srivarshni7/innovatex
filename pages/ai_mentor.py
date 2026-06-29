import streamlit as st
from utils.ai_engine import get_ai_mentor_response


def show_ai_mentor():
    st.title("🤖 AI Mentor")

    # Initialize chat history in session
    if "mentor_messages" not in st.session_state:
        st.session_state.mentor_messages = []

    # Display full chat history
    for msg in st.session_state.mentor_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input at bottom
    user_input = st.chat_input("Ask your AI Mentor anything...")

    if user_input:
        # Show user message
        with st.chat_message("user"):
            st.markdown(user_input)

        # Add to history
        st.session_state.mentor_messages.append({
            "role": "user",
            "content": user_input
        })

        # Get AI response with full history
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                reply = get_ai_mentor_response(st.session_state.mentor_messages)
            st.markdown(reply)

        # Save assistant reply to history
        st.session_state.mentor_messages.append({
            "role": "assistant",
            "content": reply
        })

    # Button to clear chat
    if st.session_state.mentor_messages:
        if st.button("🗑️ Clear Chat"):
            st.session_state.mentor_messages = []
            st.rerun()