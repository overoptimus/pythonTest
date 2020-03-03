import urllib.request

response = urllib.request.urlopen('http://www.fishc.com')
html = response.read()
html = html.decode("UTF-8")
print(html)
