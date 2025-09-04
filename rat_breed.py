import requests
from bs4 import BeautifulSoup

url_for_rats = "https://www.coopsandcages.com.au/blog/ultimate-list-rat-breeds/?srsltid=AfmBOoozSXXBSUibB0sQLUaI-7ZTFPcuiTpqdJDKIMZMawFc8Vpmgntf"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
              "image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
}

response = requests.get(url_for_rats, headers=headers)
# print(response.status_code)
print(response.status_code)
print(response.text[:500])

soup = BeautifulSoup(response.text,'html.parser')

all_breeds_of_rats = []

lists = soup.find("div",class_="entry-content")
# print(lists)
for li in lists.find_all("h2"):
  # print(li)
  breed = li.get_text(strip=True)
  print(breed)
  if breed:
    # breed_name = breed.find("strong")
    all_breeds_of_rats.append(breed)

# print(all_breeds_of_rats)
for rat_breed in all_breeds_of_rats:
  # try:
  rats_breeds = f"rat breed name: {rat_breed}"
  with open("rat_breeds.txt",'a') as file:
    rats_breed = file.write(rats_breeds + '\n')
    print("----------------------------------")
    print("rat breed: ", rats_breeds)
  # except Exception as e:
  #   print(e)

# try:
#     r = requests.get(url_for_rats, timeout=10)
#     print("Status:", r.status_code)
#     print("Headers:", r.headers)
# except Exception as e:
#     print("Error:", e)
