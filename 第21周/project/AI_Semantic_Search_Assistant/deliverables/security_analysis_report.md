# Security Analysis Report

## Where are the attack entry points?
The main attack entry point is the user query field. If a user can submit arbitrary text, an attacker may try to override instructions, request hidden content, or ask the system to ignore safety policies.

## How does the Prompt Filter reduce risk?
The prompt filter reduces risk by enforcing input length limits, rejecting special characters, and blocking common injection phrases such as ignore, override, jailbreak, and reveal secrets.

## What security risks remain?
Current risks include simple keyword-based bypasses, false positives on benign text, and the absence of output-level checks. The system also does not yet separate system instructions from user prompts in a robust way.

## How can we improve it?
- Add a policy classifier or LLM-based safety checker
- Use a stricter allowlist for tool use and external actions
- Log and monitor suspicious prompts
- Combine rule-based filtering with semantic adversarial evaluation
