from flask import Flask, render_template, request
from prompt_filter import filter_prompt
from src.Implementation1.similarity import cosine_similarity
from src.Implementation2.tfidf_search import search
from src.Implementation3.embedding_similarity import cosine
from src.Implementation4.vector_search import top_k
from src.Implementation5.embedding_search import search2
from src.Implementation6.gradient_descent_demo import run_gradient_demo
from src.Implementation7.embedding_failure_analysis import find_failure_cases

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        q = request.form.get("query", "").strip()
        ok, message = filter_prompt(q)
        if not ok:
            return render_template("index.html", error=message)

        cosine_result = cosine_similarity(q, "example text")
        tfidf_results = search(q)
        embedding_matrix = cosine()
        vector_results = top_k(q)
        embedding_results = search2(q)
        loss_curve = run_gradient_demo()
        failure_cases = find_failure_cases(q)
        return render_template(
            "index.html",
            cosine_result=cosine_result,
            tfidf_results=tfidf_results,
            embedding_matrix=embedding_matrix,
            vector_results=vector_results,
            embedding_results=embedding_results,
            loss_curve=loss_curve,
            failure_cases=failure_cases,
            error=None,
        )

    return render_template("index.html", error=None)


if __name__ == "__main__":
    app.run(debug=True)