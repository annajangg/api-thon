from flask import Flask, render_template, redirect, request, url_for
from flask.templating import Environment
from livereload import Server
from requests import get
from requests.models import Response
from api import grab_url

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
async def index():
    if request.method == "POST":

        object_name = str(request.form['object_name'])

        # TODO: make your api request for the object the user specified
        # space_res = get("https://api.le-systeme-solaire.net/rest/bodies/", params={"order": "eccentricity,asc"})
        # data = space_res.json()["bodies"]
        refined_res = get(f"https://api.le-systeme-solaire.net/rest/bodies/{object_name}")
        data = refined_res.json()

        gravity: float = data["gravity"]
        discovered_by: str = data["discoveredBy"]
        discovery_date: str = data["discoveryDate"]
        moons: list[str] = []

        url: str = grab_url(object_name)

        if data["moons"] != None:
            for entry in data["moons"]:
                moons.append(entry['moon'])
            return render_template("result.html", object_name=object_name, moons=moons, gravity=gravity, discovered_by=discovered_by, discovery_date=discovery_date, url=url)
        
        if object_name == '':
            return render_template("index.html")

        return render_template("result.html", object_name=object_name, moons=moons, gravity=gravity, discovered_by=discovered_by, discovery_date=discovery_date, url=url)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)