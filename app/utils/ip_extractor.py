import re

def extract_ip(log: str) -> str:
    match = re.search(r"(\\d+\\.\\d+\\.\\d+\\.\\d+)", log)
    return match.group(0) if match else "unknown"