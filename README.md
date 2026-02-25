# AI-Based Root Cause Analysis (RCA) using AWS Bedrock & RAG

## 📌 Project Overview

This project implements an **AI-powered Root Cause Analysis (RCA) system** that analyzes application/system logs and generates **human-readable explanations** for issues using **Retrieval-Augmented Generation (RAG)** combined with **AWS Bedrock Large Language Models (LLMs)**.

The system helps engineers and support teams quickly understand failures, authentication issues, performance bottlenecks, and recurring errors without manual log inspection.

---

## 🚀 Phase-4 Enhancements (Current Phase)
✅ AWS Bedrock LLM integrated (Free-tier compatible model)  
✅ RAG (Vector Search + Context Retrieval) implemented  
✅ AI-generated Root Cause Explanation from logs  
✅ Streamlit-based interactive UI  
✅ RCA report downloadable as **PDF**  
✅ Git version-controlled and production-ready  

---

## 🧠 Architecture Overview
Logs → Chunking → Embeddings → FAISS Vector Store
↓
Relevant Context
↓
AWS Bedrock LLM
↓
AI Root Cause Explanation


---

## 🛠️ Tech Stack
| Component | Technology |
Frontend | Streamlit |
Backend | Python |
LLM | AWS Bedrock (NVIDIA Nemotron Nano – Free model) |
Embeddings | Sentence-Transformers |
Vector DB | FAISS |
Cloud | AWS |
Version Control | Git & GitHub

## 📂 Project Structure
AI-RCA-Bedrock-RAG-phase-4/
│
├── app.py # Streamlit main app
├── llm/
│ └── bedrock_llm.py # AWS Bedrock LLM wrapper
├── rag/
│ ├── chunker.py # Log chunking
│ ├── loader.py # Log loader
│ ├── retriever.py # Context retrieval
│ └── vector_store.py # FAISS vector store
├── rca/
│ └── rca_engine.py # RCA logic
├── data/
│ ├── logs.txt # Sample logs
│ └── vectors/ # FAISS index files
├── test_phase4_rca.py # Phase-4 test script
├── bedrock_free_test.py # Bedrock connectivity test
├── requirements.txt
└── README.md

## ⚙️ Setup Instructions

```bash
### 1️⃣ Clone Repository
git clone https://github.com/SangeethaGowda14/AI-RCA-Bedrock-RAG-phase-4.git
cd AI-RCA-Bedrock-RAG-phase-4

### 2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Configure AWS Credentials
aws configure

Provide:
AWS Access Key
AWS Secret Key
Region: us-east-1

⚠️ Ensure AWS Bedrock access is enabled in your account.

### ▶️ Run the Application
streamlit run app.py

Open browser:
http://localhost:8501

### 🧪 Example Use Case
Input: Authentication failure logs
Output: Clear RCA explanation, Possible causes,  Preventive suggestions, Downloadable PDF report

###📄 Features Demonstrated
✔ AI-powered reasoning
✔ Cloud-based LLM integration
✔ Real-time RCA
✔ Scalable RAG architecture
✔ Industry-ready design

###🎓 Academic & Internship Relevance
Suitable for VTU Major Project
Internship-grade implementation
Demonstrates real-world AIOps / SRE use case
Uses production cloud services

### 🔒 Security Note
No API keys are hardcoded
AWS credentials handled securely via CLI configuration

### 👩‍💻 Author
Sangeetha VL

Information Science Engineering

AI & Cloud Intern

### 📌 Future Enhancements
Multi-log source support
Severity-based RCA classification
Dashboard analytics
Deployment on AWS EC2 / ECS
