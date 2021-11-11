from requests import get
from requests.models import Response
from random import choice

# 1. Starting small
# https://boredapi.com/api/activity/, returns a random activity for you to do.

bored_api_response: Response = get("https://boredapi.com/api/activity/")

# response codes
# 200 means everything went ok.
# 400 errors are errors on your end.
# 500 errors are errors on the servers end.

print(bored_api_response.status_code) 

# json == JavaScript Object Notation.
# just a large dictionary with str keys and variable values.

print(bored_api_response.json())

# other fields
bored_api_response.url  # the url that was sent with the request (more interesting when params are involved)

# 2. Requests with params
# https://api.agify.io, returns average age for people with a given name (passed as a parameter)
# 

def grab_url(planet: str) -> str:
    return f"/{planet.lower()}.jpg"

def random_body(bodies: list[str]):
    return choice(bodies)

# name = "io"
# space_res = get(f"https://api.le-systeme-solaire.net/rest/bodies/{name}")
# space_data = space_res.json()
# print(space_data)

space_res = get("https://api.le-systeme-solaire.net/rest/bodies/", params={"order": "eccentricity,asc"})
data = space_res.json()["bodies"]
print(choice(data))
# for s in data:
#     if str(s["eccentricity"]) != "":
#         print(s["id"], end="")
#         print(f": {s['englishName']} {str(s['eccentricity'])}", end="")
#         print()

# refined_res = get("https://api.le-systeme-solaire.net/rest/bodies/io")
# print(refined_res.json())

# 3. Requests with an API key