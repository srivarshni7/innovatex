# 🚀 InnovateX — AI Innovation & Hackathon Mentor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://innovatex-app.streamlit.app/)

> An AI-powered platform to evaluate, mentor, and guide hackathon project ideas using cutting-edge LLM technology.

---

## 🌐 Live Demo
👉 **[https://innovatex-app.streamlit.app/](https://innovatex-app.streamlit.app/)**

---

## ✨ Features

- 💡 **Idea Evaluation** — AI scores your project on Innovation, Feasibility, and Market Potential
- 🤖 **AI Mentor** — Multi-turn chat assistant for project guidance
- 📊 **Analysis Dashboard** — Visual breakdown of your project scores
- 🗺️ **Roadmap Generator** — Auto-generates an 8-week development plan
- 📄 **PDF Report** — Download a professional AI-generated evaluation report
- 🗂️ **Project History** — Persistent history of all evaluated projects

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| AI Model | Groq API (LLaMA 3) |
| PDF Generation | ReportLab |
| Deployment | Streamlit Community Cloud |
| Version Control | GitHub |

---

## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/srivarshni7/innovatex.git
cd innovatex

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Add your API key
echo GROQ_API_KEY=your_key_here > .env

# Run the app
streamlit run app.py
```

---

## 🔑 Environment Variables

Create a `.env` file in the root folder:

Get your free API key at [console.groq.com](https://console.groq.com)

---

## 📁 Project Structure
InnovateX/

├── components/        # Sidebar, Dashboard components

├── pages/             # App pages (Mentor, Evaluation, History...)

├── utils/             # AI engine, scoring, history manager

├── app.py             # Main entry point

└── requirements.txt   # Dependencies

---

## 👩‍💻 Author

**Srivarshni** — [@srivarshni7](https://github.com/srivarshni7)

---

## 📜 License

This project is licensed under the MIT License.
