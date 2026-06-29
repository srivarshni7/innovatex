import streamlit as st

from components.sidebar import show_sidebar
from components.dashboard import show_dashboard
from pages.idea_evaluation import show_idea_evaluation
from pages.analysis import show_analysis
from pages.ai_mentor import show_ai_mentor
from pages.pdf_report import show_pdf_report
from pages.roadmap import show_roadmap
from pages.pdf_report import show_pdf_report
from pages.history import show_history

st.set_page_config(
    page_title="InnovateX",
    page_icon="🚀",
    layout="wide"
)

selected = show_sidebar()

if selected == "Dashboard":
    show_dashboard()

elif selected == "Idea Evaluation":
    show_idea_evaluation()

elif selected == "Analysis":
    show_analysis()

elif selected == "AI Mentor":
    show_ai_mentor()

elif selected == "Roadmap":
    show_roadmap()


elif selected == "PDF Report":
    show_pdf_report()

elif selected == "History":
    show_history()

elif selected == "About":
    st.title("ℹ️ About")
    st.write("InnovateX - AI Innovation & Hackathon Mentor")