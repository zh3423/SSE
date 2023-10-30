from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


def process_query(name):
    if name == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 \
million years ago"

    if name == "asteroids":
        return "Unknown"


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)


@app.route("/query", methods=["GET"])
def handle_query():
    q_query = request.args.get('q')
    return process_query(q_query)


def process_query_2(query):
    if query == "What is your name?":
        return "15mahomes"


@app.route("/query", methods=["GET"])
def query_endpoint():
    q_query = request.args.get('q')
    return process_query_2(q_query)
