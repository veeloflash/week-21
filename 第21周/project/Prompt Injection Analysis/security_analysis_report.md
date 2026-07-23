# Security Analysis Report

## 1. Which prompts are likely to cause abnormal behavior?
Prompts that explicitly try to ignore instructions, bypass safety rules, reveal hidden content, or output secrets are most likely to trigger abnormal behavior. In this experiment, P3-P8 and P11 were the clearest examples. The filter blocked them before any unsafe continuation could happen.

## 2. Which prompts had no effect?
The prompts that had no effect were the ordinary, benign tasks in P1, P2, P10, and P12. They did not contain jailbreak language and therefore remained allowed. P9 also did not attempt an attack, but it was blocked because the phrase "prompt injection" matched the filter’s rule set.

## 3. Why?
The current defense is based on simple keyword matching. It checks for terms such as ignore, drop, bypass, override, system, developer, and phrases like prompt injection or jailbreak. This is effective against obvious attacks, but it cannot understand context well enough to distinguish a malicious instruction from a harmless discussion about the same topic.

## 4. What is the biggest difference between Prompt Injection and traditional vulnerabilities?
Traditional vulnerabilities usually target code execution, memory corruption, authentication, or access control. Prompt Injection targets the model’s instruction-following behavior instead. It exploits the boundary between user input and hidden system instructions, so the vulnerability is at the language interface rather than the application code path.

## 5. If you were designing an enterprise AI system, how would you defend it?
1. Use layered defenses: prompt filtering, policy checks, output classification, and human review for sensitive actions.
2. Separate system instructions from user content and prevent user text from overriding hidden policy.
3. Restrict tool use and external actions so that the model cannot access secrets or perform high-risk operations without approval.
4. Log prompts and monitor attack patterns continuously.
5. Add a second-stage safety checker before sensitive outputs are shown or acted on.

## Conclusion
The experiment shows that simple rule-based protection can block obvious prompt injection attempts, but it should be combined with contextual detection and safer system design to reduce both false positives and false negatives.
