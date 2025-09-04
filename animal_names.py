import requests
from bs4 import BeautifulSoup
import json

# url = "https://www.espncricinfo.com/cricketers/team/india-6"

# headers = {
#     'accept': '*/*',
#     'accept-language': 'en-IN,en;q=0.9',
#     'origin': 'https://www.espncricinfo.com',
#     'priority': 'u=1, i',
#     'referer': 'https://www.espncricinfo.com/',
#     'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Linux"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-site',
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
#     'x-hsci-auth-token': 'exp=1756905869~hmac=e584749b84aac806d3f0c5c9b3d04a6cc27563428dd1519f26ceb178b0228ebe',
# }

# params = {
#     'teamId': '6'
# }

# response = requests.get(url, params=params, headers=headers)
# soup = BeautifulSoup(response.text,'html.parser')
# print(soup)

# import requests
# from bs4 import BeautifulSoup

# url = "https://data.stackexchange.com/stackoverflow/queries?order_by=everything&page=2&pagesize=100"

headers = {
    'accept': '*/*',
    'accept-language': 'en-IN,en;q=0.9',
    'origin': 'https://www.espncricinfo.com',
    'priority': 'u=1, i',
    'referer': 'https://www.espncricinfo.com/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'x-hsci-auth-token': 'exp=1756905869~hmac=e584749b84aac806d3f0c5c9b3d04a6cc27563428dd1519f26ceb178b0228ebe',
}

# response = requests.get(url,headers=headers)

# soup = BeautifulSoup(response.text, 'html.parser')
# # print(soup)
# # div1 = soup.find("body", class_="page")
# # print(div1)
# div1 = soup.find("div", id="mainbar")
# print(div1)
# div2 = div1.find("ul",class_="querylist")
# print(div2)
# # for list_ in lists:

