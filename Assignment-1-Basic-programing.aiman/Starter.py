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


# =========================
# YOUR PART (ADD MOVIE)
# =========================
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


# =========================
# YOUR PART (VIEW MOVIES)
# =========================
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


# =========================
# PARTNER CAN IMPROVE THIS
# =========================
def search_movie():
    print("\n--- Search Movie ---")
    search_query = input("Enter movie title: ")

    found = False

    for movie in movies:
        if search_query.lower() == movie['title'].lower():
            print("\nMovie Found!")
            print(f"Title: {movie['title']}")
            print(f"Genre: {movie['genre']}")
            print(f"Rating: {movie['rating']}")
            found = True
            break

    if not found:
        print("Movie not found.")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_movie()

        elif choice == "2":
            view_movies()

        elif choice == "3":
            search_movie()

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()