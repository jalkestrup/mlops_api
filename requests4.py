import requests

response = requests.get("https://imgs.xkcd.com/comics/making_progress.png")

if response.status_code == 200:
    print("Success!")
    with open(r"img.png", "wb") as f:
        f.write(response.content)
elif response.status_code == 403:
    print("API rate used up")
elif response.status_code == 404:
    print("Not Found.")
