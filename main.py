#!/usr/bin/python3
""" main for the web app """
from flask import Flask, request, render_template

from models.helpers import search, build_result
from models.inverted_idx import get_matrix_repr


app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        search_quiery = request.form.get("search_query")
        results = build_result(search(search_quiery, get_matrix_repr))
        return render_template('result.html', results=results)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
