# CBMM 2013 - Assignment 1
# Movie Collection Manager (Starter Template)
# Lecturer: Mohd Faiz bin Alias

movies = []

# Example movie structure:
# {"title": "Movie Name", "genre": "Genre", "rating": "8"}

def show_menu():
    print("\nMovie Collection Manager")
    print("1. Add movie")
    print("2. View movies")
    print("3. Search movie")
    print("4. Exit")

def add_movie():
    # TODO: ask user for title, genre and rating
    # TODO: store the movie in the movies list
    pass


def view_movies():

    # Debugging task: check why the program crashes when the list is empty
    if movies == "":
        print("No movies available")

    # TODO: display all movies stored in the list
    pass


def search_movie():
    # TODO: ask user for movie title
    # TODO: search movie in the list
    # TODO: display result
    pass


def main():
    while True:
        show_menu()
        choice = input("Choose option: ")

        if choice == "1":
            add_movie()

        elif choice == "2":
            view_movies()

        elif choice == "3":
            search_movie()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


main()
