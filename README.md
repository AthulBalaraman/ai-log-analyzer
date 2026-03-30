# 🛡️ AI Log Analyzer (Level 1 → Agentic Actions System)

## 🚀 Overview

This project is an **AI-powered log analysis and response system** built using:

* LangChain (latest architecture)
* Google Gemini (LLM)
* FastAPI (backend)

It not only analyzes logs but also **takes automated actions** based on detected threats.

---

## 🧠 What’s New in This Branch

### 🔥 Agent-like Action System (Major Upgrade)

Previously:

* System only analyzed logs

Now:

* System **takes automated actions**
* Implements **severity-based decision making**
* Simulates a **real-world SOC (Security Operations Center)**

---

## ⚙️ Tech Stack

* Python 3.10+
* LangChain
* langchain-google-genai
* FastAPI
* Pydantic
* asyncio (parallel execution)
* Uvicorn

---

## 🏗️ Project Structure

```id="y1c8bm"
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
│   ├── tools/                 # NEW
│   │   └── security_tools.py
│   └── utils/
│       ├── parser.py
│       └── ip_extractor.py    # NEW
│
├── .env
├── requirements.txt
└── README.md
```

---

## 🔄 Application Flow

```id="czb3t3"
Client Request (Multiple Logs)
   ↓
FastAPI Route (/analyze)
   ↓
Parallel Processing (asyncio)
   ↓
LangChain (Prompt → LLM → Parser)
   ↓
Structured Log Analysis
   ↓
Risk Aggregation
   ↓
Action Layer (Tool Execution)
   ↓
Final Response
```

---

## 🧠 How It Works

### 1. Input (Batch Logs)

```json id="9w4n4x"
{
  "logs": [
    "Failed login attempts from IP 192.168.1.10",
    "User attempted SQL injection",
    "Normal API request"
  ]
}
```

---

### 2. Parallel AI Analysis

* Each log processed concurrently
* Uses LangChain pipeline:

  * Prompt → Gemini → Output Parser

---

### 3. Intelligent Classification

For each log:

* Detects log type (authentication, database, etc.)
* Identifies attack type (brute force, SQL injection, etc.)
* Assigns risk level & confidence score

---

### 4. Aggregation

System computes:

* Overall risk (High / Medium / Low)
* Average confidence
* Total logs analyzed

---

### 5. 🔥 Action Layer (NEW)

Based on severity:

#### 🔴 High Risk

* Block IP
* Alert Admin
* Log Incident

#### 🟡 Medium Risk

* Alert Admin
* Log Incident

#### 🟢 Low Risk

* Log Incident only

---

### 6. Final Output

```json id="9a0a3g"
{
  "overall_risk": "High",
  "average_confidence": 87.5,
  "total_logs": 2,
  "analysis": [...],
  "actions_taken": [
    "Blocked IP 192.168.1.10",
    "Admin alerted: Multiple failed login attempts detected",
    "Incident logged: Repeated login failures"
  ]
}
```

---

## 🛠️ Tools Implemented

* **block_ip(ip)** → Simulates blocking malicious IP
* **alert_admin(message)** → Simulates alerting system admin
* **log_incident(details)** → Logs security events

---

## ▶️ Setup Instructions

### 1. Create virtual environment

```bash id="lzzx1t"
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

---

### 2. Install dependencies

```bash id="b7b5gl"
pip install -r requirements.txt
```

---

### 3. Add environment variables

```env id="kqk7s0"
GOOGLE_API_KEY=your_api_key_here
```

---

### 4. Run application

```bash id="y3t0gl"
uvicorn app.main:app --reload
```

---

### 5. Test API

Open:

```id="xk7pr1"
http://127.0.0.1:8000/docs
```

---

## 📌 Key Features

### ✅ Batch Log Processing

* Handles multiple logs in one request

### ✅ Parallel Execution

* Fast processing using asyncio

### ✅ Fault Tolerance

* Prevents full system failure

### ✅ Structured Output

* Reliable JSON responses

### ✅ Context-Aware AI

* Log classification + attack detection

### ✅ 🔥 Agent-like Actions (NEW)

* Automated response system
* Severity-based decisions

---

## 📌 Key Learning Outcomes

* Building AI-powered backend systems
* Async programming and concurrency
* Prompt engineering for structured outputs
* Designing fault-tolerant systems
* Implementing action-based AI workflows

---

## ⚠️ Challenges Solved

* ❌ Slow processing → solved with parallel execution
* ❌ Inconsistent outputs → solved with structured parsing
* ❌ Passive system → solved with action layer

---

## 🚀 What’s Next (Important)

### 🔥 Next Upgrade: True Agent System

Current system:

* Uses **rule-based actions** (if-else)

Next:

* Use **LangChain Agent**
* AI will:

  * Decide **which tool to use**
  * Choose **when to act**
  * Execute tools dynamically

---

### 🧠 Upcoming Features

* Dynamic tool selection (LLM decides actions)
* Multi-agent architecture (planner + executor)
* Vector DB (RAG for historical logs)
* Real-time log streaming (WebSockets)
* Integration with real systems (firewall / email / DB)

---

## 💡 Author Notes

This project is being developed as a **step-by-step journey into Agentic AI systems**.

Each branch represents:

* A clear architectural improvement
* A real-world capability
* A production-ready concept

---

## 🎯 Final Vision

> Build a fully autonomous AI-powered cybersecurity system that:

* Detects threats
* Understands context
* Takes actions
* Learns from past data

---
