# Week21_AI_Semantic_Search_Assistant

An auditable Flask product for comparing lexical and semantic retrieval on the same 50-record English AI/ML corpus. The product surface lives in `app.py`, `src/`, `templates/`, `static/`, `data/`, and `docs/`; classroom experiments are isolated in `Week21_Engineering/`.

## Product workflow

`User query -> Prompt Filter -> Normalization -> TF-IDF / Embedding -> Cosine / Euclidean -> Ranking -> Top-5 -> Web UI`

Every query produces three comparable Top-5 lists: TF-IDF, deterministic embedding plus cosine similarity, and deterministic embedding plus Euclidean distance. The product implementation explicitly computes dot product, L2 norms, zero-vector handling, cosine division, and Euclidean distance in `src/search.py`; the encoder only creates vectors.

## Repository structure

```text
Week21_AI_Semantic_Search_Assistant/
├── README.md
├── requirements.txt
├── app.py
├── src/               # product code, independent of experiment numbering
├── tests/
├── data/dataset.json
├── templates/
├── static/
└── docs/
Week21_Engineering/   # independent Implementation 1-7 experiments
```

## Dataset

- Records: **50** (automatically rejected below 50)
- Domain: introductory artificial intelligence and machine learning
- Source: project-authored educational sentences in `data/dataset.json`
- Language: English
- Licence: original coursework material, shared for educational use
- Schema: stable `id` plus `text`; IDs are used as ground truth labels

## Evaluation and deliverables

- [Architecture diagram](docs/architecture_diagram.svg)
- [20-query product results](docs/product_test_results.csv)
- [Testing results](docs/testing_results.md), including Hit@5, Precision@5, Recall@5, and MRR
- [User manual](docs/user_manual.md)
- [Model analysis report](docs/model_analysis_report.md)
- [Security analysis report](docs/security_analysis_report.md)
- [Project reflection](docs/project_reflection.md)
- [Security lab results](docs/security_lab_results.csv)
- [Embedding similarity report](docs/embedding_similarity_testing_report.md)
- [Embedding failure analysis](docs/embedding_failure_analysis.csv)
- [Gradient descent report](docs/gradient_descent_report.md)

## Run

```bash
python -m pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000`. The product needs no pretrained-model download: its reproducible local encoder is deliberately kept separate from the engineering embedding experiments.

## Verify

```bash
python -m unittest discover -s tests -v
```
