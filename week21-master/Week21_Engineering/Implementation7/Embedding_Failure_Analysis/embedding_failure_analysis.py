def find_failure_cases(query):
    lower_query = (query or "").lower()
    cases = [
        f"Ambiguous term '{query or 'bank'}': the system may mix different meanings of the same word.",
        "Short or noisy queries often receive unstable rankings because the available context is limited.",
        "Out-of-domain requests can fail when the document set does not match the target topic.",
        "Rare terms may not be represented well if the corpus does not contain enough supporting examples.",
        "Polysemy such as 'bank' can produce different results depending on surrounding context.",
    ]
    if "bank" in lower_query:
        cases.insert(0, "The query 'bank' shows the classic ambiguity problem because it can refer to a riverbank or a financial institution.")
    return cases
