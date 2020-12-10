planets = {
    "Mercury": ["The smallest planet, nearest the Sun", False, 0],
    "Venus": ["Venus takes 243 days to rotate", False, 0],
    "Earth": ["The only planet known to have native life", False, 1],
    "Mars": ["The red planet is the second smallest planet", False, 2],
    "Jupiter": ["The largest planet, Jupiter is a gas gaint", True, 67],
    "Saturn": ["The second largest planet is a gas gaint", True, 62],
    "Uranus": ["An ice giant with a ring system", True, 27],
    "Neptune": ["An ice gaint and farthest from the sun", True, 14],
    "Jakku": ["Home to thieves and outlaws", True, 2]
}

while True: 
    query = input("Which planet would you like information on? ")
    if query in planets.keys():
        print(planets[query][0])
        print("Does it have rings?", planets[query][1])
        print("How many moons does it have?", planets[query][2])
    else: 
        print("No data available, Sorry!")
