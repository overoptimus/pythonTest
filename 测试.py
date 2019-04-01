import requests

req = requests.get("http://files.grouplens.org/datasets/movielens/ml-100k.zip")
print(req.text)


print(isinstance(12, int))
