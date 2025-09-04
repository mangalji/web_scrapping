import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
              "image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
}



url_for_horse = "https://www.ehorses.com/magazine/horse-breeds/"
response = requests.get(url_for_horse, headers=headers)

# print(response.status_code)
print(response.text[:500])

soup = BeautifulSoup(response.text,'html.parser')

all_breeds_of_horses = []

lists = soup.find("div",class_="elementor-text-editor")
# print(lists)

# h3 = lists.find_all("h3")
uls = lists.find_all("ul")
for ul in uls:
	for li in ul:
		breed = li.get_text(strip=True)
		# print(breed)
		if breed:
			all_breeds_of_horses.append(breed)

for horse_breed in all_breeds_of_horses:
	try:
		horses_breeds = f"breed name: {horse_breed}"
		with open("horse_breeed.txt",'a') as file:
			horses_breed = file.write(horses_breeds + '\n')
			print("-------------------------------------")
			print("horse breed: ",horses_breeds)
	except Exception as e:
		print(e)


