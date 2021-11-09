import requests


requests.get("https://api.agify.io", params={"name": "Marc"})
# or
requests.get("https://api.agify.io/?name=Marc")

name: str = input("What is your name?")
requests.get("https://api.agify.io", params={"name": name})