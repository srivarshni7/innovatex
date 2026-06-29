import re
import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

from utils.ai_engine import get_ai_report, get_ai_scores, get_ai_roadmap
import json


def clean_for_pdf(text):
    # Remove markdown headers
    text = re.sub(r'#{1,6}\s*', '', text)
    # Remove bold/italic markers
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    # Remove horizontal rules
    text = re.sub(r'---+', '', text)
    # Remove table rows (lines with pipes)
    text = re.sub(r'\|.*', '', text)
    # Replace unicode stars/bullets with dash
    text = re.sub(r'[★☆✓•·]', '-', text)
    # Remove non-ASCII characters to avoid ReportLab crashes
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    # Split into lines, strip whitespace, drop empty lines
    lines = [line.strip() for line in text.split('\n')]
    lines = [line for line in lines if line]
    return lines


def show_pdf_report():

    st.title("📄 AI PDF Report Generator")

    if "project" not in st.session_state:
        st.warning("⚠️ Please evaluate a project first.")
        return

    project = st.session_state["project"]

    if st.button("📥 Generate AI Report PDF"):

        # ---------------- AI DATA ----------------
        with st.spinner("Generating AI report..."):
            raw_scores = get_ai_scores(project)

            try:
                scores = json.loads(raw_scores[raw_scores.find("{"):raw_scores.rfind("}") + 1])
            except Exception:
                st.error("Score parsing failed")
                return

            roadmap = get_ai_roadmap(project)
            report_text = get_ai_report(project, scores, roadmap)

        # ---------------- PDF CREATION ----------------
        file_name = "InnovateX_AI_Report.pdf"
        doc = SimpleDocTemplate(file_name, pagesize=A4)
        styles = getSampleStyleSheet()

        story = []

        story.append(Paragraph("InnovateX AI Report", styles["Title"]))
        story.append(Spacer(1, 12))

        story.append(Paragraph(f"<b>Title:</b> {project['title']}", styles["Normal"]))
        story.append(Paragraph(f"<b>Domain:</b> {project['domain']}", styles["Normal"]))
        story.append(Spacer(1, 12))

        story.append(Paragraph("<b>AI Generated Report:</b>", styles["Heading2"]))
        story.append(Spacer(1, 8))

        # Add each cleaned line as its own Paragraph
        for line in clean_for_pdf(report_text):
            try:
                story.append(Paragraph(line, styles["Normal"]))
                story.append(Spacer(1, 4))
            except Exception:
                # Last resort: strip everything except basic ASCII
                safe = re.sub(r'[^\x20-\x7E]', '', line)
                if safe:
                    story.append(Paragraph(safe, styles["Normal"]))
                    story.append(Spacer(1, 4))

        doc.build(story)

        with open(file_name, "rb") as f:
            st.download_button(
                "⬇️ Download AI Report PDF",
                f,
                file_name="InnovateX_AI_Report.pdf",
                mime="application/pdf"
            )

        st.success("✅ AI PDF Report Generated!")