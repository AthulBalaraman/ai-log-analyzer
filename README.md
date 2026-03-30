# 🛡️ AI Log Analyzer (Level 1 → Batch Processing + Parallel Execution)

## 🚀 Overview

This project is an **AI-powered log analysis system** built using:

* LangChain (latest architecture)
* Google Gemini (LLM)
* FastAPI (backend)

It analyzes system logs and provides:

* Context-aware log classification
* Attack detection
* Risk level assessment
* Suggested mitigation actions
* **Batch log processing (NEW)**
* **Parallel execution (NEW)**
* **Aggregated system risk scoring (NEW)**

---

## 🧠 What’s New in This Branch

### 🔥 Batch Processing + Parallel Execution

Previously:

* Only single log analysis
* Sequential processing (slow)

Now:

* Accepts **multiple logs in one request**
* Processes logs **concurrently using asyncio**
* Computes **overall system risk**
* Handles failures gracefully (fault tolerance)

👉 Result:

* Faster processing ⚡
* Scalable architecture 🚀
* Real-world SOC simulation 🛡️

---

## ⚙️ Tech Stack

* Python 3.10+
* LangChain (latest modular syntax)
* langchain-google-genai
* FastAPI
* Pydantic
* asyncio (parallel execution)
* Uvicorn

---

## 🏗️ Project Structure

```id="0d3b9n"
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

```id="9hps7y"
Client Request (Multiple Logs)
   ↓
FastAPI Route (/analyze)
   ↓
Service Layer
   ↓
Parallel Execution (asyncio.gather)
   ↓
LangChain Pipeline (prompt → LLM → parser)
   ↓
Individual Log Analysis
   ↓
Aggregation Logic
   ↓
Final Structured Response
```

---

## 🧠 How It Works

### 1. Input (NEW - Batch Support)

User sends multiple logs:

```json id="o6u4qz"
{
  "logs": [
    "Failed login attempt from IP 192.168.1.1",
    "User attempted SQL injection using SELECT * FROM users",
    "High traffic spike from single IP"
  ]
}
```

---

### 2. Parallel Processing (NEW)

* Each log is processed **independently**
* Uses `asyncio.gather()` for concurrency
* Reduces response time significantly

---

### 3. Individual Log Analysis

For each log:

* Detects log type (authentication, database, etc.)
* Identifies attack type (brute force, SQL injection, etc.)
* Assigns confidence score

---

### 4. Fault Tolerance (NEW)

* If one log fails:

  * System continues processing others
  * Returns fallback response instead of crashing

---

### 5. Aggregation Logic (NEW)

System computes:

* Total logs analyzed
* Average confidence score
* Overall system risk

---

### 6. Final Response

```json id="qk9k1y"
{
  "overall_risk": "High",
  "average_confidence": 88.3,
  "total_logs": 3,
  "analysis": [
    {
      "log_type": "authentication",
      "attack_type": "brute_force",
      "summary": "Multiple failed login attempts detected",
      "suspicious_activity": "Repeated login failures",
      "risk_level": "High",
      "confidence_score": 92,
      "suggested_action": "Block IP and enable rate limiting"
    },
    {
      "log_type": "database",
      "attack_type": "sql_injection",
      "summary": "SQL query manipulation detected",
      "suspicious_activity": "Injection pattern found",
      "risk_level": "High",
      "confidence_score": 90,
      "suggested_action": "Sanitize inputs and monitor queries"
    }
  ]
}
```

---

## ▶️ Setup Instructions

### 1. Create virtual environment

```bash id="zq3c0s"
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

---

### 2. Install dependencies

```bash id="7oxhbm"
pip install -r requirements.txt
```

---

### 3. Add environment variables

```env id="xz82lu"
GOOGLE_API_KEY=your_api_key_here
```

---

### 4. Run the application

```bash id="3smw9p"
uvicorn app.main:app --reload
```

---

### 5. Test API

Open:

```id="n8o1v1"
http://127.0.0.1:8000/docs
```

Use `/analyze` endpoint (POST)

---

## 📌 Key Features

### ✅ Batch Log Processing (NEW)

* Accepts multiple logs in a single request

### ✅ Parallel Execution (NEW)

* Faster processing using asyncio

### ✅ Fault Tolerance (NEW)

* Prevents system failure due to single log error

### ✅ Aggregated Risk Scoring (NEW)

* Provides system-level threat assessment

### ✅ Context-Aware AI Analysis

* Log classification + attack detection

### ✅ Structured Output

* Reliable JSON responses

---

## 📌 Key Learning Outcomes

* Async programming with asyncio
* Parallel execution design
* Fault-tolerant system design
* Aggregation logic for AI systems
* Advanced LangChain pipeline usage

---

## ⚠️ Challenges Solved

* ❌ Slow sequential processing
* ❌ Single point of failure
* ❌ No system-level insight

✔️ Solved using:

* Parallel execution
* Error handling
* Aggregated scoring

---

## 🚀 Next Improvements

* Tool calling (AI takes actions like blocking IP)
* Multi-agent architecture
* Vector database (RAG memory)
* Real-time log streaming (WebSockets)

---

## 💡 Author Notes

This project is being built incrementally with:

* Clean architecture
* Feature-based branching
* Production-grade AI practices

Each branch represents a **milestone toward building an autonomous AI security system**

---
