You are a senior full-stack AI engineer. Extend my existing FastAPI + LangChain + Gemini project by building a **Streamlit-based UI dashboard** inside the same codebase.

---

# ⚠️ CRITICAL INSTRUCTION

Before writing ANY code:

1. Read `requirements.txt`
2. Use only compatible versions of:

   * streamlit
   * requests / httpx
3. Do NOT upgrade existing dependencies unless necessary
4. Ensure compatibility with current FastAPI backend

---

# 🎯 GOAL

Build a **Streamlit UI dashboard** that:

* Simulates **20+ real-world vulnerable log events**
* Allows:

  * Single click execution
  * Multi-select execution
* Sends logs to backend `/analyze` API
* Displays:

  * Raw log
  * AI analysis
  * Risk level
  * Actions taken

---

# 📂 FILE TO CREATE

```plaintext
app/ui/streamlit_app.py
```

---

# 🧠 UI FEATURES

---

## 🔹 1. Page Layout

Use Streamlit to create:

* Title:
  "🛡️ AI Security Log Analyzer Dashboard"

* Sections:

  1. Event Selection Panel
  2. Action Button
  3. Results Display

---

## 🔹 2. Predefined Log Events (IMPORTANT)

Create at least **20 realistic logs**, including:

### Authentication Attacks

* Failed login multiple times from IP
* Brute force attempt
* Suspicious login location

### Web Attacks

* SQL injection attempt
* XSS attack
* API abuse

### Network Attacks

* High traffic spike from single IP
* Port scanning detected

### Normal Logs (for contrast)

* Successful login
* Normal API request

Store them in a list like:

```python
logs = [
    "Failed login attempts from IP 192.168.1.10",
    "User attempted SQL injection using SELECT * FROM users",
    ...
]
```

---

## 🔹 3. Multi-Select Input

Use:

```python
st.multiselect()
```

Allow user to:

* Select multiple logs
* Quickly simulate multiple attacks

---

## 🔹 4. Execute Button

Add:

```python
st.button("Analyze Logs")
```

On click:

* Send selected logs to FastAPI backend

---

## 🔹 5. API Integration

Call:

```plaintext
POST http://127.0.0.1:8000/analyze
```

Send:

```json
{
  "logs": [...]
}
```

Use `requests` or `httpx`

---

## 🔹 6. Display Results (VERY IMPORTANT)

For each log, show:

### 📦 Card Layout (per log)

Display:

#### 🧾 Raw Log

#### 🧠 AI Analysis Summary

#### ⚠️ Risk Level (color-coded)

* High → Red
* Medium → Yellow
* Low → Green

#### 🎯 Attack Type

#### 📊 Confidence Score

---

## 🔹 7. Actions Taken Section

Display:

```plaintext
🚨 Actions Taken:
- Blocked IP ...
- Alert sent ...
- Incident logged ...
```

---

## 🔹 8. Overall Summary

At top or bottom show:

* Overall Risk
* Average Confidence
* Total Logs

---

## 🔹 9. UI Enhancements (IMPORTANT)

Use:

* `st.columns()` for layout
* `st.container()` for grouping
* `st.markdown()` with HTML for styling
* Emojis for better UX

---

## 🔹 10. Loading State

Add spinner:

```python
with st.spinner("Analyzing logs..."):
```

---

## 🔹 11. Error Handling

If API fails:

* Show error message
* Do not crash UI

---

# 🎨12. add these too

* Add "Select All" button
* Add "Clear Selection"
* Add sidebar info panel

---

# 🔄 FLOW

```plaintext
User selects logs
   ↓
Clicks Analyze
   ↓
Streamlit calls FastAPI
   ↓
Backend processes (AI + agents)
   ↓
Response returned
   ↓
UI displays structured insights
```

---

# 📘 README UPDATE (MANDATORY)

Update README.md:

---

## 🔥 Streamlit Dashboard (NEW)

Explain:

* Interactive UI for testing AI system
* Simulates real-world attack scenarios
* Helps visualize:

  * AI decisions
  * Risk levels
  * Actions taken

---

## 🖥️ How to Run UI

Add:

```bash
streamlit run app/ui/streamlit_app.py
```

---

## 🧪 Demo Flow

1. Select logs
2. Click Analyze
3. View results

---

## 🎯 Why This Matters

Explain:

* Demonstrates full-stack AI system
* Makes project demo-ready
* Simulates real SOC dashboard

---

# 🚀 EXPECTED OUTPUT

* Fully working Streamlit UI
* Integrated with FastAPI backend
* Clean UX with structured results
* Updated README

---

# ⚠️ FINAL NOTES

* Keep code modular
* Do not break backend
* Ensure UI runs independently
* Maintain clean structure

---

# 🎯 DELIVERABLE

Return:

* Complete streamlit_app.py
* Updated README
* Any required dependency updates
