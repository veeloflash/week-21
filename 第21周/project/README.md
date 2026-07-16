# Search & Similarity Comparison Framework

A Flask-based web application that demonstrates and compares multiple text search and similarity computation methods using different NLP techniques.

## Overview

This project showcases 7 different implementations of text search and similarity algorithms, allowing users to compare their performance and behavior on the same queries. It provides both a web interface and programmatic access to various search methodologies.

## Features

- **Multiple Search Implementations**: Compare 5+ different search and similarity algorithms
- **Web Interface**: User-friendly Flask web application for interactive queries
- **Prompt Filtering**: Built-in security measures to detect and filter unsafe inputs
- **Diverse Algorithms**: From classical TF-IDF to modern sentence embeddings

## Project Structure

```
project/
├── app.py                          # Flask application entry point
├── prompt_filter.py                # Input validation and safety checks
├── dataset.txt                     # Document corpus for search
├── templates/
│   └── index.html                  # Web interface template
└── src/
    ├── Implementation1/
    │   └── similarity.py           # Cosine similarity using sentence embeddings
    ├── Implementation2/
    │   └── tfidf_search.py         # TF-IDF based search
    ├── Implementation3/
    │   └── embedding_similarity.py # Embedding similarity matrix computation
    ├── Implementation4/
    │   └── vector_search.py        # Vector-based top-k search
    ├── Implementation5/
    │   └── embedding_search.py     # Embedding-based semantic search
    ├── Implementation6/
    │   └── gradient_descent_demo.py # Gradient descent optimization demo
    └── Implementation7/
        └── embedding_failure_analysis.py # Analysis of embedding limitations
```

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup

1. Clone or download the project:
```bash
cd project
```

2. Install required dependencies:
```bash
pip install flask numpy scikit-learn sentence-transformers
```

## Usage

### Running the Web Application

Start the Flask server:
```bash
python app.py
```

Then open your browser and navigate to `http://localhost:5000`

### How to Use

1. Enter a search query in the web interface
2. The system will process your query using 5 different methods:
   - **Cosine Similarity**: Compares query against example text using embeddings
   - **TF-IDF Results**: Traditional term frequency-inverse document frequency search
   - **Embedding Similarity**: Shows the embedding similarity matrix
   - **Vector Search**: Returns top-k results using vector similarity
   - **Embedding Search**: Semantic search using sentence embeddings

### Programmatic Usage

You can import individual implementations:

```python
from src.Implementation1.similarity import cosine_similarity
from src.Implementation2.tfidf_search import tfidf_search
from src.Implementation5.embedding_search import search2

# Compute cosine similarity
result = cosine_similarity("your text", "reference text")

# Perform TF-IDF search
results = tfidf_search("your query", top_k=5)

# Perform embedding search
results = search2("your query")
```

## Implementations

### Implementation 1: Sentence Embedding Similarity
Uses the `sentence-transformers` library with the "all-MiniLM-L6-v2" model to compute cosine similarity between text pairs.

### Implementation 2: TF-IDF Search
Classical information retrieval approach using sklearn's TfidfVectorizer to find similar documents based on term frequencies.

### Implementation 3: Embedding Similarity Matrix
Computes and displays the similarity matrix between document embeddings.

### Implementation 4: Vector Search
Performs efficient k-nearest neighbor search in the embedding space.

### Implementation 5: Embedding-Based Search
Semantic search using pre-trained sentence embeddings to find relevant documents.

### Implementation 6: Gradient Descent Demo
Demonstrates gradient descent optimization for educational purposes.

### Implementation 7: Embedding Failure Analysis
Analyzes and documents cases where embedding-based methods may fail or produce unexpected results.

## Security

The application includes input validation through `prompt_filter.py`:
- Maximum input length: 300 characters
- Blocks potentially unsafe keywords (ignore, system, override, bypass)
- Returns validation errors when criteria are not met

## Data

The `dataset.txt` file contains the document corpus used for search operations. Each line represents a separate document that can be searched and compared against queries.

## Dependencies

- **Flask**: Web framework for the user interface
- **NumPy**: Numerical computations
- **scikit-learn**: TF-IDF vectorization and machine learning utilities
- **sentence-transformers**: Pre-trained sentence embedding models

## Technologies Used

- Python 3
- Flask (web framework)
- Scikit-learn (machine learning)
- Sentence Transformers (NLP embeddings)
- NumPy (numerical computing)

## Learning Objectives

This project is designed to help understand:
- Different text search methodologies
- Embeddings and their applications in NLP
- Comparison between traditional and modern NLP approaches
- Web application development with Flask
- Performance characteristics of various algorithms

## Future Enhancements

- Performance benchmarking and comparison metrics
- Visualization of embedding spaces
- Support for additional languages
- More sophisticated filtering options
- Batch query processing
- Results caching for better performance

## License

This project is for educational purposes.

## Author

Created as a learning project for NLP and search systems.
