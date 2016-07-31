import requests, bs4

r = requests.get('http://barmvicente.pythonanywhere.com/')

blog = bs4.BeautifulSoup(r.text, 'lxml')

titles = blog.select('h1')

for i in range(1, len(titles)):
	print(titles[i].getText())