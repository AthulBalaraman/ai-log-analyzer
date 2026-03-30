import streamlit as st
import httpx
import asyncio
from typing import List, Dict

# --- Configuration ---
API_URL = "http://127.0.0.1:8000/analyze"

# --- Predefined Logs ---
LOG_EVENTS = [
    "Failed login attempt from IP 192.168.1.100 (admin)",
    "Brute force attempt: 50 failed logins from 45.33.22.11 in 2 minutes",
    "Suspicious login from Russia (IP 91.198.174.192) for user 'dev_user'",
    "SQL Injection attempt detected: User entered \"' OR 1=1 --\" in login field",
    "Cross-Site Scripting (XSS) detected: <script>alert('XSS')</script> in comment field",
    "API abuse: Client 10.0.0.5 requesting /api/v1/users 500 times per minute",
    "High traffic spike: 10,000 requests/sec from IP 185.12.33.4",
    "Port scanning detected from 203.0.113.5: Scanning ports 21, 22, 23, 80, 443",
    "Successful login: User 'admin' logged in from 192.168.1.5",
    "Normal API request: GET /api/v1/health from 127.0.0.1",
    "File inclusion attempt: GET /index.php?page=../../../../etc/passwd",
    "Suspicious file upload: 'shell.php' uploaded to /uploads/",
    "SSH brute force: Multiple failed root logins from 5.188.62.144",
    "Command Injection attempt: POST /exec?cmd=ls; rm -rf /",
    "Sensitive data exposure: Unencrypted PII found in outbound traffic to 190.10.0.5",
    "Unauthorized access: User 'guest' attempted to access /admin/settings",
    "DDoS attempt: TCP SYN flood from multiple sources targeting port 80",
    "Malicious URL detected: User clicked on http://malicious-site.com/phish",
    "Outbound connection to known C2 server: IP 10.0.0.2 connecting to 8.8.8.8:4444",
    "Configuration change: Firewall rules modified by user 'sysadmin' from 10.0.0.1",
    "Normal User Logout: User 'jdoe' logged out successfully.",
    "Database Query: SELECT count(*) FROM orders; (Execution time: 45ms)"
]

# --- UI Setup ---
st.set_page_config(page_title="🛡️ AI Security Log Analyzer", layout="wide")

st.title("🛡️ AI Security Log Analyzer Dashboard")
st.markdown("### Interactive UI for testing and visualizing AI-driven security log analysis.")

# --- Sidebar ---
st.sidebar.title("ℹ️ Information")
st.sidebar.info(
    "This dashboard simulates real-world vulnerable log events and sends them to a "
    "FastAPI backend powered by LangChain and Gemini for analysis."
)
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔥 Key Features")
st.sidebar.markdown("- AI-driven analysis\n- Risk level detection\n- Automated planning\n- Multi-agent execution")

# --- Event Selection ---
st.header("1. Event Selection Panel")

# State for multiselect
if 'selected_logs' not in st.session_state:
    st.session_state.selected_logs = []

col_select1, col_select2 = st.columns([4, 1])

with col_select1:
    selected_logs = st.multiselect(
        "Choose logs to simulate:",
        options=LOG_EVENTS,
        default=st.session_state.selected_logs,
        key="log_selector"
    )

with col_select2:
    if st.button("Select All"):
        st.session_state.selected_logs = LOG_EVENTS
        st.rerun()
    if st.button("Clear Selection"):
        st.session_state.selected_logs = []
        st.rerun()

# --- Execution ---
st.header("2. Action")

if st.button("Analyze Logs", type="primary"):
    if not selected_logs:
        st.warning("Please select at least one log to analyze.")
    else:
        with st.spinner("Analyzing logs..."):
            try:
                response = httpx.post(API_URL, json={"logs": selected_logs}, timeout=30.0)
                if response.status_code == 200:
                    data = response.json().get("result", {})
                    st.session_state.results = data
                    st.success("Analysis complete!")
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Error connecting to backend: {str(e)}")

# --- Results Display ---
if 'results' in st.session_state:
    results = st.session_state.results
    
    st.header("3. Results Display")
    
    # --- Overall Summary ---
    summary_col1, summary_col2, summary_col3 = st.columns(3)
    
    overall_risk = results.get("overall_risk", "N/A")
    risk_color = "red" if overall_risk.lower() == "high" else "orange" if overall_risk.lower() == "medium" else "green"
    
    summary_col1.metric("Overall Risk", overall_risk)
    summary_col2.metric("Average Confidence", f"{results.get('average_confidence', 0):.1f}%")
    summary_col3.metric("Total Logs", results.get("total_logs", 0))

    # --- Actions Taken Section ---
    if results.get("actions_taken"):
        st.markdown("### 🚨 Actions Taken:")
        for action in results["actions_taken"]:
            st.info(f"- {action}")
    else:
        st.write("No specific actions taken.")

    st.markdown("---")

    # --- Detailed Analysis (Card Layout) ---
    st.markdown("### 🔍 Detailed Analysis")
    
    analysis_list = results.get("analysis", [])
    for idx, item in enumerate(analysis_list):
        risk_level = item.get("risk_level", "Low")
        color = "#ff4b4b" if risk_level.lower() == "high" else "#ffa500" if risk_level.lower() == "medium" else "#00c853"
        
        with st.container():
            st.markdown(
                f"""
                <div style="border-left: 5px solid {color}; padding: 15px; border-radius: 5px; background-color: #f0f2f6; margin-bottom: 20px;">
                    <h4 style="margin-top: 0;">Log #{idx + 1}: {item.get('attack_type', 'Unknown')}</h4>
                    <p><strong>🧾 Raw Log:</strong> <code>{selected_logs[idx] if idx < len(selected_logs) else 'N/A'}</code></p>
                    <p><strong>🧠 AI Analysis Summary:</strong> {item.get('summary', 'N/A')}</p>
                    <p><strong>⚠️ Risk Level:</strong> <span style="color: {color}; font-weight: bold;">{risk_level}</span></p>
                    <p><strong>🎯 Suspicious Activity:</strong> {item.get('suspicious_activity', 'N/A')}</p>
                    <p><strong>📊 Confidence Score:</strong> {item.get('confidence_score', 0)}%</p>
                    <p><strong>💡 Suggested Action:</strong> {item.get('suggested_action', 'N/A')}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
