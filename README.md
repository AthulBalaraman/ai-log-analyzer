# 🛡️ AI Log Analyzer (Level 1 → Structured Output)

## 🚀 Overview

This project is an **AI-powered log analysis system** built using:

* LangChain (latest architecture)
* Google Gemini (LLM)
* FastAPI (backend)

It analyzes system logs and returns:

* Summary of events
* Suspicious activity detection
* Risk level classification
* Suggested actions

---

## 🧠 What’s New in This Branch

### ✅ Structured Output Parsing (Major Upgrade)

Previously, the model returned **raw text or inconsistent JSON**.

Now:

* Enforced **strict JSON output**
* Used **Pydantic schema validation**
* Integrated **LangChain Output Parser**

👉 Result:

* Reliable API responses
* No broken JSON
* Production-ready AI output

---

## ⚙️ Tech Stack

* Python 3.10+
* LangChain (latest modular syntax)
* langchain-google-genai
* FastAPI
* Pydantic
* Uvicorn

---

## 🏗️ Project Structure

```
ai-log-analyzer/
│
├── app/
│   ├── main.py
│   ├── core/
│   │   └── config.py
│   ├── api/
│   │   └── routes/
│   │       └── analyze.py
│   ├── services/
│   │   └── ai_service.py
│   ├── prompts/
│   │   └── log_prompt.py
│   ├── schemas/
│   │   └── log_schema.py
│   └── utils/
│       └── parser.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## 🔄 Application Flow

```
Client Request
   ↓
FastAPI Route (/analyze)
   ↓
Service Layer (LangChain)
   ↓
Prompt Template
   ↓
Gemini LLM
   ↓
Pydantic Output Parser
   ↓
Structured JSON Response
```

---

## 🧠 How It Works

### 1. Input

User sends logs via POST request:

```json
{
  "logs": "Multiple failed login attempts from IP 45.33.21.1"
}
```

---

### 2. Prompt Processing

LangChain formats input using:

* ChatPromptTemplate
* Dynamic format instructions from parser

---

### 3. LLM Analysis

Gemini analyzes:

* Patterns
* Security risks
* Suspicious behavior

---

### 4. Output Parsing (NEW)

* Response is passed through **PydanticOutputParser**
* Ensures strict schema validation

---

### 5. Final Response

```json
{
  "summary": "Multiple failed login attempts detected",
  "suspicious_activity": "Possible brute force attack",
  "risk_level": "High",
  "suggested_action": "Block IP and enable rate limiting"
}
```

---

## ▶️ Setup Instructions

### 1. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Add environment variables

Create `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

---

### 4. Run the application

```bash
uvicorn app.main:app --reload
```

---

### 5. Test API

Open:

```
http://127.0.0.1:8000/docs
```

Use `/analyze` endpoint (POST)

---

## 🧪 Example Request

```json
{
  "logs": "User attempted login 10 times within 5 seconds from IP 192.168.1.1"
}
```

---

## 📌 Key Learning Outcomes

* LangChain latest architecture (`prompt | llm | parser`)
* Structured output using Pydantic
* Reliable LLM responses
* FastAPI integration with AI services

---

## ⚠️ Challenges Solved

* ❌ Inconsistent LLM output
* ❌ Broken JSON responses
* ❌ Manual parsing issues

✔️ Solved using structured output parsing

---


## 💡 Author Notes

This project is being built incrementally with:

* Clean architecture
* Version-controlled feature branches
* Production-ready practices

Each branch represents a **learning milestone in Agentic AI Development**

---
