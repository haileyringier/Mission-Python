room_map = [ 
    [1, 0, 0, 0, 0],
    [0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0],
    [0, 0, 0, 0, 4]
]

print(room_map[3][1])

# changing fertilizer to blankets
room_map[0][0] = 5 
print(room_map[0][0])

# changing toothpaste to emergency radio
room_map[4][4] = 6
print(room_map[4][4])
