import requests

# Base URL for accessing GitHub's user repositories API
BASE_URL = "https://api.github.com/users/"

def fetch_repos(username):
    # Construct the full API URL for the user's repositories
    url = f"{BASE_URL}{username}/repos"

    try:
        # Send a GET request to the GitHub API with a timeout (in seconds)
        res = requests.get(url, timeout=10)
    except requests.exceptions.Timeout:
        # Handle timeout explicitly
        raise Exception("Request timed out. Please try again later.")
    except requests.exceptions.RequestException as e:
        # Handle other request-related errors
        raise Exception(f"Request failed: {e}")

    # Check if the request was successful (status code 200 OK)
    if res.status_code != 200:
        # Raise an exception with the status code if something went wrong
        raise Exception(f"GitHub API error: {res.status_code}")

    # Parse and return the JSON response (a list of repositories)
    return res.json()
