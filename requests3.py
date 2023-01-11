import requests

response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "requests+language:python"},
    # Paramter q defines search paramters in repos, the query is "requests" in files that are written in python in the repo
)

if response.status_code == 200:
    print("Success!")
    response_json = response.json()
    print(response_json.keys())
    print(response_json)
elif response.status_code == 403:
    print("API rate used up")
elif response.status_code == 404:
    print("Not Found.")
