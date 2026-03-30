You are a senior AI architect. Upgrade my existing FastAPI + LangChain + Gemini project (already using a single agent with tools) into a **Multi-Agent System**.

---

# ⚠️ CRITICAL INSTRUCTION

Before writing ANY code:

1. **Read `requirements.txt`**
2. Use ONLY the versions specified
3. Ensure all LangChain APIs used are compatible with those versions
4. DO NOT use deprecated APIs
5. Maintain compatibility with `langchain-google-genai`

---

# 🎯 GOAL

Currently:

* Single agent handles everything

Upgrade to:
👉 **Multi-Agent Architecture with clear separation of responsibilities**

---

# 🧠 ARCHITECTURE DESIGN

Implement 3 agents:

---

## 🔹 1. Planner Agent

**Responsibility:**

* Analyze batch results
* Decide what needs to be done
* Create structured plan

**Input:**

* Logs
* Analysis results

**Output:**

```json id="planner_out"
{
  "tasks": [
    {"action": "block_ip", "ip": "192.168.1.10"},
    {"action": "alert_admin", "message": "..."}
  ]
}
```

---

## 🔹 2. Executor Agent

**Responsibility:**

* Execute tasks using tools
* Convert plan → real actions

Uses:

* block_ip
* alert_admin
* log_incident

---

## 🔹 3. Supervisor Agent (Lightweight)

**Responsibility:**

* Validate results
* Ensure no unnecessary actions
* Optional refinement

---

# 📂 FILE STRUCTURE

Create:

```id="multi_agent_structure"
app/
├── agents/
│   ├── planner_agent.py
│   ├── executor_agent.py
│   ├── supervisor_agent.py
│   └── __init__.py
```

---

# ⚙️ IMPLEMENTATION DETAILS

---

## 1. Planner Agent

File: `planner_agent.py`

* Use LLM (Gemini)
* No tools required
* Output structured JSON plan

Prompt should:

* Act as cybersecurity planner
* Decide:

  * Which actions are needed
  * Extract IPs if needed
* Be strict about JSON output

---

## 2. Executor Agent

File: `executor_agent.py`

* Use LangChain tool-calling agent
* Pass tools:

  * block_ip
  * alert_admin
  * log_incident

Input:

* Planner output

Output:

* List of executed actions

---

## 3. Supervisor Agent

File: `supervisor_agent.py`

* Simple LLM validation layer
* Ensures:

  * No duplicate actions
  * No unnecessary blocking
* Can modify or filter actions

---

## 4. Modify Service Layer

File: `app/services/ai_service.py`

---

### Replace current agent logic with:

Flow:

```id="multi_agent_flow"
Logs
 ↓
LLM Analysis (existing)
 ↓
Planner Agent → creates plan
 ↓
Executor Agent → executes tools
 ↓
Supervisor Agent → validates/refines
 ↓
Final Response
```

---

## 5. Maintain Existing Features

DO NOT REMOVE:

* Parallel processing (asyncio)
* Fault tolerance
* Aggregation logic

---

## 6. Output Format

Final response:

```json id="final_out"
{
  "overall_risk": "...",
  "average_confidence": ...,
  "total_logs": ...,
  "analysis": [...],
  "plan": [...],
  "actions_taken": [...]
}
```

---

## 7. Error Handling

* If planner fails → fallback to no actions
* If executor fails → skip failed task
* Ensure API never crashes

---

## 8. Prompt Engineering (IMPORTANT)

Each agent must have:

* Clear role definition
* Strict output format
* Minimal hallucination

---

## 9. Code Quality

* Modular design
* Clean separation of concerns
* Async support where possible

---

# 📘 README UPDATE (MANDATORY)

Update README.md with:

---

## 🔥 Multi-Agent AI System (NEW)

Explain:

### Architecture:

* Planner Agent
* Executor Agent
* Supervisor Agent

### Why Multi-Agent:

* Better decision making
* Separation of concerns
* Scalable design

---

### Update Flow Diagram:

```id="readme_flow"
Logs → Analysis → Planner → Executor → Supervisor → Response
```

---

### Add Example:

Show:

* Input logs
* Planner output
* Final actions

---

### Add Section:

## 🧠 Why This Matters

Explain:

* Real-world AI systems use multi-agent
* Similar to:

  * CrewAI
  * AutoGPT
  * Enterprise AI systems

---

# 🚀 EXPECTED OUTCOME

After implementation:

* System uses multiple agents collaboratively
* No single point of decision logic
* Highly modular and scalable
* Strong resume-level project

---

# ⚠️ FINAL INSTRUCTION

* Use only compatible APIs from requirements.txt
* Avoid deprecated LangChain patterns
* Ensure everything runs without errors

---

# 🎯 DELIVERABLE

Return:

* All new agent files
* Updated service layer
* Updated README
* Working multi-agent system
