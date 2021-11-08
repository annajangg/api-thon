from requests import api, models
from random import choice

Response: type = models.Response  # this is the type of a response object

res: Response = api.get("https://api.le-systeme-solaire.net/rest/bodies/")

data: list[dict[str: str]] = res.json()["bodies"]

print(choice(data))
# for planet in data:
#     if planet["englishName"] and not planet["isPlanet"]:
        
#         print("Planet: " + planet["englishName"] + ", id: " + planet["id"])
