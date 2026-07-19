import os
import streamlit as st

from app import ask_construction_ai
from rag.vector_store import ingest_pdf


# ============================================
# Page Configuration
# ============================================

st.set_page_config(
    page_title="Construction AI Assistant",
    page_icon="🏗️",
    layout="wide"
)


# ============================================
# Title
# ============================================

st.title("🏗️ Construction AI Assistant")

st.write(
    "Ask construction-related questions, perform calculations, and query uploaded project documents."
)


# ============================================
# Sidebar
# ============================================

with st.sidebar:

    st.header("📂 Project Documents")

    UPLOAD_DIR = "uploads"
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    uploaded_file = st.file_uploader(
        "Upload Construction PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        file_path = os.path.join(
            UPLOAD_DIR,
            uploaded_file.name
        )

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Processing PDF..."):

            total_chunks = ingest_pdf(file_path)

        st.success(
            f"✅ PDF processed successfully!\n\nCreated {total_chunks} chunks."
        )

    st.divider()

    st.header("ℹ️ About")

    st.write("""
    **Construction AI Assistant**

    Features

    - 🤖 Groq LLM
    - 📚 RAG
    - 🏗️ LangGraph
    - 🛠️ Tool Calling
    - 📄 PDF Upload
    """)


# ============================================
# Ask Question
# ============================================

st.subheader("💬 Ask a Question")

question = st.text_area(
    "Enter your question",
    height=120,
    placeholder="Example: Calculate concrete volume for a slab measuring 10m × 5m × 0.2m"
)

ask_button = st.button(
    "🚀 Ask AI",
    use_container_width=True
)


result = None


# ============================================
# AI Processing
# ============================================

if ask_button:

    if question.strip() == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner("🤖 Thinking..."):

            result = ask_construction_ai(question)


# ============================================
# Display Result
# ============================================

if result:

    # -------------------------
    # AI Response
    # -------------------------

    st.subheader("🤖 AI Response")

    st.markdown(result["answer"])

    # -------------------------
    # Planner Decision
    # -------------------------

    st.subheader("🧠 Planner Decision")

    st.info(result["route"])

    # -------------------------
    # Tool Used
    # -------------------------

    if result["tool_name"]:

        st.subheader("🛠 Selected Tool")

        st.success(result["tool_name"])

    # -------------------------
    # Retrieved Context
    # -------------------------

    if result["retrieved_documents"]:

        st.subheader("📚 Retrieved Context")

        for index, doc in enumerate(result["retrieved_documents"], start=1):

            with st.expander(f"Document Chunk {index}"):

                try:
                    st.write(doc.page_content)
                except AttributeError:
                    st.write(doc)