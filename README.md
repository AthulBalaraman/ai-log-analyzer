# 🛡️ AI Log Analyzer (Multi-Agent AI System)

## 🚀 Overview

This project is an **autonomous Multi-Agent AI-powered log analysis and response system** built using:

* LangChain (latest architecture)
* Google Gemini (LLM)
* FastAPI (backend)
* **Multi-Agent Orchestration (Planner, Executor, Supervisor)**

It not only analyzes logs but also **collaboratively plans, executes, and validates security actions** using multiple specialized AI agents.

---

## 🔥 Multi-Agent AI System (NEW)

### Architecture:

1.  **Planner Agent:** Analyzes the batch analysis results and creates a structured action plan in JSON format. It decides which IPs to block and what alerts to send.
2.  **Executor Agent:** A tool-calling agent that takes the plan and executes the necessary tools (`block_ip`, `alert_admin`, `log_incident`).
3.  **Supervisor Agent:** A lightweight validation layer that reviews the analysis and the actions taken to ensure they are appropriate and provides a final polished assessment.

### Why Multi-Agent:

*   **Better Decision Making:** Specialized agents focus on specific tasks (planning vs. execution), leading to more reliable outcomes.
*   **Separation of Concerns:** Each agent has a clear role, making the system easier to debug and extend.
*   **Scalable Design:** New agents or tools can be added without bloating a single agent's logic.

---

## 🧠 Why This Matters

*   **Real-world AI systems** are moving towards multi-agent architectures to handle complex workflows.
*   Similar to frameworks like **CrewAI**, **AutoGPT**, and **Enterprise AI systems**, this project demonstrates how multiple LLM instances can collaborate to solve a problem.
*   It provides a robust foundation for building autonomous security operations centers (SOCs).

---

## 🔥 Streamlit Dashboard (NEW)

The project now includes an interactive **Streamlit-based UI dashboard** for easy testing and visualization of the AI Security Log Analyzer.

### Features:
* **Interactive UI:** A modern dashboard for simulating real-world security events.
* **Predefined Log Events:** 20+ realistic attack scenarios (SQLi, XSS, Brute Force, etc.) and normal logs.
* **Multi-Select Execution:** Select multiple logs and analyze them in a single batch.
* **Visual Insights:** 
    * **Risk Levels:** Color-coded indicators (High/Medium/Low).
    * **AI Analysis:** Detailed summaries and confidence scores for each log.
    * **Actions Taken:** Real-time feedback on security actions performed by the agents.
* **Overall Summary:** Quick metrics on total logs, average confidence, and overall risk.

---

## 🖥️ How to Run UI

1. Ensure the FastAPI backend is running:
```bash
uvicorn app.main:app --reload
```

2. In a new terminal, run the Streamlit app:
```bash
streamlit run app/ui/streamlit_app.py
```

---

## 🧪 Demo Flow

1. **Select Logs:** Use the multi-select dropdown to pick one or more security logs.
2. **Analyze:** Click the **"Analyze Logs"** button.
3. **Review Results:** View the overall risk metrics and detailed AI analysis cards for each log.
4. **Observe Actions:** See the list of automated actions taken by the AI agents (e.g., blocking IPs, alerting admins).

---

## 🎯 Why This Matters

* **Demo-Ready:** Provides a visual way to showcase the power of the multi-agent AI system.
* **Realistic Testing:** Easily simulate complex attack scenarios without manual API calls.
* **SOC Visualization:** Mimics a simplified Security Operations Center (SOC) dashboard.

---

## ⚙️ Tech Stack

* Python 3.10+
* LangChain (v1.2+ as per requirements)
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
│   ├── agents/                # UPDATED: Multi-Agent Logic
│   │   ├── __init__.py
│   │   ├── planner_agent.py
│   │   ├── executor_agent.py
│   │   ├── supervisor_agent.py
│   │   └── security_agent.py  # Legacy single agent
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
Logs → Analysis → Planner → Executor → Supervisor → Response
```

Detailed Flow:
1.  **Logs** are received via FastAPI.
2.  **LLM Analysis** classifies each log in parallel.
3.  **Planner Agent** creates a JSON plan of action.
4.  **Executor Agent** calls tools based on the plan.
5.  **Supervisor Agent** validates the results and provides a final summary.
6.  **Final Response** is returned to the client.

---

## 🚀 Example Request & Response

### Request:
```json
{
  "logs": [
    "Failed login attempts from IP 192.168.1.10",
    "SQL injection attempt detected on /api/users"
  ]
}
```

### Planner Output (Internal):
```json
{
  "tasks": [
    {"action": "block_ip", "ip": "192.168.1.10"},
    {"action": "alert_admin", "message": "Multiple high-risk attacks detected: Brute Force and SQL Injection."},
    {"action": "log_incident", "details": "Blocked IP 192.168.1.10 and alerted admin regarding SQLi."}
  ]
}
```

### Final Response:
```json
{
  "overall_risk": "High",
  "average_confidence": 95.0,
  "total_logs": 2,
  "analysis": [...],
  "plan": [
    {"action": "block_ip", "ip": "192.168.1.10"},
    {"action": "alert_admin", "message": "..."},
    {"action": "log_incident", "details": "..."}
  ],
  "actions_taken": [
    "Blocked IP 192.168.1.10",
    "Admin alerted: Multiple high-risk attacks detected...",
    "Incident logged: ...",
    "Supervisor Assessment: The security response was appropriate. Both threats were neutralized and documented."
  ]
}
```

---

## 🛠️ Tools (Agent Capabilities)

* **block_ip(ip)** → Blocks malicious IP addresses.
* **alert_admin(message)** → Sends critical alerts to administrators.
* **log_incident(details)** → Records security events for auditing.

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

### ✅ Multi-Agent Orchestration
* Planner, Executor, and Supervisor working together.
* Structured JSON communication between agents.

### ✅ Parallel Execution
* Fast processing of log batches using `asyncio`.

### ✅ Structured Output
* Reliable JSON responses for integration with other systems.

### ✅ Context-Aware AI
* Understands attack patterns (SQLi, Brute Force, DDoS) and responds appropriately.

---

## 💡 Author Notes
This upgrade transforms the system into a sophisticated **Multi-Agent Security Orchestrator**, mimicking real-world enterprise AI workflows.

---
