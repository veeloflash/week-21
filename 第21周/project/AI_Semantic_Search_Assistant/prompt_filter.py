import re


def filter_prompt(prompt: str):
    if not isinstance(prompt, str):
        return False, "Input must be a text string."

    normalized = prompt.strip()
    if not normalized:
        return False, "Please enter a non-empty query."

    if len(normalized) > 300:
        return False, "Input is too long. Keep it under 300 characters."

    if re.search(r"[^\w\s,.;:!?()\-]", normalized):
        return False, "Special characters are not allowed in this demo."

    blocked_patterns = [
        r"\b(ignore|drop|bypass|override|system|developer)\b",
        r"(prompt\s+injection|jailbreak|admin password|reveal secrets)",
    ]
    lower_prompt = normalized.lower()
    if any(re.search(pattern, lower_prompt) for pattern in blocked_patterns):
        return False, "Unsafe or injection-like prompt detected."

    return True, normalized
