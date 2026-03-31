import json

with open("posts.json") as f:
    posts = json.load(f)

rss = """<?xml version="1.0"?>
<rss version="2.0"><channel>
<title>Updates</title>
"""

for post in posts:
    rss += f"""
<item>
<title>{post['title']}</title>
<description>{post['description']}</description>
</item>
"""

rss += "</channel></rss>"

with open("feed.xml", "w") as f:
    f.write(rss)
