import re

# Layer 1: Static Pattern Detection
DENY_PATTERNS = [
    r"ignore (all )?previous instructions",
    r"system prompt",
    r"output the full prompt",
    r"dan mode",
    r"jailbreak",
    r"sql injection",
    r"rm -rf"
]

# Layer 3: Tool Policy
ALLOWED_TOOLS = ["get_weather", "search_wiki"]

def static_check(text: str):
    for pattern in DENY_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return False, f"Flagged by Pattern Match: {pattern}"
    return True, None

def validate_tool_call(tool_name: str):
    if tool_name not in ALLOWED_TOOLS:
        return False, f"Policy Violation: Tool '{tool_name}' is restricted."
    return True, None