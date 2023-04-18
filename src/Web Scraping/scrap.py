import requests
import bs4

result = requests.get("https://example.com")
soup = bs4.BeautifulSoup(result.text, "lxml")

# query selectors
title = soup.select('title')[0].getText()
title['class']
print(result.text)


str 