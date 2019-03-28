from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     []),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'], [])

# current_room = player.current_room
# room_name = player.current_room.name
# room_description = player.current_room.description
# room_items = room.items


def try_direction(direction, current_room):
    attribute = direction + '_to'

    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)
    else:
        print("You can't move in that direction!")
        return current_room

    # Write a loop that:
    #
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.


print('Type [h] or help for additional information.')
while True:
    print(player.current_room.name)
    print(player.current_room.description)
    s = input("\n>").lower().split()

    print(s)

    if len(s) == 1:
        # direction
        s = s[0][0]

        if s == 'q':
            print("Goodbye!")
            break
        elif s == 'h':
            print("Directions: [n] North, [s] South, [e] East, [w] West")
            print('To pickup an item, try take followed by the items name (ex. take dagger). Or to drop, drop followed by the item name (ex. drop dagger).')

        player.current_room = try_direction(s, player.current_room)

    elif len(s) == 2:
        # two word command
        first_word = s[0]
        second_word = s[1]

        # if first_word in ['take', 'drop']:

    else:
        print("Please give a valid response")
        continue

        # print(textwrap.fill(f'Location: {room_name}'))
        # print(f'{room_description}')
        # print(f'{room_items}')
        # print('Please choose a direction')
        # direction = input('\n[n] North [s] South [e] East [w] West:')

        # while True:
        #     if direction == 'n':
        #         player.current_room = player.current_room.n_to
        #     elif direction == 's':
        #         player.current_room = player.current_room.s_to
        #     elif direction == 'e':
        #         cplayer.current_room = player.current_room.e_to
        #     elif direction == 'w':
        #         player.current_room = player.current_room.w_to
        #     elif direction == 'q':
        #         print('Goodbye!')
        #         break
        #     else:
        #         print("You can't move in that direction!")
