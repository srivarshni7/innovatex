import streamlit as st
from utils.ai_engine import get_ai_scores
import json


def show_analysis():

    st.title("📊 AI Evaluation Report")

    if "project" not in st.session_state:
        st.warning("⚠️ Please evaluate a project first.")
        return

    project = st.session_state["project"]

    # -----------------------------
    # AI SCORES (REAL AI)
    # -----------------------------
    raw = get_ai_scores(project)

    try:
        start = raw.find("{")
        end = raw.rfind("}") + 1
        clean_json = raw[start:end]

        scores = json.loads(clean_json)

    except Exception:
        st.error("⚠️ AI returned invalid format. Please try again.")
        st.stop()

    # -----------------------------
    # PROJECT SUMMARY
    # -----------------------------
    st.subheader("📌 Project Summary")

    st.write("**Project Title:**", project["title"])
    st.write("**Domain:**", project["domain"])
    st.write("**Team Size:**", project["team_size"])
    st.write("**Skill Level:**", project["skill"])

    if project["tech_stack"]:
        st.write("**Tech Stack:**", ", ".join(project["tech_stack"]))
    else:
        st.write("**Tech Stack:** Not specified")

    st.divider()

    # -----------------------------
    # AI EVALUATION
    # -----------------------------
    st.subheader("🤖 AI Evaluation")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("💡 Innovation", f"{scores['innovation']}/100")
        st.metric("📈 Market Potential", f"{scores['market']}/100")

    with col2:
        st.metric("⚙️ Feasibility", f"{scores['feasibility']}/100")
        st.metric("🏆 Overall Score", f"{scores['overall']}/100")

    st.divider()

    # -----------------------------
    # STATIC INSIGHTS (for now)
    # -----------------------------
    st.subheader("✅ Strengths")

    st.success("""
• AI-generated evaluation based on your idea

• Identifies real-world potential

• Assesses technical feasibility
""")

    st.subheader("⚠️ Suggestions")

    st.info("""
• Improve problem explanation

• Add implementation timeline

• Define scalability plan
""")