import streamlit as st
from model import multi_agent_chatbot

# -----------------------------
# TITLE
# -----------------------------
st.set_page_config(page_title="AI Symptom Analyzer", layout="centered")

st.title("🧠 AI Symptom Analyzer")
st.write("Describe your symptoms and get possible conditions.")

# -----------------------------
# CHAT MEMORY
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# INPUT BOX (CHAT STYLE)
# -----------------------------
user_input = st.chat_input("Type your symptoms...")

# -----------------------------
# HANDLE INPUT
# -----------------------------
if user_input:
    # Store user message
    st.session_state.messages.append(("user", user_input))

    # 👉 CALL YOUR BACKEND FUNCTION HERE
    response = multi_agent_chatbot(user_input)

    # Store bot response
    st.session_state.messages.append(("bot", response))

# -----------------------------
# DISPLAY CHAT
# -----------------------------
for role, msg in st.session_state.messages:
    if role == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)

# -----------------------------
# SIDEBAR INFO
# -----------------------------
st.sidebar.title("ℹ️ About")
st.sidebar.write("""
This AI Symptom Analyzer uses:
- NLP (TF-IDF)
- Machine Learning
- Multi-agent architecture

⚠️ Not a real medical diagnosis
""")