import requests
from bs4 import BeautifulSoup
import csv
from tabulate import tabulate

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

        movies.append([title, year, rating])

    return movies

def save_movies_to_csv(movies_data, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        table = tabulate(movies_data, headers=["Title", "Year", "Rating"], tablefmt="pipe")
        writer.writerow([table])

    print(f"Movie data saved to {filename} successfully.")

# Scrape top rated movies and save to CSV
movies_data = scrape_top_rated_movies()
save_movies_to_csv(movies_data, "top_rated_movies.csv")
