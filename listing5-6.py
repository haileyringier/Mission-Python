import time, random, math

# VARIABLES 

WIDTH = 800
HEIGHT = 800

PLAYER_NAME = "Hailey"
FRIEND1_NAME = "Kevin"
FRIEND2_NAME = "Korra"
current_room = 31

top_left_x = 100
top_left_y = 150

DEMO_OBJECTS = [images.floor, images.pillar, images.soil]

LANDER_SECTOR = random.randint(1, 24)
LANDER_X = random.randint(2, 11)
LANDER_Y = random.randint(2, 11)

MAP_WIDTH = 5
MAP_HEIGHT = 10
MAP_SIZE = MAP_WIDTH * MAP_HEIGHT

objects = {
    0: [images.floor, None, "The floor is shiny and clean"],
    1: [images.pillar, images.full_shadow, "the wall is smooth and cold"],
    2: [images.soil, None, "It's like a desert. Or should that be dessert?"],
    3: [images.pillar_low, images.half_shadow, "The wall is smooth and cold"],
    4: [images.bed, images.half_shadow, "A tidy and comfortable bed"],
    5: [images.table, images.half_shadow, "It's made from strong plastic."],
    6: [images.chair_left, None, "A chair with a soft cushion"],
    7: [images.chair_right, None, "A chair with a soft cushion"],
    8: [images.bookcase_tall, images.full_shadow, "Bookshelves, stacked with reference books"],
    9: [images.bookcase_small, images.half_shadow, "Bookshelves, stacked with reference books"],
    10: [images.cabinet, images.half_shadow, "A small locker, for storing personal items"],
    11: [images.desk_computer, images.half_shadow, "A computer. Use it to run life support diagnostics"],
    12: [images.plant, images.plant_shadow, "A spaceberry plant, grown here"],
}

GAME_MAP = [
    ["Room 0 - where unused objects are kept", 0, 0, False, False]
]

outdoor_rooms = range(1, 26)
for planetsectors in range(1, 26):
    GAME_MAP.append(["The dusty planet surface", 13, 13, True, True])

GAME_MAP += [ 
    ["The airlock", 13, 5, True, False], # room 26
    ["The engineering lab", 13, 13, False, False], # room 27
    ["Poodle Mission Control", 9, 13, False, True], # room 28
    ["The viewing gallery", 9, 15, False, False], # room 29
    ["The crew's bathroom", 5, 5, False, False], # room 30
    ["The airlock entry bay", 7, 11, True, True], # room 31
    ["Left elbow room", 9, 7, True, False], # room 32
    ["Right elbow room", 7, 13, True, True], # room 33
    ["The science lab", 13, 13, False, True], # room 34
    ["The greenhouse", 13, 13, True, False], # room 35
    [PLAYER_NAME + "'s sleeping quarters", 9, 11, False, False], # room 36
    ["West corridor", 15, 5, True, True], # room 37
    ["The briefing room", 7, 13, False, True], # room 38
    ["The crew's community room", 11, 13, True, False], # room 39
    ["Main Mission Control", 14, 14, False, False], # room 40
    ["The sick bay", 12, 7, True, False], # room 41
    ["West corridor", 9, 7, True, False], # room 42
    ["Utilities control room", 9, 9, False, True], # room 43
    ["Systems engineering bay", 9, 11, False, False], # room 44
    ["Security portal to Mission Control", 7, 7, True, False], # room 45
    [FRIEND1_NAME + "'s sleeping quarters", 9, 11, True, True], # room 46
    [FRIEND2_NAME + "'s sleeping quarters", 9, 11, True, True], # room 47
    ["The pipeworks", 13, 11, True, False], # room 48
    ["The chief scientist's office", 9, 7, True, True], # room 49
    ["The robot workshop", 9, 11, True, False] # room 50
]

# test to ensure the number of rooms we created matches our map size
assert len(GAME_MAP) - 1 == MAP_SIZE, "Map size and GAME_MAP do not match!"

#begining of 4-2 

def get_floor_type():
    if current_room in outdoor_rooms:
        return 2 # soil 
    else: 
        return 0 # tile

def generate_map():
    global room_map, room_width, room_height, room_name, hazard_map
    global top_left_x, top_left_y, wall_transparency_frame
    room_data = GAME_MAP[current_room]
    room_name = room_data[0]
    room_height = room_data[1]
    room_width = room_data[2]

    floor_type = get_floor_type()
    if current_room in range(1, 21):
        bottom_edge = 2
        side_edge = 2
    if current_room in range(21, 26):
        bottom_edge = 1
        side_edge = 2 
    if current_room > 25:
        bottom_edge = 1
        side_edge = 1

    room_map=[[side_edge] * room_width]

    for y in range(room_height - 2):
        room_map.append([side_edge] + [floor_type]*(room_width - 2) + [side_edge])
    
    room_map.append([bottom_edge] * room_width)

    middle_row = int(room_height / 2)
    middle_column = int(room_width / 2)

    if room_data[4]:
        room_map[middle_row][room_width - 1] = floor_type
        room_map[middle_row + 1][room_width - 1] = floor_type
        room_map[middle_row - 1][room_width - 1] = floor_type

    if current_room % MAP_WIDTH != 1:
        room_to_left = GAME_MAP[current_room - 1]
        if room_to_left[4]:
            room_map[middle_row][0] = floor_type
            room_map[middle_row + 1][0] = floor_type
            room_map[middle_row - 1][0] = floor_type

    if room_data[3]:
        room_map[0][middle_column] = floor_type
        room_map[0][middle_column + 1] = floor_type
        room_map[0][middle_column - 1] = floor_type

    if current_room <= MAP_SIZE - MAP_WIDTH:
        room_below = GAME_MAP[current_room + MAP_WIDTH]
        if room_below[3]:
            room_map[room_height - 1][middle_column] = floor_type
            room_map[room_height - 1][middle_column + 1] = floor_type
            room_map[room_height - 1][middle_column - 1] = floor_type


def draw():
    global room_height, room_width, room_map
    print(current_room)
    generate_map()
    screen.clear()
    room_map[2][4] = 7
    room_map[2][6] = 6
    room_map[1][1] = 8
    room_map[1][2] = 9
    room_map[1][8] = 12
    room_map[1][9] = 9

    for y in range(room_height):
        for x in range(room_width):
            image_to_draw = objects[room_map[y][x]][0]
            screen.blit(image_to_draw,
            (top_left_x + (x * 30), 
            top_left_y + (y * 30) - image_to_draw.get_height()))

def movement():
    global current_room
    old_room = current_room

    if keyboard.left:
        current_room -= 1
    if keyboard.right:
        current_room += 1
    if keyboard.up:
        current_room -= MAP_WIDTH
    if keyboard.down:
        current_room += MAP_WIDTH

    if current_room > 50:
        current_room = 50
    if current_room < 1:
        current_room = 1

    if current_room != old_room:
        print("Entering room:" + str(current_room))

clock.schedule_interval(movement, 0.1)