import requests


response = requests.get("https://api.github.com/this-api-should-not-exist")

print(response.headers["X-RateLimit-Remaining"])

print(response.status_code)
