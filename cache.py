import requests
from bs4 import BeautifulSoup
import json
import re
import os

def get_movie_details(imdb_id):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    url = f"https://www.imdb.com/title/{imdb_id}/"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    genres = [genre.text.strip() for genre in soup.select(".ipc-chip-list a[href*=genres]")]
    countries = [country.text.strip() for country in soup.select("li.ipc-metadata-list__item a[href*=country_of_origin]")]

    return {
        "genres": genres,
        "countries": countries
    }

json_file = "imdb_top_250.json"

if os.path.exists(json_file):
    with open(json_file, "r") as file:
        movie_data = json.load(file)
else:
    url = "https://www.imdb.com/chart/top/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    movies_table = soup.find("table", class_="chart")
    movies = movies_table.find_all("tr")[1:]

    movie_data = []
    for movie in movies:
        movie_title = movie.find("td", class_="titleColumn").a.text
        movie_year = movie.find("td", class_="titleColumn").span.text.strip("()")
        movie_rating = movie.find("td", class_="ratingColumn imdbRating").strong.text
        movie_imdb_id = movie.find("td", class_="titleColumn").a["href"].split("/")[2]
        movie_director_and_cast = movie.find("td", class_="titleColumn").a["title"].split(", ")
        movie_director = movie_director_and_cast[0].replace(" (dir.)", "")
        movie_cast = movie_director_and_cast[1:]

        movie_details = get_movie_details(movie_imdb_id)

        movie_data.append({
            "title": movie_title,
            "year": movie_year,
            "rating": movie_rating,
            "imdb_id": movie_imdb_id,
            "director": movie_director,
            "cast": movie_cast,
            "genres": movie_details["genres"],
            "countries": movie_details["countries"]
        })

    with open("imdb_top_250.json", "w") as outfile:
        json.dump(movie_data, outfile, indent=4)