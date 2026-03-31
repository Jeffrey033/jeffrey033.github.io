import requests
import json

repo = "Jeffrey033/jeffrey033.github.io"  # aanpassen!

url = f"https://api.github.com/repos/{repo}/issues"
issues = requests.get(url).json()

posts = []

for issue in issues:
    if any(label["name"] == "bericht" for label in issue["labels"]):
        posts.append({
            "title": issue["title"],
            "description": issue["body"]
        })

with open("posts.json", "w") as f:
    json.dump(posts, f, indent=2)
