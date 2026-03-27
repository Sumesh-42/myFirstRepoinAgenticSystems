# github_api.py

import requests

# Base API URL
base_url = "https://api.github.com/search/repositories"

# Query parameters
params = {
    "q": "python",          # search keyword
    "sort": "stars",       # sort by stars
    "order": "desc",       # highest first
    "per_page": 5          # limit to 5 results
}

# Send request
response = requests.get(base_url, params=params)

# Check if request was successful
if response.status_code == 200:
    data = response.json()

    print("\nTop 5 Python repositories on GitHub:\n")

    # Loop through repositories
    for repo in data["items"]:
        name = repo["name"]
        stars = repo["stargazers_count"]

        print(f"Repository: {name}")
        print(f"Stars: {stars}")
        print("-" * 30)

else:
    print("Failed to fetch data from GitHub API")