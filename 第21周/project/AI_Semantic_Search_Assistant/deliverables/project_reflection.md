# Project Reflection

1. The biggest technical challenge was implementing a simple retrieval pipeline that could compare TF-IDF and embedding-based search in a consistent way.
2. The biggest performance bottleneck is the naive linear scan over the entire document corpus for every query.
3. The biggest security risk is prompt injection through the free-form query interface.
4. For one million documents, the system would need a vector database, approximate nearest-neighbor indexing, and better hardware or distributed serving.
5. The next version should add real embedding models, hybrid retrieval, and more robust safety controls.
