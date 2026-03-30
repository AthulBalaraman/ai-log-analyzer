# 🛡️ AI Log Analyzer (Level 1 → Log Intelligence Upgrade)

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
* **Log type classification (NEW)**
* **Attack detection (NEW)**
* **Confidence scoring (NEW)**

---

## 🧠 What’s New in This Branch

### 🔥 Intelligent Log Analysis (Major Upgrade)

Previously:

* Generic log analysis
* No understanding of log context

Now:

* Detects **log type** (authentication, API, database, etc.)
* Identifies **attack type** (brute force, SQL injection, etc.)
* Assigns **confidence score (0–100)**
* Produces **more accurate and contextual insights**

👉 Result:

* Smarter AI reasoning
* Closer to real-world SOC systems
* Stronger resume impact

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

```id="v5y6j2"
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

```id="t8t6hz"
Client Request
   ↓
FastAPI Route (/analyze)
   ↓
Service Layer (LangChain)
   ↓
Prompt Template (with classification rules)
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

User sends logs:

```json id="slqz3s"
{
  "logs": "User failed login 15 times in 20 seconds from IP 192.168.1.10"
}
```

---

### 2. Prompt Intelligence (NEW)

The system now:

* Classifies log type:

  * authentication
  * api
  * database
  * network
  * system

* Detects attack types:

  * brute_force
  * sql_injection
  * ddos
  * none
  * unknown

---

### 3. LLM Analysis

Gemini performs:

* Pattern recognition
* Threat detection
* Context-aware reasoning

---

### 4. Structured Output (from previous step)

* Enforced using PydanticOutputParser
* Guarantees valid JSON

---

### 5. Final Response

```json id="k7o3lu"
{
  "log_type": "authentication",
  "attack_type": "brute_force",
  "summary": "Multiple failed login attempts detected",
  "suspicious_activity": "Repeated login failures indicating brute force attack",
  "risk_level": "High",
  "confidence_score": 92,
  "suggested_action": "Block IP and enable account lockout policy"
}
```

---

## ▶️ Setup Instructions

### 1. Create virtual environment

```bash id="98p4uz"
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

---

### 2. Install dependencies

```bash id="fwgsh2"
pip install -r requirements.txt
```

---

### 3. Add environment variables

```env id="3khtb5"
GOOGLE_API_KEY=your_api_key_here
```

---

### 4. Run the application

```bash id="2lflpz"
uvicorn app.main:app --reload
```

---

### 5. Test API

Open:

```id="5j9q9s"
http://127.0.0.1:8000/docs
```

---

## 🧪 Example Request

```json id="9l6u8y"
{
  "logs": "POST /login failed 10 times from IP 45.33.21.1"
}
```

---

## 📌 Key Features

### ✅ Context-Aware Analysis (NEW)

* Understands log type
* Applies domain-specific reasoning

### ✅ Attack Detection (NEW)

* Identifies common attack patterns
* Maps logs to known threats

### ✅ Confidence Scoring (NEW)

* Adds reliability indicator to predictions

### ✅ Structured Output

* Clean JSON responses
* API-ready format

---

## 📌 Key Learning Outcomes

* Prompt engineering with classification rules
* Context-aware AI systems
* Structured output enforcement using Pydantic
* LangChain pipeline (`prompt | llm | parser`)
* Designing intelligent AI services

---

## ⚠️ Challenges Solved

* ❌ Generic AI responses
* ❌ No context awareness
* ❌ Weak reasoning

✔️ Solved using:

* Prompt design improvements
* Controlled output schema
* Explicit classification rules

---

## 🚀 Next Improvements

* Batch log processing (multiple logs at once)
* Risk scoring system (aggregated threat scoring)
* Multi-agent architecture
* Tool calling (auto-block IP simulation)
* Vector DB memory (RAG)

---

## 💡 Author Notes

This project is being developed incrementally with:

* Clean architecture
* Feature-based branching
* Production-level AI practices

Each branch represents a **step toward building an autonomous AI security system**

---
