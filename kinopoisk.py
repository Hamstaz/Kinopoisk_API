import requests
import json
import textwrap

token = "ZQQ8GMN-TN54SGK-NB3MKEC-ZKB8V06"

# Загружаем требования к поиску
with open('config.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

type = data["Search"]["type"]
year = data["Search"]["year"]
rating = data["Search"]["rating"]
sort_year = data["Sorting"]["release_year"]
sort_rate = data["Sorting"]["kinopoisk_rating"]

url = f"https://api.kinopoisk.dev/movie?field=rating.kp&search={rating}&field=year&search={year}&field=type&search={type}&token={token}&sortField=year&sortType={sort_year}&sortField=rating.kp&sortType={sort_rate}"

response = requests.get(url)
search_results = json.loads(response.text)

for result in search_results["docs"]:
    name = result["name"]
    kp = result["rating"]["kp"]
    imdb = result["rating"]["imdb"]
    year = result["year"]
    description = result["description"]
    try:
        wrapped_description = textwrap.fill(description, width=120)
    except:
        description = ""
    print("Название:", name)
    print("Год премьеры:", year)
    print("Рейтинг КП:", kp)
    print("Рейтинг IMDB:", imdb)
    print("Описание:", wrapped_description, '\n')


