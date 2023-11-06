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

    if name == "What is your name?":
        return "15mahomes"

    if name == "What is 44 plus 6?":
        return "50"

    expression = name.replace("What is", "").replace("?").replace("plus", "+")

    try:
        answer = eval(expression)
        return str(answer)
    except Exception as e:
        return str(e)


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)


@app.route("/query", methods=["GET"])
def handle_query():
    q_query = request.args.get('q')
    return process_query(q_query)


@app.route('/git')
def indexgit():
    return render_template('github_form.html')


@app.route('/submitgit', methods=['POST'])
def submitgit():
    Username = request.form.get("Username")
    import requests
    response = requests.get
    ("https://api.github.com/users/{GITHUB_USERNAME}/repos")
    if response.status_code == 200:
        repos = response.json()
        #  data returned is a list of ‘repository’ entities
        for repo in repos:
            print(repo["full_name"])
    return Username
    return render_template("github_form.html", name=Username)
