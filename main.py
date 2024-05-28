#!/usr/bin/python3
""" main for the web app """
from flask import Flask, request, render_template
from assignment2 import reload
from models.file import File, create_files
from models.quiery import SearchQuiery
from models.helpers import search
import json


app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        search_quiery = request.form.get("search_query")
        results = {}
        try:
            with open('stemmed.json') as file:
                idx_terms = json.load(file)
                print(idx_terms)
                results = search(search_quiery=SearchQuiery(search_quiery=idx_terms), file_lists=create_files(), idx_terms=idx_terms)
                print('------------------ try Block -----------------------')
                print(results)
        except FileNotFoundError:
            pass
        
        return render_template('result.html', results=results)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
