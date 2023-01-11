import requests

pload = {"username": "Olivia", "password": "123"}

response = requests.post("https://httpbin.org/post", data=pload)

if response.status_code == 200:
    print("Success!")
    response_json = response.json()
    print(response_json.keys())
    print(response_json)
elif response.status_code == 403:
    print("API rate used up")
elif response.status_code == 404:
    print("Not Found.")
