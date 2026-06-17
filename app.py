import streamlit as st
from google import genai

# Gemini Client
client = genai.Client(
    api_key=st.secrets"AQ.Ab8RN6L0XTacQTvfuJS6txgUo3J5kNA7Vbrq2BIP74lGkli1Aw"
)

st.set_page_config(page_title="NayePankh AI Career Assistant")

st.title("🤖 NayePankh AI Career Assistant")

# Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
     
# User input
prompt = st.chat_input("Ask anything...")

if prompt:

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Create conversation history
    history = ""

    for msg in st.session_state.messages:
        history += f"{msg['role']}: {msg['content']}\n"

    # Generate response
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
You are an AI Career Assistant for NayePankh Foundation.

Conversation history:
{history}

Answer clearly and professionally.
"""
    )

    answer = response.text

    # Show assistant response
    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
