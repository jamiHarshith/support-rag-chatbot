# 📚 RAG Chatbot for Support Documentation

This project implements a Retrieval-Augmented Generation (RAG) chatbot using [LlamaIndex](https://www.llamaindex.ai/) and OpenRouter (for online LLM access). It scrapes support documentation, indexes it, and allows users to ask questions via a web-based chatbot interface.

---

## 🔧 Tech Stack

- **LlamaIndex**: Framework for RAG pipeline
- **OpenRouter**: Free access to powerful LLMs (e.g., OpenAI GPT)
- **Python**: Core scripting and backend logic
- **Streamlit or Gradio (optional)**: UI for the chatbot
- **BeautifulSoup**: Web scraping
- **PyMuPDF / docx**: For PDF & Word file parsing

---

## 📁 File Structure

```bash
.
├── scraper.py          # Scrapes all support pages from the AngelOne website
├── ingest.py           # Loads and parses web pages, PDFs, Word docs into documents
├── settings.py         # Centralized config for models, embedding, storage
├── index_documents.py  # Creates and persists VectorStore index from documents
├── query_handler.py    # Loads index and handles queries
├── app.py              # (Optional) Web UI for chatbot interface
├── storage/            # Folder where indexed data is stored
└── requirements.txt    # All necessary Python packages


⚙️ Setup Instructions
1. 📦 Install Dependencies

pip install -r requirements.txt
Add your OpenRouter API key as an environment variable or inside settings.py:


export OPENROUTER_API_KEY=your-api-key
🚀 Execution Order
Step 1: Scrape Support Website

    python scraper.py
    Scrapes all relevant URLs under https://www.angelone.in/support

Saves HTML or text files locally.

Step 2: Ingest All Sources

    python ingest.py
    Reads scraped web pages, PDFs, and .docx files.

Converts them into a document format suitable for LlamaIndex.

Step 3: Configure Embeddings and LLMs
Edit settings.py to define:

    The embedding model (local or OpenAI/OpenRouter)

    LLM for querying

    ServiceContext & StorageContext

    Chunk size, persist location

    No need to call this file directly. It’s imported where needed.

Step 4: Create the Vector Index

    python index_documents.py
    Uses the documents to create a VectorStoreIndex.

    Embeddings are stored in ./storage/ for persistence.

Step 5: Ask Questions via Terminal

    python query_handler.py
    Loads the persisted index.

Asks a question using the custom prompt.

Responds with relevant answers or “I don’t know” if out of scope.

[Optional] Step 6: Run Web Chatbot

    python app.py
    Launches a web UI using Gradio or Streamlit.

Users can interact with the chatbot easily.

💬 Prompt Template
The system uses a strict template to avoid hallucination:


    You are a helpful assistant answering user questions based on the provided context.

    Context:
    {context_str}

    Question:
    {query_str}

    Answer the question only using the context above.
    If the context does not contain relevant information, say:
    "I don't know based on the provided documentation."
    Do not attempt to make up an answer.

📌 Notes
The index is persisted. No need to recreate unless documents change.

You can plug in any LLM via OpenRouter by changing settings.py.

You can extend to handle image, video, or scanned PDF inputs.