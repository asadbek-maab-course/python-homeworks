import requests
import random
from apikey import MOVIE_API_KEY

MOVIE_API_KEY = "YOUR_API_KEY_HERE"
URL = "https://api.themoviedb.org/3"

def get_genres():
    url = f"{URL}/genre/movie/list"
    params = {"api_key": MOVIE_API_KEY, "language": "en-US"}
    response = requests.get(url, params=params)
    response.raise_for_status()
    genres = response.json().get("genres", [])
    return {genre["name"].lower(): genre["id"] for genre in genres}

def get_movies_by_genre(genre_id, page=1):
    url = f"{URL}/discover/movie"
    params = {
        "api_key": MOVIE_API_KEY,
        "language": "en-US",
        "sort_by": "popularity.desc",
        "with_genres": genre_id,
        "page": page
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def main():
    print("Getting genres...")
    genres = get_genres()

    print("\ngenres:")
    for genre_name in genres:
        print(f"- {genre_name.capitalize()}")

    user_input = input("\nEnter a movie genre: ").strip().lower()
    if user_input not in genres:
        print("genre not found.")
        return

    genre_id = genres[user_input]
    
    page = random.randint(1, 5)
    movies_data = get_movies_by_genre(genre_id, page=page)

    movies = movies_data.get("results", [])
    if not movies:
        print("movies not found with this genre.")
        return

    movie = random.choice(movies)
    print("\nMovie Recommendation:")
    print(f"Title: {movie['title']}")
    print(f"Overview: {movie['overview']}")
    print(f"Rating: {movie['vote_average']} / 10")

if __name__ == "__main__":
    main()
