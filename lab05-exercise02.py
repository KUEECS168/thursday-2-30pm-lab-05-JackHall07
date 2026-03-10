'''
Author: Jack Halligan
KUID: 3195571
Date: 3/6/26
Lab: lab05
Last modified: 3/6/26
Purpose: Exercise 2 Lab 5
'''


planets = []

while True:
    planet = input("Enter planet name: ")
    planets.append(planet)
    done = input("Is the mission over? (y/n): ")

    if done.lower() == "y":
        break

search = input("Which planet do you want the neighbors for?: ")

print("Planets neighboring " + search + ":")

for i in range(len(planets)):
    if planets[i].lower() == search.lower():
        if i - 1 >= 0:
            print("     " + planets[i - 1])
        if i + 1 < len(planets):
            print("     " + planets[i + 1])

print("Ship crashing...na, program ending")
