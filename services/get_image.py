import requests


# Получение фото рандомного кота (в случае неудачи - собаки)
def get_new_image():
    try:
        response = requests.get('https://api.thecatapi.com/v1/images/search')
    except Exception as error:
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)
    response = response.json()
    random_cat = response[0].get('url')
    return random_cat
