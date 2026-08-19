# Product testing results

The CSV contains 20 manually labelled queries. `Expected` stores relevant document IDs and each query requires at least one relevant ID in Top-5.

`Hit@5 = 1` when any expected ID is retrieved; `Precision@5 = hits / 5`; `Recall@5 = hits / relevant IDs`; `MRR` is reciprocal rank of the first hit. The fixture is deliberately transparent so TF-IDF, cosine, and Euclidean rankings can be audited side by side.