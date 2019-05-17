
from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("sword", "This sword has a blade of a copper color."), Item("lantern", "It shines brightly.")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("helm", "This looks like it could provide some protection for your head.")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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
# room['outside'].items.append(
#     Item("sword", "This sword has a blade of a copper color, styled to resemble a fang. The guard is a pair of bird wings."))

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'], [])

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


def move_direction(direction, current_room):
    attribute = direction + '_to'

    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)
    else:
        print("You can't move in that direction!")
        return current_room


while True:
    print(player.current_room.name)
    print(player.current_room.description)
    if player.current_room.items != []:
        print(f'In the room you see: {player.current_room.items}')
    elif player.current_room.items == []:
        print("You see no items of interest here.")
    d = input("\n>").lower().split()

    if len(d) == 1:
        d = d[0][0]
        player.current_room = move_direction(d, player.current_room)

        if d == 'q':
            print("Goodbye!")
            break
        elif d == 'i' or d == 'inventory':
            if len(player.inv) > 0:
                print(f'Inventory: {player.inv}')

    elif len(d) == 2:
        if d[0] == 'take' or d[0] == 'get':
            if len(player.current_room.items) > 0:
                for item in player.current_room.items:
                    if d[1] == item.name:
                        player.inv.append(item)
                        player.current_room.items.remove(item)
                        item.on_take()
                    else:
                        print("There is no item with that name.")
        elif d[0] == 'drop':
            if len(player.inv) > 0:
                for item in player.inv:
                    if d[1] == item.name:
                        player.current_room.items.append(item)
                        player.inv.remove(item)
                        item.on_drop()
