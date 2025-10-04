from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"
}

url = "https://www.proflowers.com/blog/types-of-flowers"

response = requests.get(url,headers=headers)
print(response.status_code)

soup = BeautifulSoup(response.text,'html.parser')

flowers = soup.find_all("h3")
for flower in flowers:
	print(flower.get_text())