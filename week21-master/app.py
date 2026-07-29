from flask import Flask, render_template, request

from prompt_filter import filter_prompt
from record import add_record

from Week21_Engineering.Implementation1.Similarity_Engine.similarity import cosine_similarity, euclidean_distance
from Week21_Engineering.Implementation2.TFIDF_Retrieval.tfidf_search import search as tfidf_search
from Week21_Engineering.Implementation3.Embedding_Similarity.embedding_similarity import cosine as full_matrix
from Week21_Engineering.Implementation4.Vector_Search.vector_search import top_k, euclidean_search
from Week21_Engineering.Implementation5.Embedding_Search.embedding_search import search2
from Week21_Engineering.Implementation6.Gradient_Descent.gradient_descent_demo import run_gradient_demo
from Week21_Engineering.Implementation7.Embedding_Failure_Analysis.embedding_failure_analysis import find_failure_cases

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

@app.route("/", methods=["GET", "POST"])
def index():
    q = request.form.get("query", "").strip()

    if request.method == "POST":
        ok, msg = filter_prompt(q)
        if not ok:
            add_record(q, None, "error", False, msg)
            return render_template("index.html", error=msg)

        cosine_results = top_k(q)
        euclidean_results = euclidean_search(q)
        tfidf_results = tfidf_search(q)
        embedding_results = search2(q)
        gradient_summary = run_gradient_demo()
        tfidf_top = tfidf_search(q)
        expected = [tfidf_top[0][0]] if tfidf_top else []
        failure_cases = find_failure_cases(q, expected_ids=expected)
        add_record(q, {
            "cosine": cosine_results,
            "euclidean": euclidean_results,
            "tfidf": tfidf_results,
            "embedding": embedding_results
        }, "ok", True, "")

        return render_template(
            "index.html",
            error=None,
            cosine_results=cosine_results,
            euclidean_results=euclidean_results,
            tfidf_results=tfidf_results,
            embedding_results=embedding_results,
            gradient_summary=gradient_summary,
            failure_cases=failure_cases
        )

    return render_template(
        "index.html",
        error=None,
        cosine_results=[],
        euclidean_results=[],
        tfidf_results=[],
        embedding_results=[],
        gradient_summary=None,
        failure_cases=[]
    )

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
