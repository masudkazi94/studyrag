# studyrag# 📚 StudyPal – RAG Study Assistant

An AI-powered study assistant that helps students understand their study material through conversational AI. Built using **Retrieval-Augmented Generation (RAG)**, StudyPal allows students to ask questions from their textbooks and chapter-specific PDFs and receive context-aware answers, along with relevant YouTube video recommendations.

---

## 🚀 Overview

StudyPal combines document processing, semantic search, vector databases, and Large Language Models (LLMs) to create an interactive learning experience.

Instead of relying only on the general knowledge of an AI model, the application retrieves relevant information from the selected study material and uses it to generate answers.

Students can select a subject and chapter, ask questions in natural language, and explore additional learning resources through YouTube.

## ✨ Features

- **📖 Subject & Chapter Selection** – Select a subject and specific chapter to study.
- **💬 AI-Powered Question Answering** – Ask questions in natural language and receive contextual responses.
- **🔎 Retrieval-Augmented Generation (RAG)** – Retrieves relevant textbook content before generating answers.
- **🧠 Semantic Search** – Uses vector embeddings to retrieve information based on meaning rather than exact keyword matches.
- **📚 Vector Database** – Stores document embeddings using ChromaDB for efficient retrieval.
- **🔗 YouTube Learning Resources** – Provides relevant video recommendations to supplement learning.
- **🗂️ Chapter-Level Knowledge Retrieval** – Supports chapter-specific vector databases for focused learning.
- **💭 Conversational Memory** – Maintains conversation context during a study session.
- **🖥️ Interactive Web Interface** – Built with Streamlit for a simple and user-friendly experience.

---

## 🏗️ Architecture

```text
                 ┌──────────────────────────┐
                 │       StudyPal UI        │
                 │       (Streamlit)        │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │ Subject & Chapter Select │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │       User Question      │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │    Chroma Vector DB      │
                 │  Semantic Retrieval /    │
                 │       MMR Search        │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │ Retrieved Study Context │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │       Groq LLM           │
                 │  Contextual Answering    │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │   AI Answer + YouTube    │
                 │     Recommendations      │
                 └──────────────────────────┘
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application and user interface |
| LangChain | RAG pipeline and LLM orchestration |
| ChromaDB | Persistent vector database |
| HuggingFace | Text embedding generation |
| Sentence Transformers | Semantic embeddings |
| Groq API | LLM inference |
| YouTube Search | Finding supplementary video resources |
| python-dotenv | Environment variable management |

---

## ⚙️ How It Works

### 1. Document Processing

Study material is loaded from PDF documents using document loaders.

### 2. Text Chunking

Documents are split into smaller chunks using text-splitting techniques to make retrieval more effective.

### 3. Embedding Generation

HuggingFace embedding models convert text chunks into numerical vector representations.

### 4. Vector Storage

The generated embeddings are stored in ChromaDB, allowing the application to retrieve relevant information based on semantic similarity.

### 5. Retrieval

When a student asks a question, the application searches the selected vector database and retrieves relevant chunks using Maximum Marginal Relevance (MMR) retrieval.

### 6. Answer Generation

The retrieved context is passed to the LLM through a LangChain conversational retrieval chain. The model uses the retrieved information to generate a context-aware response.

### 7. Learning Resources

The application can also search for relevant YouTube videos to help students explore a topic further.

---

## 📂 Project Structure

```text
StudyPal/
│
├── src/
│   ├── main.py
│   ├── vectorize_book.py
│   ├── vectorize_script.py
│   ├── chatbot_utility.py
│   └── get_yt_video.py
│
├── data/                       # Study PDFs (not tracked by Git)
│
├── vector_db/                  # Persistent book-level vector DB
│
├── chapters_vector_db/          # Chapter-level vector DBs
│
├── requirements.txt
├── .env                        # API keys (not tracked by Git)
├── .gitignore
└── README.md
```

*Note: The exact folder structure and filenames may evolve as the project develops.*

---

## 🔧 Installation & Setup

### Prerequisites

- Python 3.10+
- Git
- Groq API key
- Study material in PDF format

### 1. Clone the repository

```bash
git clone https://github.com/masudkazi94/studyrag.git
```

```bash
cd studyrag
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

```cmd
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your actual API key.

> ⚠️ Never commit your `.env` file or expose your API keys publicly.

---

## 📚 Adding Study Material

Place your PDF study materials inside the appropriate directories under the project's `data/` folder.

Example:

```text
data/
├── class_11/
│   ├── Biology/
│   └── Physics/
│
└── class_12/
    ├── Biology/
    ├── Physics/
    └── Chemistry/
```

The actual directory and file naming conventions should match the paths expected by the vectorization scripts.

---

## 🧮 Generating Vector Databases

Before launching the application, process the study material and generate the vector databases.

Run the vectorization scripts from the project environment according to the configured paths and subjects.

Example:

```bash
python src/vectorize_book.py
```

```bash
python src/vectorize_script.py
```

The vectorization process loads the documents, splits the text, generates embeddings, and stores them in persistent ChromaDB directories.

> Vector databases need to be generated before querying the corresponding study material.

---

## ▶️ Running the Application

Once the dependencies are installed and the vector databases are prepared, launch the Streamlit application:

```bash
streamlit run src/main.py
```

Streamlit will provide a local URL, typically:

```text
http://localhost:8501
```

Open the URL in your browser to start using StudyPal.

---

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | API key used to access the Groq LLM service |

Keep credentials private and store them in your local `.env` file.

---

## 🧠 RAG Pipeline

The project follows a Retrieval-Augmented Generation workflow:

```text
PDF Documents
     │
     ▼
Document Loading
     │
     ▼
Text Splitting
     │
     ▼
HuggingFace Embeddings
     │
     ▼
ChromaDB Vector Storage
     │
     ▼
User Query
     │
     ▼
Semantic Retrieval (MMR)
     │
     ▼
Retrieved Context
     │
     ▼
Conversational LLM
     │
     ▼
Context-Aware Response
```

---

## 🎯 Project Objectives

- Explore practical implementation of Retrieval-Augmented Generation.
- Build a document-based conversational AI application.
- Understand embeddings, semantic search, and vector databases.
- Integrate LLMs with external knowledge sources.
- Develop an end-to-end AI application using Python.
- Create an interactive learning tool for students.

---

## 🔮 Future Improvements

- [ ] Support additional subjects and educational levels.
- [ ] Improve PDF parsing for complex layouts, tables, and scanned documents.
- [ ] Add source citations to generated answers.
- [ ] Add quiz and flashcard generation.
- [ ] Improve chat history management.
- [ ] Deploy the application to a cloud platform.
- [ ] Optimize retrieval quality and response performance.
- [ ] Improve UI/UX and mobile responsiveness.

---

## 👨‍💻 Author

**Masud Kazi**

GitHub: [@masudkazi94](https://github.com/masudkazi94)

---

## 📄 License

This project is intended for educational and learning purposes.
