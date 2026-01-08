# DeepSearch AI (Local LLM Agent with Web Search)

**DeepSearch AI** is a fully local, full-stack conversational agent capable of real-time web search. It runs a quantized **Large Language Model (LLM)** directly on your machine using **Docker**, ensuring privacy and control without relying on external cloud APIs for the core logic.

---

## Video Preview


https://github.com/user-attachments/assets/e35c2b49-c4ab-401d-84a4-0f00b7666ed2



---

## Project Description

This project is a production-ready **Local AI Agent** designed to bridge the gap between offline LLMs and real-time internet data. Built with **FastAPI** and **cpp-python**, the agent intelligently detects when a user needs up-to-date information (e.g., "search iPhone 16 price") and triggers a web search using **DuckDuckGo**. The results are then synthesized by the local **Qwen2.5** model to provide a comprehensive answer.

The project is fully containerized, allowing for a seamless "write once, run anywhere" experience using Docker, while keeping the heavy model files managed locally.

---

## Project Goal

The primary goal of this project is to provide a **private, low-latency, and cost-effective** alternative to cloud-based AI assistants. It is designed for developers and privacy enthusiasts who want to run powerful AI agents on consumer hardware.

Key capabilities include:
*   **Smart Intent Detection:** Automatically switches between "Chat Mode" and "Search Mode" based on user input.
*   **Real-Time Knowledge:** Overcomes the knowledge cutoff of static LLMs by fetching live data from the web.
*   **Local Inference:** Uses 4-bit quantized GGUF models (`Qwen2.5-0.5B`) to run efficiently on CPU/RAM.
*   **Full-Stack Experience:** Provides a clean, dark-mode chat interface built with Vanilla JS, connected to a robust Python backend.

---

## Architecture

The system follows a microservice-like architecture encapsulated within a Docker container:

1.  **Frontend:** Captures user input and handles UI state (Thinking/Searching animations).
2.  **API Layer:** FastAPI receives the request.
3.  **Agent Logic:** Analyzes the prompt to decide if a search tool is needed.
4.  **Tool Execution:** If needed, queries DuckDuckGo (`ddgs`) for live results.
5.  **LLM Inference:** The Context + Query is fed into `llama-cpp-python` running the Qwen model.
6.  **Response:** The final answer is streamed back to the user.

---

## 🛠️ Technologies Used

### AI & Core Logic
*   **LLM Engine:** `llama-cpp-python` (Binding for llama.cpp)
*   **Model:** `Qwen2.5-0.5B-Instruct` (GGUF Format - Quantized)
*   **Web Search Tool:** `duckduckgo-search`
*   **Model Management:** `Hugging Face Hub` (for downloading the GGUF)

### Backend
*   **Framework:** `FastAPI`
*   **Server:** `Uvicorn`
*   **Data Validation:** `Pydantic`

### Frontend
*   **Core:** `HTML5`, `CSS3`, `Vanilla JavaScript`
*   **Styling:** Custom CSS with Dark Mode & Responsive Design

### DevOps & Deployment
*   **Containerization:** `Docker`
*   **Virtualization:** `Docker Volumes` (For mapping local models)

## Libraries Used
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-blue?style=for-the-badge)
![Llama Cpp](https://img.shields.io/badge/Llama_Cpp-black?style=for-the-badge&logo=python&logoColor=white)

---

## 📂 Project Structure

*   **`ai/`**
    *   `main.py` → **Script to download the GGUF model.**
    *   `models/` → Directory where the model file will be stored.
*   **`agent.py`** → Core logic for the AI Agent (Switching between Search/Chat).
*   **`main.py`** → FastAPI application entry point.
*   **`tools.py`** → Implementation of the Internet Search tool.
*   **`index.html`** → The frontend chat interface.
*   **`Dockerfile`** → Configuration for building the application image.
*   **`requirements.txt`** → Python dependencies.

---

## How to Run Locally

Since the AI model file (`.gguf`) is large, it is **NOT** included in the GitHub repository. You must download it manually using the provided script before running the Docker container.

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/DeepSearch-AI.git
cd DeepSearch-AI
```

### 2. Download the Model (Critical Step)
You need to download the `qwen2.5-0.5b-instruct-q4_k_m.gguf` model. I have prepared a script to do this automatically.

First, install the necessary library:
```bash
pip install huggingface_hub
```

Then, run the download script:
```bash
python ai/main.py
```
*This will download the model (~400MB) and place it into the `./ai/models/` directory.*

### 3. Build the Docker Image
```bash
docker build -t ai-agent .
```

### 4. Run the Container
We use Docker Volumes to map the downloaded model into the container. This keeps the image light and allows you to swap models easily.

```bash
docker run -d -p 8000:8000 --name ai-agent \
-v $(pwd)/ai/models:/app/ai/models \
ai-agent
```

### 5. Access the Application
Open your browser and go to:
**http://localhost:8000**

---

## How It Works

1.  **Chat Mode:** If you ask general questions (e.g., "Write a poem"), the Local LLM answers directly.
2.  **Search Mode:** If you start your sentence with keywords like `search`, `ara`, or `bul` (e.g., "search Tesla stock price"), the Agent:
    *   Parses your query.
    *   Searches DuckDuckGo for live results.
    *   Reads the content.
    *   Summarizes the answer using the LLM.

---

## Summary

DeepSearch AI demonstrates how to build a **functional, privacy-focused AI Agent** without relying on paid cloud APIs. By combining **FastAPI** for the backend, **Docker** for deployment, and **GGUF quantization** for performance, it brings the power of modern LLMs to your local machine.
```
