# User manual

1. Install dependencies with `python -m pip install -r requirements.txt`.
2. Start the service with `python app.py`.
3. Enter an English AI/ML question and submit it.
4. Compare the three Top-5 lists. Cosine is higher-is-better; Euclidean is lower-is-better.
5. Unsafe or empty prompts are rejected before retrieval and recorded in the security log.