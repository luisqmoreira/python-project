# define rooms and items
# Game Room
import pandas as pd
import random
import random
import time

# defining items and rooms
couch = {
    "name": "couch",
    "type": "furniture",
}

table = {
    "name": "table",
    "type": "furniture",
}

toy = {
    "name": "toy",
    "type": "furniture",
}

ping_pong = {
    "name": "ping pong",
    "type": "furniture",
}

door_a = {
    "name": "door a",
    "type": "door",
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

piano = {
    "name": "piano",
    "type": "furniture",
}

game_room = {
    "name": "game room",
    "type": "room",
}

# Bedroom 1

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}

door_b = {
    "name": "door b",
    "type": "door",
}
door_c = {
    "name": "door c",
    "type": "door",
}

closet = {
    "name": "closet",
    "type": "furniture",
}

secretary = {
    "name": "secretary",
    "type": "furniture",
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}
bedroom_1 = {
    "name": "Bedroom 1",
    "type": "room",
}

# Bedroom 2

double_bed = {
    "name": "double bed",
    "type": "furniture",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}

mirror = {
    "name": "mirror",
    "type": "furniture",
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}

door_d = {
    "name": "door d",
    "type": "door",
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}

bedroom_2 = {
    "name": "Bedroom 2",
    "type": "room",
}
# Living Room


living_room = {
    "name": "Living Room",
    "type": "room",
}
dining_table = {
    "name": "Dining Table",
    "type": "furniture",
}

# Outside
outside = {
    "name": "outside",
    'type': 'room',
}

all_rooms = [game_room, bedroom_1, bedroom_2, living_room, outside]

all_doors = [door_a, door_b, door_c, door_d]

# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, table, ping_pong, toy, door_a],
    "piano": [key_a],
    "outside": [door_d],
    'door d': [living_room, outside],
    'door a': [game_room, bedroom_1],
    'Bedroom 1': [queen_bed, closet, secretary, door_a, door_b, door_c],
    'queen bed': [key_b],
    'door b': [bedroom_1, bedroom_2],
    'Bedroom 2': [double_bed, dresser, mirror, door_b],
    'double bed': [key_c],
    'dresser': [key_d],
    'door c': [bedroom_1, living_room],
    'Living Room': [dining_table, door_d]
}

# define game state. Do not directly change this dict.
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}
# placeholder variable used in examine_item function
tries = 0


def challenge():
    # play quiz, shows up whenever you try to move to the next room after unlocking the door.
    # it will randomly select one from a list of question
    # If you fail it will select another question until you get it right

    d = {"What's the capital of Venezuela - Buenos Aires, Lima or Caracas?": "Caracas",
         "What's the name of the first Imperator of Rome? - Julius Cesar, Cesar Augustus or Romulus Augustus?": "Cesar Augustus",
         "In what what year did the french revolution took place? - 1769, 1815 or 1789": "1789",
         "How old was Elvis Presley when he died? - 46, 44 or 42": "42",
         "How many planets are there in the solar system? - 10, 9, or 8": "8",
         "How many countries are there today in the European Union? - 28, 27, 29": "27",
         "What's the longest river in the world? - Amazon, Yangtze or Nile": "Nile",
         "who was the 42nd president of the United States of America? - George Bush, Bill Clinton or Donald Trump": "Bill Clinton",
         "In what year did World War II ended? - 1939, 1953 or 1945": "1945",
         "When was Einestein born? - 1889, 1879, 1881": "1879"
         }

    k, v = random.choice(list(d.items()))

    print("In order to move to the next room you have to pass a challenge! Answer the following question: ")
    print(k)

    answer = input("Pick an answer: ")

    while True:

        if answer.upper() == v.upper():
            break
        else:
            print("Wrong Answer! Let´s try another challenge!")
            k, v = random.choice(list(d.items()))
            print(k)
            answer = input("Pick an answer:")

def linebreak():
    """
    Print a line break
    """
    print("\n\n")


def start_game():
    """
    Start the game
    """
    print(
        "You wake up on a couch and find yourself in a strange house with no windows which you have never been to "
        "before. You don't remember why you are here and what had happened before. You feel some unknown danger is "
        "approaching and you must get out of the house, NOW!")
    play_room(game_state["current_room"])


def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if game_state["current_room"] == game_state["target_room"]:
        print("Congrats! You escaped the room!")
    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type '1' to explore or '2' to examine ").strip()
        if intended_action == "1":
            explore_room(room)
            play_room(room)
        elif intended_action == "2":
            examine_item(input("What would you like to examine? ").strip())
            if tries == 3:
                return print('You lost')

        else:
            print("Not sure what you mean. Type '1' to explore or '2' to examine ")
            play_room(room)
        linebreak()


def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))


def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if not current_room == room:
            return room


def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    # global used to bring the value outside, otherwise it will reset everytime the function runs
    global tries
    current_room = game_state["current_room"]
    next_room = ""
    output = None

    # limits the tries to 2, tries are the number of times you can examine items before you find the keys
    if tries < 2:
        for item in object_relations[current_room["name"]]:
            if (item["name"] == item_name):
                output = "You examine " + item_name + ". "
                if (item["type"] == "door"):
                    have_key = False
                    for key in game_state["keys_collected"]:
                        if key["target"] == item:
                            have_key = True
                    if (have_key):
                        output += "You unlock it with a key you have."
                        next_room = get_next_room_of_door(item, current_room)
                    else:
                        output += "It is locked but you don't have the key."
                else:
                    if item["name"] in object_relations and len(object_relations[item["name"]]) > 0:
                        item_found = object_relations[item["name"]].pop()
                        game_state["keys_collected"].append(item_found)
                        output += "You find " + item_found["name"] + "."
                    else:
                        output += "There isn't anything interesting about it."
                        tries = tries + 1

                print(output)
                break
    else:
        # if tries are exceeded it will return a message communicating to the player that he lost, reset the tries to 0 and restart the game
        print('You lost! Try again')
        tries = 0
        return play_room(game_room)

    if (output is None):
        print("The item you requested is not found in the current room.")

    if (next_room and input("Do you want to go to the next room? Enter 'yes' or 'no' ").strip() == 'yes'):
        challenge()
        play_room(next_room)
    else:
        play_room(current_room)






game_state = INIT_GAME_STATE.copy()

# Player will be prompted to input its name before starting game
player_name = input('Write your name ')


# time_start begins counting the time when the player begins the game
time_start = time.time()
start_game()

# time_ends when the player passes the last door and finishes the game
time_passed = time.time() - time_start


# if time is less than 100 seconds it will return you're good else 'you can do this better
if (time.time() - time_start) <= 100.0:
    print("you are good 😊")
else:
    (time.time() - time_start) >= 100.0
    print("you can do this better 😑")


# Returns player name with the result in seconds
print(str(player_name) + ' you finished the game in ' + str(round((time_passed), 2)) + 'seconds')

# generates and saves a file in txt with the player's name and time
ranking_table = open('standings ' + str(player_name) + '.txt', 'w')

with  ranking_table:
    ranking_table.write(player_name + ' ' + str(time_passed) + '\n')

