import streamlit as st
from rag_utils import ask_bot

st.set_page_config(page_title="Chatbot Panduan Skripsi", layout="wide")

st.title("📚 Chatbot Panduan Skripsi")
st.markdown("Tanyakan apapun terkait **pengajuan penelitian, daftar sidang, yudisium, dan syarat-syaratnya**. "
            "Chatbot ini bisa mengingat percakapan sebelumnya.")

# Simpan history percakapan di Streamlit session_state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

query = st.text_input("Masukkan pertanyaan Anda:")

if st.button("Tanya"):
    if query.strip() != "":
        with st.spinner("Sedang mencari jawaban..."):
            answer = ask_bot(query)

        # Simpan ke history
        st.session_state.chat_history.append(("Anda", query))
        st.session_state.chat_history.append(("Chatbot", answer))

# Tampilkan percakapan
for speaker, message in st.session_state.chat_history:
    if speaker == "Anda":
        st.markdown(f"**🧑 {speaker}:** {message}")
    else:
        st.markdown(f"**🤖 {speaker}:** {message}")
