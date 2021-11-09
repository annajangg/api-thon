from flask import Flask, render_template, redirect, request, url_for
from flask.templating import Environment
from livereload import Server
from requests import get
from requests.models import Response

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
async def index():
    if request.method == "POST":

        object_name = request.form['object_name']

        # TODO: make your api request for the object the user specified
        res: Response = get("https://api.agify.io", params={"name": "Kaki"})
        data = res.json()

        if object_name == '':
            return render_template("index.html")

        return render_template("result.html", object_name=data["count"])
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)