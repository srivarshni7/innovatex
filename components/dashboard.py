import streamlit as st

def show_dashboard():

    st.markdown("""
    <style>
    .hero{
        background: linear-gradient(90deg,#2563EB,#7C3AED);
        padding:35px;
        border-radius:18px;
        color:white;
        text-align:center;
        margin-bottom:20px;
    }

    .card{
        background:white;
        padding:20px;
        border-radius:15px;
        text-align:center;
        box-shadow:0px 3px 12px rgba(0,0,0,.12);
        transition:.3s;
    }

    .card:hover{
        transform:translateY(-5px);
    }

    .feature{
        background:#F8FAFC;
        padding:18px;
        border-radius:15px;
        border-left:6px solid #2563EB;
        margin-top:15px;
    }

    div.stButton>button{
        width:100%;
        border-radius:10px;
        height:50px;
        font-size:18px;
        font-weight:bold;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">
        <h1>🚀 InnovateX</h1>
        <h3>AI Innovation & Hackathon Mentor</h3>
        <p>Transform Ideas into Winning Solutions</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("💡 Ideas", "0")

    with c2:
        st.metric("🏆 Winning Score", "--")

    with c3:
        st.metric("🤖 AI Mentor", "Ready")

    with c4:
        st.metric("📄 Reports", "0")

    st.write("")

    a, b, c, d = st.columns(4)

    with a:
        st.button("💡 Start Evaluation")

    with b:
        st.button("🤖 AI Mentor")

    with c:
        st.button("🛣️ Roadmap")

    with d:
        st.button("📄 PDF Report")

    st.write("")
    st.subheader("✨ Platform Features")

    x, y = st.columns(2)

    with x:
        st.markdown("""
        <div class='feature'>
        <h4>💡 AI Idea Evaluation</h4>
        Analyze innovation, feasibility and impact.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='feature'>
        <h4>🧩 Innovation Gap Analyzer</h4>
        Find missing features and improve your project.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='feature'>
        <h4>🤖 AI Project Mentor</h4>
        Ask project-related questions anytime.
        </div>
        """, unsafe_allow_html=True)

    with y:
        st.markdown("""
        <div class='feature'>
        <h4>🛣️ Roadmap Generator</h4>
        Generate milestones and development plans.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='feature'>
        <h4>📄 PDF Report</h4>
        Download a professional evaluation report.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='feature'>
        <h4>📚 History</h4>
        View and manage previous analyses.
        </div>
        """, unsafe_allow_html=True)