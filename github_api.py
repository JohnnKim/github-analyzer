import requests

BASE_URL = "https://api.github.com/users/"

def fetch_repos(username):
    url = f"{BASE_URL}{username}/repos"
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception(f"GitHub API error: {res.status_code}")
    return res.json()