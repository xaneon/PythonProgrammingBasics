import json
import pandas as pd
from pprint import pprint

reduced_dict = dict()
reduced_dict["Movie"] = list()
reduced_dict["Director"] = list()
reduced_dict["Runtime"] = list()

with open("scify_movies.json", "r") as fid:
    movies = json.load(fid)

for movie, content in movies["Movies"].items():
    reduced_dict["Movie"].append(movie)
    reduced_dict["Director"].append(content["Director"])
    reduced_dict["Runtime"].append(content["Runtime"])

pprint(reduced_dict)
movieids = reduced_dict["Movie"]
reduced_dict.pop("Movie", None)

df = pd.DataFrame(reduced_dict, index=movieids)
print(df.head())

df.to_excel("scify_movies.xlsx", sheet_name="Movies")

df2 = pd.read_excel("scify_movies.xlsx", sheet_name="Movies")

df == df2 # note the difference between N/A and NaN

