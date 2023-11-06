from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('github_form.html')


@app.route('/submit', methods=['POST'])
def submit():
    Username = request.form.get("Username")
    return render_template("github_form.html", name=Username)
