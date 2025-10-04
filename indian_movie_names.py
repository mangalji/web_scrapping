import requests
from bs4 import BeautifulSoup

def movie_names_func():
	
	for i in range(1900,2028):
	
		all_movie_names = []
		url = f"https://en.wikipedia.org/wiki/List_of_Hindi_films_of_{i}"
	
		headers = {
	    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
	                  "AppleWebKit/537.36 (KHTML, like Gecko) "
	                  "Chrome/115.0 Safari/537.36",
	    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
	              "image/webp,image/apng,*/*;q=0.8",
	    "Accept-Language": "en-US,en;q=0.9",
	    "Connection": "keep-alive",
		}
	
		response = requests.get(url,headers=headers)
	
		soup = BeautifulSoup(response.text,'html.parser')
	
		tables = soup.find_all("table",class_="wikitable")
	
		# 	print(tables)
	
		for table in tables:
			# print(table)
			rows = table.find_all('tr')[1:]
			# print(rows)
			for row in rows:
				# print(row)
				movie_name_column = row.find_all('td')
				# print(movie_name_column)
				for movie in movie_name_column:
					# print(movie)
					# print(movie.get_text(strip=True))
					# break
					movie_name_in_i = movie.find('i')
					if movie_name_in_i:
						movie_name = movie_name_in_i.get_text(strip=True)
						# print(movie_name.get_text(strip=True))
						# print(movie_name)
						all_movie_names.append(movie_name)
	
		for movie_names in all_movie_names:
		# try:
			movies_name = f"{movie_names} released in {i} year"
			with open("moviee.txt",'a') as file:
				moviee = file.write(movies_name + '\n')
				print("---------------------")
				print(movies_name)
		# except Exception as e:
		# 	print(e)
	
movie_names_func()




















	# # print(tables)
	# # print(tables)
	# for table in tables:
	# 	# print(table)
	# 	rows = table.find_all('tr')[1:]
	# 	for row in rows:
	# 		columns = row.find_all(['td','th'])
	# 		# for cols in columns:
	# 		for cols in columns:
	# 		# movie_name = columns[0].get_text(strip=True)
	# 			movie_name = cols.find('i')
	# 			if movie_name:
	# 				name = movie_name.get_text(strip=True)
	# 				# print(movie_name)
	# 				print(name)
	# 				all_movie_names.append(movie_name)

