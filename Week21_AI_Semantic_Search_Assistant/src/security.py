import base64
import logging
import re
import unicodedata

logger = logging.getLogger("semantic_search.security")
DIRECT_PATTERNS = [r"ignore\s+(all\s+)?previous", r"disregard\s+(the\s+)?system", r"bypass\s+(the\s+)?filter"]
INDIRECT_PATTERNS = [r"system\s+prompt", r"reveal\s+hidden\s+instructions", r"follow\s+only\s+my\s+instructions"]
JAILBREAK_PATTERNS = [r"developer\s+mode", r"do\s+anything\s+now", r"no\s+rules"]

def normalize_prompt(prompt):
    normalized = unicodedata.normalize("NFKC", prompt).replace("\u200b", "").replace("\ufeff", "")
    return " ".join(normalized.strip().split()).lower()

def _decoded_forms(prompt):
    try:
        decoded = base64.b64decode(prompt, validate=True).decode("utf-8").lower()
    except (ValueError, UnicodeDecodeError):
        decoded = ""
    return [prompt, decoded]

def filter_prompt(prompt):
    if not isinstance(prompt, str):
        return False, "Input must be a text string."
    normalized = normalize_prompt(prompt)
    if not normalized:
        return False, "Please enter a non-empty query."
    if len(normalized) > 300:
        return False, "Input is too long. Keep it under 300 characters."
    reasons = []
    for form in _decoded_forms(normalized):
        for category, patterns in (("direct injection", DIRECT_PATTERNS), ("indirect injection", INDIRECT_PATTERNS), ("jailbreak", JAILBREAK_PATTERNS)):
            if any(re.search(pattern, form) for pattern in patterns):
                reasons.append(category)
    if any(word in normalized for word in ("忽略", "绕过", "覆盖", "игнорировать", "omitir")):
        reasons.append("multilingual injection")
    if reasons:
        logger.warning("Blocked prompt category=%s", ",".join(sorted(set(reasons))))
        return False, "High-risk prompt blocked: " + ", ".join(sorted(set(reasons)))
    return True, normalized

def check_output(text):
    normalized = normalize_prompt(text)
    return not any(token in normalized for token in ("system prompt", "hidden instructions", "api key"))