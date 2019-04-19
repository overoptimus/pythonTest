import urllib.request as req
import sys, os

path = os.getcwd() + '\\img'

pathExist = os.path.exists(path)

if not pathExist:
    os.makedirs(path)

url = req.Request('http://placekitten.com/200/300')
response = req.urlopen(url)
cat_img = response.read()

file_name = path + '\\cat_200_300.jpg'

with open(file_name, 'wb') as f:
    f.write(cat_img)
