#!/usr/bin/env python3

import csv
import os.path

FILENAME = "movies.csv"

# -------------Program works only if file already exists----------------


def display_movies():
 #   if not os.path.exists(FILENAME):
 #       print(f"No movies are in '{FILENAME}' yet.")
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[0] + " (" + row[1] + ")")
            print()
    except OSError:
        print(f"File '{FILENAME}' doesn't exist yet.")


def write_file(movies):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(movies)


def read_movies():
    movies = []
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
            return movies
    except FileNotFoundError as e:
        return movies
    except OSError:
        print(f"File '{FILENAME}' doesn't exist yet.")


def add_movie(movies):
    new_movie = []
    movie = input("Enter movie: ")
    year = input("Enter year:  ")
    new_movie.append(movie)
    new_movie.append(year)
    movies.append(new_movie)
    write_file(movies)
    print("Movie was added.")


def delete_movie(movies):
#    if not os.path.exists(FILENAME):
#        print(f"No movies are in '{FILENAME}' yet.")
#    else:
    length_counter = 0
    movie = input("Enter name of movie to delete: ")
    for m in movies:
        if m[0].lower() == movie.lower():
            movies.remove(m)
            print("Movie deleted successfully.")
            write_file(movies)
            break
        else:
            length_counter += 1
            if length_counter == len(movies):
                print("Movie not found.")


def display_menu():
    print("-----The Movie List Program-----")
    print("view - View the movie list")
    print("add  - Add to the movie list")
    print("del  - Delete a movie from the list")
    print("exit - Exit the program")
    print("--------------------------------")


def main():
    display_menu()
    movies = read_movies()
    print()
    while True:
        choice = input("Enter a command: ")
        if choice.lower() == "view":
            display_movies()
        elif choice.lower() == "add":
            add_movie(movies)
        elif choice.lower() == "del":
            delete_movie(movies)
        elif choice.lower() == "exit":
            break
        else:
            print("Invalid command. Try again.")

    print("Goodbye.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
