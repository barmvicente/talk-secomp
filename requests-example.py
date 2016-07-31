import requests

r = requests.get('http://www.gutenberg.org/cache/epub/16865/pg16865.txt')

print(r.text[:485])