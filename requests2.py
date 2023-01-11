import requests

response = requests.get("https://api.github.com/repos/SkafteNicki/dtu_mlops")

if response.status_code == 200:
    print("Success!")
elif response.status_code == 403:
    print("API rate used up")
elif response.status_code == 404:
    print("Not Found.")
