import streamlit as st
from google import genai

# -------------------- Page Config --------------------
st.set_page_config(
    page_title="NayePankh AI Career Assistant",
    page_icon="🕊️"
)

st.title("🤖 NayePankh AI Career Assistant")

# -------------------- Gemini Client --------------------
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# -------------------- Memory --------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------- Show Previous Messages --------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------- User Input --------------------
prompt = st.chat_input("Ask anything...")

if prompt:

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Create conversation history
    history = ""

    for msg in st.session_state.messages:
        history += f"{msg['role']}: {msg['content']}\n"

    # Generate response
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"""
You are an AI Career Assistant for NayePankh Foundation.

Conversation history:
{history}

Answer clearly and professionally.
"""
        )

        answer = response.text

    except Exception as e:
        answer = f"⚠️ Error:\n\n{e}"

    # Show assistant response
    with st.chat_message("assistant"):
        st.markdown(answer)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
