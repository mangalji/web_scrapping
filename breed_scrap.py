import requests
import json

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-none-match': 'W/"18b0-iXI0GlNR3rO5oQR/x3PXvYfNmGM"',
    'origin': 'https://www.happypet.care',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
}

def entries_of_breeds_dog_cat_birds():
	breeds_of_dogs()
	breeds_of_cats()
	breeds_of_birds()

def breeds_of_dogs():
	for i in range(1,20):
		response = requests.get(
	    f'https://api.happypet.care/v1/breed/search-page?page={i}&limit=25&shedding_level=[]&quick_filter=[]&cost_of_buying=[]&temperament_with_dogs=[]&friendliness=[]&size=[%22Small%22]&outerFilter=[]&breed_slug=',
	    headers=headers,)

		complete_data = response.json()
		raw_data = complete_data['data']
		results = raw_data['results']
	
		for result in results:
			try:
				dog_breeds = f"dog breed name:{result['breed_name']}, size:{result['size']}, slug:{result['slug']}"
				with open('dog_breed.txt','a') as file:
					dog_breed = file.write(dog_breeds + '\n')
				print('-------------------------------------------')
				print(dog_breeds)
			except Exception as e:
				print(e) 

	for i in range(1,20):
		response = requests.get(
	    f'https://api.happypet.care/v1/breed/search-page?page={i}&limit=25&shedding_level=[]&quick_filter=[]&cost_of_buying=[]&temperament_with_dogs=[]&friendliness=[]&size=[%22Medium%22]&outerFilter=[]&breed_slug=',
	    headers=headers,)

		complete_data = response.json()	
		raw_data = complete_data['data']
		results = raw_data['results']
	
		for result in results:
			try:
				dog_breeds = f"dog breed name:{result['breed_name']}, size:{result['size']}, slug:{result['slug']}"
				with open('dog_breed.txt','a') as file:
					dog_breed = file.write(dog_breeds + '\n')
				print('-------------------------------------------')
				print(dog_breeds)
			except Exception as e:
				print(e)

	for i in range(1,20):
		response = requests.get(
	    f'https://api.happypet.care/v1/breed/search-page?page={i}&limit=25&shedding_level=[]&quick_filter=[]&cost_of_buying=[]&temperament_with_dogs=[]&friendliness=[]&size=[%22Large%22]&outerFilter=[]&breed_slug=',
	    headers=headers,)
		
		complete_data = response.json()	
		raw_data = complete_data['data']
		results = raw_data['results']
	
		for result in results:
			try:
				dog_breeds = f"dog breed name:{result['breed_name']}, size:{result['size']}, slug:{result['slug']}"
				with open('dog_breed.txt','a') as file:
					dog_breed = file.write(dog_breeds + '\n')
				print('-------------------------------------------')
				print(dog_breeds)
			except Exception as e:
				print(e)

	for i in range(1,20):
		response = requests.get(
	    f'https://api.happypet.care/v1/breed/search-page?page={i}&limit=25&shedding_level=[]&quick_filter=[]&cost_of_buying=[]&temperament_with_dogs=[]&friendliness=[]&size=[%22Giant%22]&outerFilter=[]&breed_slug=',
	    headers=headers,)

		complete_data = response.json()
		raw_data = complete_data['data']
		results = raw_data['results']
	
		for result in results:
			try:
				dog_breeds = f"dog breed name:{result['breed_name']}, size:{result['size']}, slug:{result['slug']}"
				with open('dog_breed.txt','a') as file:
					dog_breed = file.write(dog_breeds + '\n')
				print('-------------------------------------------')
				print(dog_breeds)
			except Exception as e:
				print(e)

def breeds_of_cats():

	for i in range(1,11):
		response = requests.get(
	    f'https://api.happypet.care/v1/breed/cat/search-page?page={i}&limit=25&shedding_level=[]&quick_filter=[]&cost_of_buying=[]&temperament_with_dogs=[]&friendliness=[]&size=[%22Small%22]',
	    headers=headers,)

		complete_data = response.json()
		raw_data = complete_data['data']
		results = raw_data['results']

		for result in results:
			try:
				cat_breeds = f"cat breed name:{result['breed_name']}, size:{result['size']}, slug:{result['slug']}"
				with open('cat_breeds.txt','a') as file:
					cat_breed = file.write(cat_breeds + '\n')
					print('-----------------------------------')
					print('cat_breeds:', cat_breeds)
			except Exception as e:
				print(e)
		
	for i in range(1,11):
		response = requests.get(
	    f'https://api.happypet.care/v1/breed/cat/search-page?page={i}&limit=25&shedding_level=[]&quick_filter=[]&cost_of_buying=[]&temperament_with_dogs=[]&friendliness=[]&size=[%22Medium%22]',
	    headers=headers,)

		complete_data = response.json()
		raw_data = complete_data['data']
		results = raw_data['results']

		for result in results:
			try:
				cat_breeds = f"cat breed name:{result['breed_name']}, size:{result['size']}, slug:{result['slug']}"
				with open('cat_breeds.txt','a') as file:
					cat_breed = file.write(cat_breeds + '\n')
					print('-----------------------------------')
					print('cat_breeds:', cat_breeds)
			except Exception as e:
				print(e)	

	for i in range(1,11):
		response = requests.get(
	    f'https://api.happypet.care/v1/breed/cat/search-page?page={i}&limit=25&shedding_level=[]&quick_filter=[]&cost_of_buying=[]&temperament_with_dogs=[]&friendliness=[]&size=[%22Medium%22]',
	    headers=headers,)

		complete_data = response.json()
		raw_data = complete_data['data']
		results = raw_data['results']

		for result in results:
			try:
				cat_breeds = f"cat breed name:{result['breed_name']}, size:{result['size']}, slug:{result['slug']}"
				with open('cat_breeds.txt','a') as file:
					cat_breed = file.write(cat_breeds + '\n')
					print('-----------------------------------')
					print('cat_breeds:', cat_breeds)
			except Exception as e:
				print(e)

def breeds_of_birds():
	for i in range(1,2):
		response = requests.get(f'https://api.happypet.care/v1/breed/bird/search-page?page={1}&limit=25&shedding_level=[]&quick_filter=[]&cost_of_buying=[]&temperament_with_dogs=[]&friendliness=[]&size=[]',
	    headers=headers,)
		
		complete_data = response.json()
	
		raw_data = complete_data['data']
		results = raw_data['results']
		for result in results:
			try:
				bird_breeds = f"bird breed name: {result['breed_name']}, size: {result['size']}, slug: {result['slug']}"
				with open("birds_breeds.txt",'a') as file:
					bird_breed = file.write(bird_breeds + '\n')
					print("-----------------------------------")
					print("birds_breeds: ",bird_breeds)
			except Exception as e:
				print(e)


# pet_cate = input("which pet you want to know his breeds: dog/cat/bird ")

# if pet_cate == 'dog' or pet_cate == 'Dog':

# elif pet_cate == 'cat' or pet_cate == 'Cat':
	
# elif pet_cate == 'bird' or pet_cate == 'Bird':

	



