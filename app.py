import streamlit as st
from vqa_engine import VisionLLM

st.set_page_config(page_title="Multimodal Vision LLM", layout="wide")
st.title("👁️ Multimodal Vision LLM & Visual Q&A System")
st.caption("Visual reasoning, document VQA, and image understanding powered by Qwen2-VL & CLIP.")

uploaded_img = st.file_uploader("Upload Image or Document", type=['png', 'jpg', 'pdf'])
prompt = st.text_input("Ask anything about the visual content:")

if uploaded_img and prompt:
    vllm = VisionLLM()
    res = vllm.process_vqa("uploaded_file", prompt)
    st.info(res)
