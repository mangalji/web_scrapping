from bs4 import BeautifulSoup
import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
              "image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
}



# chars=[]
# for i in range(26):
# 	chars.append(chr(97+i))

# for i in range(26):

url = "https://www.espncricinfo.com/cricketers/team/india-6/alpha-a"

response = requests.get(url, headers=headers)
print(response.status_code)

soup = BeautifulSoup(response.text,'html.parser')
div_ds_grid = soup.find_all("div",class_="ds-grid")
print(div_ds_grid)
# for div in div_ds_grid:
# 	print(div)
# 
