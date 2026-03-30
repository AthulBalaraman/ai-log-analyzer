from langchain.tools import tool

@tool
def block_ip(ip: str) -> str:
    """Block a malicious IP address."""
    return f"Blocked IP {ip}"

@tool
def alert_admin(message: str) -> str:
    """Send an alert message to the system administrator."""
    return f"Admin alerted: {message}"

@tool
def log_incident(details: str) -> str:
    """Log a security incident for auditing purposes."""
    return f"Incident logged: {details}"