# 🛡️ AI Log Analyzer (Level 2 → Agentic AI System)

## 🚀 Overview

This project is an **autonomous AI-powered log analysis and response system** built using:

* LangChain (latest architecture)
* Google Gemini (LLM)
* FastAPI (backend)
* **LangChain Agents (Dynamic Tool Calling)**

It not only analyzes logs but also **dynamically decides and executes security actions** using an LLM-based agent.

---

## 🧠 What’s New in This Upgrade

### 🔥 Agentic AI System (Major Upgrade)

Previously:
* System used **rule-based logic (if-else)** to take actions.

Now:
* System uses a **True Agentic Architecture**.
* The LLM **dynamically decides** which tools to call and when.
* Implements **autonomous decision-making** based on security context.

---

## ⚙️ Tech Stack

* Python 3.10+
* LangChain (v0.3+)
* langchain-google-genai
* FastAPI
* Pydantic
* asyncio (parallel execution)
* Uvicorn

---

## 🏗️ Project Structure

```text
ai-log-analyzer/
│
├── app/
│   ├── main.py
│   ├── core/
│   │   └── config.py
│   ├── api/
│   │   └── routes/
│   │       └── analyze.py
│   ├── agents/                # NEW: Agent Logic
│   │   └── security_agent.py
│   ├── services/
│   │   └── ai_service.py
│   ├── prompts/
│   │   └── log_prompt.py
│   ├── schemas/
│   │   └── log_schema.py
│   ├── tools/
│   │   └── security_tools.py
│   └── utils/
│       ├── parser.py
│       └── ip_extractor.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## 🔄 Application Flow

```text
Client Request (Multiple Logs)
   ↓
FastAPI Route (/analyze)
   ↓
Parallel Analysis (asyncio)
   ↓
LLM Log Classification (Structured Output)
   ↓
Risk Aggregation
   ↓
🚀 LLM Agent (security_agent)
   ↓
Dynamic Tool Selection (Decision Layer)
   ↓
Execution (block_ip, alert_admin, log_incident)
   ↓
Final Response (Analysis + Agent Summary)
```

---

## 🧠 How It Works

### 1. Input (Batch Logs)
The system accepts a list of raw log strings via a POST request.

### 2. Parallel AI Analysis
Each log is analyzed concurrently to identify the log type, attack pattern, and risk level using a structured Pydantic parser.

### 3. 🔥 Agentic Decision Layer (NEW)
Instead of hardcoded rules, the system now passes the analysis results to a **LangChain Agent**.

The agent is equipped with:
* **Tools:** `block_ip`, `alert_admin`, `log_incident`.
* **System Prompt:** Instructs the agent to act as a cybersecurity expert.
* **Reasoning:** The agent analyzes the risk level and context to decide the best course of action.

### 4. Dynamic Execution
The agent calls the necessary tools. For example:
* If a **Brute Force** attack is detected, the agent autonomously decides to call `block_ip`, `alert_admin`, and `log_incident`.
* If it's a **Low Risk** event, it might only call `log_incident`.

---

## 🛠️ Tools (Agent Capabilities)

* **block_ip(ip)** → Blocks malicious IP addresses.
* **alert_admin(message)** → Sends critical alerts to administrators.
* **log_incident(details)** → Records security events for auditing.

---

## 🚀 Example Request & Response

### Request:
```json
{
  "logs": [
    "Failed login attempts from IP 192.168.1.10",
    "Normal API request from user admin"
  ]
}
```

### Response:
```json
{
  "overall_risk": "High",
  "average_confidence": 92.0,
  "total_logs": 2,
  "analysis": [...],
  "actions_taken": [
    "I have analyzed the logs. The IP 192.168.1.10 was identified in a brute force attack and has been blocked. I have also alerted the administrator and logged the incident for auditing. The second log was a normal request and only required logging."
  ]
}
```

---

## ▶️ Setup Instructions

### 1. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add environment variables
```env
GOOGLE_API_KEY=your_api_key_here
```

### 4. Run application
```bash
uvicorn app.main:app --reload
```

---

## 📌 Key Features

### ✅ Autonomous Agent
* No more hardcoded if-else logic for security responses.
* LLM-driven tool selection and execution.

### ✅ Parallel Execution
* Fast processing of log batches using `asyncio`.

### ✅ Structured Output
* Reliable JSON responses for integration with other systems.

### ✅ Context-Aware AI
* Understands attack patterns (SQLi, Brute Force, DDoS) and responds appropriately.

---

## 💡 Author Notes
This upgrade transforms the system from a passive analyzer into an active **Agentic Security Orchestrator**.

---
