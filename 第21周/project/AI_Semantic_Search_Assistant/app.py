from flask import Flask, render_template, request
from project.AI_Semantic_Search_Assistant.search import SearchEngine
from project.AI_Semantic_Search_Assistant.prompt_filter import filter_prompt

app = Flask(__name__)
engine = SearchEngine(data_path="dataset.txt")


@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    message = ""
    if request.method == "POST":
        query = request.form.get("query", "")
        allowed, info = filter_prompt(query)
        if not allowed:
            message = info
        else:
            results = engine.search(query, top_k=5)
            message = f"Query accepted: {info}"
    return render_template("index.html", results=results, message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
