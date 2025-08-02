
import streamlit as st
import os
import openai

# Initialize OpenAI client using new SDK (v1.0+)
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Streamlit page setup
st.set_page_config(page_title="Green Hill GPT – Investor Assistant", page_icon="🌿", layout="wide")

# Load logo
st.image("logo.png", width=120)

# Title and intro
st.markdown(
    "<h1 style='color: #1B4332; font-size: 36px;'>Green Hill GPT Investor Assistant</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='font-size: 18px; color: #2E7D32;'>Interact with the 2025 Strategic Plan using this AI assistant. Ask questions about CAPEX, governance, GMP readiness, or investor protections.</p>",
    unsafe_allow_html=True
)

# Sample prompts
example_prompts = [
    "What’s the projected ROI by 2029?",
    "Where is the board control clause in the SHA?",
    "Summarize the CAPEX requirements.",
    "How does freeze-drying benefit the product?",
    "Explain the ZEC tax advantage.",
    "Summarize investor protections in the agreement."
]

selected_prompt = st.selectbox("💡 Choose a suggested question or ask your own:", [""] + example_prompts)

# Style
st.markdown("""
    <style>
    .stButton>button {
        background-color: #1B4332;
        color: white;
        font-weight: bold;
        border-radius: 6px;
        padding: 0.5em 1em;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Question form
with st.form("ghc_form"):
    question = st.text_input("✍️ Type your question below:", value=selected_prompt if selected_prompt else "")
    submitted = st.form_submit_button("Ask GPT")

if submitted and question.strip():
    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are the Green Hill GPT Assistant, trained on the 2025 Strategic Plan for Green Hill Canarias. Provide investor-grade answers with strategic clarity and references where appropriate."},
                    {"role": "user", "content": question}
                ]
            )
            st.markdown("### ✅ Answer")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"An error occurred: {e}")
