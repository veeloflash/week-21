from flask import Flask, render_template, request

from src.security import filter_prompt
from record import add_record

from src.search import compare_rankings

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

        rankings = compare_rankings(q)
        cosine_results = rankings["cosine"]
        euclidean_results = rankings["euclidean"]
        tfidf_results = rankings["tfidf"]
        embedding_results = cosine_results
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
            gradient_summary=None,
            failure_cases=[]
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
