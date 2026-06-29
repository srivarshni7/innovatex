from streamlit_option_menu import option_menu
import streamlit as st

def show_sidebar():
    with st.sidebar:
        st.markdown(
            """
            <h2 style='text-align:center;color:#4F46E5;'>
            🚀 InnovateX
            </h2>
            <p style='text-align:center;color:gray;'>
            AI Innovation & Hackathon Mentor
            </p>
            """,
            unsafe_allow_html=True,
        )

        selected = option_menu(
            menu_title=None,
            options=[
                "Dashboard",
                "Idea Evaluation",
                "Analysis",
                "AI Mentor",
                "Roadmap",
                "PDF Report",
                "History",
                "About",
            ],
            icons=[
                "house-fill",
                "lightbulb-fill",
                "bar-chart-fill",
                "robot",
                "map-fill",
                "file-earmark-pdf-fill",
                "clock-history",
                "info-circle-fill",
            ],
            default_index=0,
        )

    return selected