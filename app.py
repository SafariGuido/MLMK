from flask import Flask, render_template, jsonify
import json
import pandas as pd

app = Flask(__name__)

def load_dict_from_file(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

@app.route("/data")
def get_data():
    dict1 = load_dict_from_file("Rank.json")
    dict2 = load_dict_from_file("Beers.json")
    dict3 = load_dict_from_file("total_scores.json")
    dict4 = load_dict_from_file("pen_dict.json")
    dict5 = load_dict_from_file("times.json")
    timestable = pd.DataFrame(dict5)
    html_table = timestable.to_html(classes="display", index=False)

    labels1 = list(dict1.keys())  # assume all dicts use same keys
    labels3 = list(dict3.keys())
    labels4 = list(dict4.keys())
    data = {
        "chart1":{
        "type":"chart",
        "labels": labels1,
        "datasets": [
            {"label": "Elo", "data": [dict1[k] for k in labels1]}
        ]
    },
        "info": {
            "type": "text",    # mark this as text
            "data": dict2["Gallons of Beer Drank"]      # send the dictionary as-is
    },
        "chart3":{
        "type":"chart",
        "labels": labels3,
        "datasets": [
            {"label": "Total Points", "data": [dict3[k] for k in labels3]}
        ]
    },
        "chart4":{
        "type":"chart",
        "labels": labels4,
        "datasets": [
            {"label": "Penalty Shots", "data": [dict4[k] for k in labels4]}
        ]
    },
        "table": {
            "type": "table",
            "html": html_table  # 👈 send as raw HTML
    }}
    return jsonify(data)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug=True)