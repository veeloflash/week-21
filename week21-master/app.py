from flask import Flask, render_template, request

from prompt_filter import filter_prompt
from Week21_Engineering.Implementation1.Similarity_Engine.similarity import cosine_similarity
from Week21_Engineering.Implementation2.TFIDF_Retrieval.tfidf_search import search
from Week21_Engineering.Implementation3.Embedding_Similarity.embedding_similarity import cosine
from Week21_Engineering.Implementation4.Vector_Search.vector_search import top_k, euclidean_search
from Week21_Engineering.Implementation5.Embedding_Search.embedding_search import search2
from Week21_Engineering.Implementation6.Gradient_Descent.gradient_descent_demo import run_gradient_demo
from Week21_Engineering.Implementation7.Embedding_Failure_Analysis.embedding_failure_analysis import find_failure_cases

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


@app.route("/", methods=["GET", "POST"])
def index():
    selected_algorithm = request.form.get("algorithm", "cosine")
    q = request.form.get("query", "").strip()

    if request.method == "POST":
        ok, message = filter_prompt(q)
        if not ok:
            return render_template("index.html", error=message, selected_algorithm=selected_algorithm)

        cosine_result = cosine_similarity(q, "semantic search over documents")
        tfidf_results = search(q)
        embedding_matrix = str(cosine())  # convert to string
        vector_results = top_k(q)
        euclidean_results = euclidean_search(q)
        embedding_results = search2(q)
        gradient_summary = run_gradient_demo(learning_rate=0.01, epochs=200)
        failure_cases = find_failure_cases(q)

        return render_template(
            "index.html",
            cosine_result=cosine_result,
            tfidf_results=tfidf_results,
            embedding_matrix=embedding_matrix,
            vector_results=vector_results,
            euclidean_results=euclidean_results,
            embedding_results=embedding_results,
            gradient_summary=gradient_summary,
            failure_cases=failure_cases,
            error=None,
            selected_algorithm=selected_algorithm,
        )

    return render_template(
        "index.html",
        error=None,
        cosine_result=None,
        tfidf_results=[],
        embedding_matrix="[]",
        vector_results=[],
        euclidean_results=[],
        embedding_results=[],
        gradient_summary={"learning_rate": 0.01, "epochs": 200, "losses": [], "final_parameters": {"w": 0.0, "b": 0.0}},
        failure_cases=[],
        selected_algorithm="cosine",
    )


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
