import streamlit as st


def show_idea_evaluation():

    st.title("💡 AI Idea Evaluation")

    st.write("Fill in the details below to evaluate your hackathon idea.")

    # -----------------------------
    # Project Details
    # -----------------------------
    st.subheader("📌 Project Details")

    project_title = st.text_input(
        "Project Title",
        placeholder="Example: AI Smart Garbage Collection System"
    )

    domain = st.selectbox(
        "Project Domain",
        [
            "Smart City",
            "Healthcare",
            "Education",
            "Agriculture",
            "Environment",
            "AI / ML",
            "Cyber Security",
            "FinTech",
            "IoT",
            "Others"
        ]
    )

    description = st.text_area(
        "Project Description",
        height=150
    )

    # -----------------------------
    # Team Details
    # -----------------------------
    st.subheader("👥 Team Details")

    col1, col2 = st.columns(2)

    with col1:
        team_size = st.slider(
            "Number of Team Members",
            1,
            6,
            4
        )

    with col2:
        duration = st.selectbox(
            "Hackathon Duration",
            [
                "24 Hours",
                "36 Hours",
                "48 Hours",
                "More than 48 Hours"
            ]
        )

    skill = st.selectbox(
        "Skill Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    # -----------------------------
    # Technical Details
    # -----------------------------
    st.subheader("💻 Technical Details")

    tech_stack = st.multiselect(
        "Tech Stack",
        [
            "Python",
            "Streamlit",
            "SQL",
            "FastAPI",
            "React",
            "Flutter",
            "Node.js",
            "AI/ML",
            "IoT",
            "MongoDB",
            "Firebase"
        ]
    )

    target_users = st.text_input(
        "Target Users",
        placeholder="Students, Farmers, Hospitals..."
    )

    problem = st.text_area(
        "Problem Statement",
        height=120
    )

    # -----------------------------
    # Analyze Button
    # -----------------------------
    if st.button("🚀 Analyze My Idea"):

        if not project_title or not description or not problem:
            st.error("Please fill all the required fields.")
            return

        # Initialize history if not exists
        if "history" not in st.session_state:
            st.session_state["history"] = []

        project_data = {
            "title": project_title,
            "domain": domain,
            "description": description,
            "team_size": team_size,
            "duration": duration,
            "skill": skill,
            "tech_stack": tech_stack,
            "target_users": target_users,
            "problem": problem
        }

        st.session_state["project"] = project_data
        st.session_state["history"].append(project_data)

        st.success("✅ Project information saved successfully!")
        st.info("Go to Analysis, AI Mentor, or Roadmap to continue 🚀")