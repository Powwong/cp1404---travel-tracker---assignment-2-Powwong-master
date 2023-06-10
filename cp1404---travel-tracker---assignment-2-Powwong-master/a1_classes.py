"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

import csv
import random
from operator import itemgetter

filename = 'places.csv'



class Place:
    """Parent class for travel tracker, places to visit"""

    def __init__(self, name="", country="", priority=0, is_visited=False):
        """Assign values to the object attributes."""
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def mark_visited(self):
        """Mark place as visited."""
        self.is_visited = True

    def mark_unvisited(self):
        """Mark place as unvisited"""
        self.is_visited = False

    def __str__(self):
        """Format the objects and neatly display them."""
        if self.is_visited is True:
            status = "(visited)"
        else:
            status = ""
        return f" {self.name} in {self.country}, priority {self.priority} {status}"

    def is_important(self):
        return self.priority <= 2


def save_places(places):
    """Save places to csv file"""
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for place in places:
                writer.writerow(place)
    except Exception as e:
        print("Error while saving: ", e)


def print_menu():
    print("Menu:")
    print("L - List places")
    print("R - Recommend random place")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("Q - Quit")


def list_places(places):
    """Print places in the list"""
    places.sort(key=itemgetter(2, 1))
    places.reverse()
    places.sort(key=itemgetter(3))
    for i, place in enumerate(places, 1):
        visited = "*" if place[3] == "n" else ""
        print(f"{visited}{i}. {place[0]} in {place[1]} {place[2]}")
    print(f"{len(places)} places. You still want to visit {sum(1 for p in places if p[3] == 'n')} places.")


def recommend_place(places):
    """Recommend a random place that has not been visited"""
    unvisited = [p for p in places if p[3] == "n"]
    if unvisited:
        recommendation = random.choice(unvisited)
        print(f"Not sure where to visit next?\nHow about... {recommendation[0]} in {recommendation[1]}?")
    else:
        print("No places left to visit!")


def add_place(places):
    """Add a new place to the list"""
    name = input("Name: ").strip()
    while not name:
        print("Input cannot be blank")
        name = input("Name: ").strip()
    country = input("Country: ").strip()
    while not country:
        print("Input cannot be blank")
        country = input("Country: ").strip()
    priority = input("Priority: ").strip()
    while not priority.isdigit():
        print("Priority should be a number.")
        priority = input("Priority: ").strip()
    places.append([name, country, priority, "n"])
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker")


def mark_place(places):
    """Mark a place as visited"""
    list_places(places)
    try:
        place_num = int(input("Enter the number of a place to mark as visited: "))
        while place_num <= 0 or place_num > len(places):
            print("Invalid place number")
            place_num = int(input("Enter the number of a place to mark as visited: "))
        place = places[place_num - 1]
        if place[3] == "n":
            place[3] = "v"
            print(f"{place[0]} in {place[1]} visited!")
        else:
            print("You have already visited", place[0])
    except ValueError:
        print("Invalid input; enter a valid number")


def main():
    places = load_places()
    while True:
        print_menu()
        choice = input(">>> ").upper()
        if choice == "L":
            list_places(places)
        elif choice == "R":
            recommend_place(places)
        elif choice == "A":
            add_place(places)
        elif choice == "M":
            if any(p[3] == "n" for p in places):
                mark_place(places)
            else:
                print("All places have been visited!")
        elif choice == "Q":
            save_places(places)
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")


if __name__ == "__main__":
    main()

