from requests import get
from requests.models import Response

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

def grab_url(planet: str, is_planet: bool) -> str:
    """Helper function to populate url variable in app.py. These files live in our 'static' folder."""
    if is_planet:
        return f"/{planet.lower()}.jpg"
    else:
        return f"/space.jpg"

# 3. Requests with an API key