from flask import Flask, render_template, redirect, request, url_for
from flask.templating import Environment
from livereload import Server

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        object_name = request.form['object_name']

        if object_name == '':
            return render_template("index.html")

        return render_template("result.html", object_name=object_name)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)