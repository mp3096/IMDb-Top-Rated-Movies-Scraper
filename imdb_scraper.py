import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_top_rated_movies():
    url = "https://www.imdb.com/chart/top"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    movie_elements = soup.select("td.titleColumn")
    ratings_elements = soup.select("td.imdbRating strong")

    movies = []
    for movie, rating in zip(movie_elements, ratings_elements):
        title = movie.a.text
        year = movie.span.text.strip("()")
        rating = rating.text.strip()

        movies.append({
            "Title": title,
            "Year": year,
            "Rating": rating
        })

    return movies

def save_movies_to_csv(movies_data, filename):
    df = pd.DataFrame(movies_data)
    df.to_csv(filename, index=False)
    print(f"Movie data saved to {filename} successfully.")

# Scrape top rated movies and save to CSV
movies_data = scrape_top_rated_movies()
save_movies_to_csv(movies_data, "top_rated_movies.csv")
