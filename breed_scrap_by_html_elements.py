import requests
from bs4 import BeautifulSoup

url_for_cows = "https://en.wikipedia.org/wiki/List_of_cattle_breeds"
url_for_rabbits = "https://en.wikipedia.org/wiki/List_of_rabbit_breeds"
url_for_bufffaloes = "https://en.wikipedia.org/wiki/List_of_water_buffalo_breeds"
url_for_rats = "https://www.hammertechltd.com/blog/rat-breeds"
url_for_horse = "https://www.ehorses.com/magazine/horse-breeds/"
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

def entries_of_cow_buff_rab_rat_hor_animal():
	breeds_of_cows()
	breeds_of_buffaloes()
	breeds_of_rabbits()
	breeds_of_rats()
	breeds_of_horses()
	animal_names_func()

def animal_names_func():

  url_for_animals_names = "https://animalcorner.org/animals/"

  response = requests.get(url, headers=headers)
  
  soup = BeautifulSoup(response.text,'html.parser')
  all_animals = []
  divs = soup.find_all("div",class_="one-third")
  # print(divs)
  for div in divs:
      # print(div)
      # for a in div.find_all('a')
      # print(div)
      # line_br = div.find('br')
      # print(line_br)
      # a = line_br.find('a')
      # print(a)
      # animal_name = a.get_text(strip=True)
      # all_animals.append(animal_name)
      a_tag = div.find_all('a')
      if len(a_tag) >= 2:
          second_a_tag = a_tag[1]
          animal_name = second_a_tag.get_text(strip=True)
          # print(animal_name)
          all_animals.append(animal_name)
  
  
  # print(all_animals)
  for animal in all_animals:
      try:
          anim_name = f"Animal name: {animal}"
          with open('animal_names.txt','a') as file:
              anim_names = file.write(anim_name + '\n')
              print(anim_name)
      except Exception as e:
          print(e)


def breeds_of_cows():

	response = requests.get(url_for_cows, headers=headers)
	soup = BeautifulSoup(response.text, "html.parser")
	
	tables = soup.find_all("table", {"class": "wikitable"})
	
	print(f"Total tables found: {len(tables)}")
	
	all_breeds_of_cows = []
	
	
	for table in tables:
	    rows = table.find_all("tr")[1:]
	    for row in rows:
	        cols = row.find_all(["td", "th"])
	        if cols:
	            breed_name = cols[0].get_text(strip=True)
	            all_breeds_of_cows.append(breed_name)
	
	
	for breed in all_breeds_of_cows:
		try:
			cow_breeds = f"cow breed name: {breed}"
			with open('cows_breeds.txt','a') as file:
				cow_breed = file.write(cow_breeds + '\n')
				print('----------------------------------')
				print('cow breed:', breed)
		except Exception as e:
			print(e)

def breeds_of_buffaloes():

	response = requests.get(url_for_bufffaloes,headers=headers)
	soup = BeautifulSoup(response.text,'html.parser')

	tables = soup.find_all("table",{'class':'wikitable'})
	print(f"total tables found: {len(tables)}")

	all_breeds_of_buffaloes = []

	for table in tables:
		rows = table.find_all("tr")[1:]
		for row in rows:
			cols = row.find_all(['td'])
			if cols:
				breed = cols[0].find('a')
				if breed:
					breed_name = breed.get_text(strip=True)
					all_breeds_of_buffaloes.append(breed_name)
				else:
					breed_name = cols[0].get_text(strip=True)

					all_breeds_of_buffaloes.append(breed_name)

	lists = soup.find_all("ul")
	for ul in lists:
		for li in ul.find_all("li"):
			breed = li.find("a")
			if breed:
				all_breeds_of_buffaloes.append(breed.get_text(strip=True))
			else:
				breed_in_text = li.get_text(strip=True)
				if breed_in_text:
					all_breeds_of_buffaloes.append(breed_in_text)


	for breed in all_breeds_of_buffaloes:
		try:
			buffalo_breeds = f"buffalo breed name: {breed}"
			with open('buffalo_breeds.txt','a') as file:
				buffalo_breed = file.write(buffalo_breeds + '\n')
				print('-----------------------------------------')
				print('buffalo_breed: ',buffalo_breed)
		except Exception as e:
			print(e)

def breeds_of_rabbits():

	response = requests.get(url_for_rabbits, headers=headers)
	soup = BeautifulSoup(response.text,'html.parser')

	tables = soup.find_all("table",{"class":"wikitable"})

	print(f"Total tables found: {len(tables)}")

	all_breeds_of_rabbits = []

	for table in tables:
		rows = table.find_all("tr")[1:]
		for row in rows:
			cols = row.find_all(['td','th'])
			if cols:
				breed = cols[0].find('a')
				if breed:
					breed_name = breed.get_text(strip=True)
					all_breeds_of_rabbits.append(breed_name)

	for breed in all_breeds_of_rabbits:
		try:
			rab_breeds = f"rabbit breed name: {breed}"
			with open('rabbit_breeds.txt','a') as file:
				rab_breed = file.write(rab_breeds + '\n')
				print('----------------------------------')
				print('rabbit breed:', breed)
		except Exception as e:
			print(e)

def breeds_of_horses():

	response = requests.get(url_for_horse, headers=headers)
	
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

def breeds_of_rats():

	response = requests.get(url_for_rats, headers=headers)
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


# choice = input("enter the pet category: ")

# if choice == 'cow' or choice == 'Cow':
# 	breeds_of_cows()

# elif choice == 'rabbit' or choice == 'Rabbit':
# 	breeds_of_rabbits()


# elif choice == 'buffalo' or choice == 'Buffalo':
# 	breeds_of_buffaloes()

# elif choice == 'rat' or choice == 'Rat':
# 	breeds_of_rats()

# elif choice == 'horse' or choice == 'Horse':
# 	breeds_of_horses()
	
