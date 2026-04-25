# CBMM 2013 - Assignment 1
# Movie Collection Manager

# Global list to store movie dictionaries
movies = [
    {"title": "Avengers: Endgame", "genre": "Action", "rating": 9.0},
    {"title": "Titanic", "genre": "Romance", "rating": 8.5},
    {"title": "The Conjuring", "genre": "Horror", "rating": 7.8},
    {"title": "Inception", "genre": "Sci-Fi", "rating": 9.2},
    {"title": "Frozen", "genre": "Animation", "rating": 7.5}
]

def show_menu():
    print("\n======= Movie Collection Manager =======")
    print("1. Add movie")
    print("2. View movies")
    print("3. Search movie")
    print("4. Exit")


# ==========================================
# AIMAN'S PART (ADD MOVIE)
# ==========================================
def add_movie():
    print("\n--- Add New Movie ---")
    
    title = input("Enter movie title: ")
    genre = input("Enter genre: ")

    # Input validation for rating
    while True:
        try:
            rating = float(input("Enter rating (1-10): "))
            if 1 <= rating <= 10:
                break
            else:
                print("Rating must be between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")

    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }

    movies.append(new_movie)
    print(f"'{title}' has been added successfully!")


# ==========================================
# AIMAN'S PART (VIEW MOVIES)
# ==========================================
def view_movies():
    print("\n--- All Movies ---")

    if not movies:
        print("Your collection is currently empty.")
        return

    print("\nMovie List:")
    print("------------------------")

    for index, movie in enumerate(movies, start=1):
        print(f"{index}. Title: {movie['title']}")
        print(f"   Genre: {movie['genre']}")
        print(f"   Rating: {movie['rating']}")
        print("------------------------")


# ==========================================
# AFIQ'S PART (SEARCH MOVIE & EXIT LOGIC)
# ==========================================
def search_movie():
    print("\n--- Search Movie ---")
    search_query = input("Enter movie title (or part of it): ").strip().lower()

    if not search_query:
        print("Search query cannot be empty.")
        return

    results = []

    # Searching for partial matches to make the tool more user-friendly
    for movie in movies:
        if search_query in movie['title'].lower():
            results.append(movie)

    if results:
        print(f"\nFound {len(results)} matching movie(s):")
        print("------------------------")
        for movie in results:
            print(f"Title: {movie['title']}")
            print(f"Genre: {movie['genre']}")
            print(f"Rating: {movie['rating']}")
            print("------------------------")
    else:
        print(f"No movies found matching '{search_query}'.")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_movie()

        elif choice == "2":
            view_movies()

        elif choice == "3":
            search_movie()

        elif choice == "4":
            print("\nExiting Movie Collection Manager. Data saved for this session.")
            print("Thank you for using the system. Goodbye!")
            break

        else:
            print("\n[!] Invalid option. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()