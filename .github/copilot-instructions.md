# Copilot Instructions for AI Coding Agents

## Project Overview
This project is a Retrieval-Augmented Generation (RAG) chatbot designed to assist FILKOM students with their thesis guidance. The chatbot answers questions strictly based on the provided thesis guide documents, primarily `PanduanSkripsiFilkom-v3.0.pdf` in the `data/` directory.

## Key Components
- `rag_utils.py`: Contains core RAG logic, including document loading, vector store creation, and chain construction using LangChain and Google Generative AI.
- `app.py`: Intended as the main entry point for the application (currently empty; implement CLI or web server here).
- `data/`: Stores source documents for retrieval (PDFs, Markdown).

## Critical Workflows
- **Document Loading**: Only files in `data/` with `.pdf` or `.md` extensions are loaded. Use `PyPDFLoader` for PDFs and `TextLoader` for Markdown.
- **Vector Store**: Uses Chroma for vector storage. Embeddings are generated via Google Generative AI (`gemini-embedding-001`).
- **RAG Chain**: Retrieval is limited to top 4 relevant chunks. Answers must be concise, clear, and strictly based on the guide. If the question is out of scope, the bot must say "tidak tahu" and suggest consulting a supervisor.
- **API Key**: The Google API key is hardcoded in `rag_utils.py` as `GOOGLE_API_KEY`. Replace with a valid key before running.

## Developer Patterns & Conventions
- All retrieval and answering logic is centralized in `rag_utils.py`.
- System prompt enforces strict adherence to the guide document; do not hallucinate or answer outside its scope.
- Use chunk size 800 and overlap 150 for text splitting.
- Persist vector store in `.chroma` directory.

## Integration Points
- Relies on LangChain, Chroma, and Google Generative AI (Gemini) libraries. Ensure these are installed and compatible.
- Extend `app.py` for CLI, API, or web integration as needed.

## Example Usage
```python
from rag_utils import load_docs, build_vectorstore, build_rag_chain

docs = load_docs()
vs = build_vectorstore(docs)
chain, retriever = build_rag_chain(vs)
```

## Testing & Debugging
- No test framework or scripts are present; add tests for document loading and chain responses as needed.
- For debugging, print intermediate results (e.g., loaded docs, vector store contents).

## External Dependencies
- langchain_community
- langchain_google_genai
- chromadb

## Next Steps
- Implement main logic in `app.py` (CLI, API, or web server).
- Add tests and expand `requirements.txt` as dependencies are finalized.

---
**Update this file as project structure or conventions evolve.**
