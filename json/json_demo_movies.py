import json

content = ""
with open("scify_movies.json") as fid:
    for line in fid:
        content += line
movies = json.loads(content)
print(movies)
print(movies["Movies"])
print(movies["Movies"]["Movie1"])
