import random

# Read the movies from the file, specifying the encoding
with open("movies.txt", "r", encoding="utf-8") as f:
    movies = f.readlines()

# Ask the user for their preference
choice = input("Are you ready for a random movie recommendation or from a specific year? Input 'random' or 'year' to get a recommendation: ")

# Generate a random recommendation or ask for a year
if choice.lower() == "random":
    movie = random.choice(movies)
    print("You should watch:", movie)
elif choice.lower() == "year":
    year = input("What year are you interested in? ")
    matching_movies = [m for m in movies if year in m]
    if not matching_movies:
        print("No movies found for that year.")
    else:
        movie = random.choice(matching_movies)
        print("You should watch:", movie)
else:
    print("Invalid choice.")
