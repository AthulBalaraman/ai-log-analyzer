from langchain.tools import tool

@tool
def block_ip(ip: str) -> str:
    """
    Blocks a malicious IP address from accessing the system.
    Use this for high-risk threats like brute force or DDoS.
    """
    return f"Blocked IP {ip}"

@tool
def alert_admin(message: str) -> str:
    """
    Sends a security alert notification to the system administrator.
    Use this for suspicious activities or medium-to-high risk incidents.
    """
    return f"Admin alerted: {message}"

@tool
def log_incident(details: str) -> str:
    """
    Logs a security incident for auditing and later analysis.
    Always use this to record details of any suspicious activity detected.
    """
    return f"Incident logged: {details}"