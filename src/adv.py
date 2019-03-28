from room import Room
from player import Player
from item import Item
from monster import Monster
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [], []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     [], []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     [], []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     [], []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     [], []),
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
room['outside'].items.append(
    Item("lamp", "This looks like it could be used to see things in the dark."))

room['outside'].items.append(
    Item("shield", "This looks like it could be used to provide some protection."))

room['treasure'].items.append(
    Item("chest", "It's completely empty")
)

room['outside'].monsters.append(
    Monster("Ogre", "Doesn't look very friendly")
)

player = Player(room['outside'], [])

# player.inventory.append(Item("sword", "A rusty old sword"))
player.inventory.append(
    Item("map", "[n] North, [s] South, [e] East, [w] West"))

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
    for monster in player.current_room.monsters:
        print(f"Monsters in room: {monster.name}")
    for item in player.current_room.items:
        print(f"Items in room: {item.name}")
    s = input("\n>").lower().split()

    print(s)

    if len(s) == 1:
        # direction, quit, help, inventory
        s = s[0][0]

        if s == 'q':
            print("Goodbye!")
            break
        elif s == 'h':
            # print("Directions: [n] North, [s] South, [e] East, [w] West")
            print("[i] or Inventory to access your inventory.")
            print("To check an items description put desc followed by the items name (ex. desc sword). You may only check the description of items in your inventory.")
            print('To pickup an item, try take followed by the items name (ex. take dagger). Or to drop, drop followed by the item name (ex. drop dagger).')
        elif s == 'i':
            if len(player.inventory) > 0:
                for item in player.inventory:
                    print(f"Inventory: {item.name}")
            else:
                print("You have no items")

        player.current_room = try_direction(s, player.current_room)

    elif len(s) == 2:
        # two word command, take, drop
        # if first_word in ['take', 'drop']:
        first_word = s[0]
        second_word = s[1]

        if first_word == 'take':
            if len(player.current_room.items) > 0:
                for item in player.current_room.items:
                    if second_word == item.name:
                        player.inventory.append(item)
                        player.current_room.items.remove(item)
                        print(f"You take the {item.name}")
                    else:
                        print("Item does not exist.")
        elif first_word == 'drop':
            if len(player.inventory) > 0:
                for item in player.inventory:
                    if second_word == item.name:
                        player.current_room.items.append(item)
                        player.inventory.remove(item)
                        print(f"You drop the {item.name}")
                    else:
                        print("Item does not exist.")
        elif first_word == 'desc':
            if len(player.inventory) > 0:
                for item in player.inventory:
                    if second_word == item.name:
                        print(f"Item description: {item.description}")
                    else:
                        print("Item does not exist")
        elif first_word == 'attack':
            if len(player.current_room.monsters) > 0:
                for monster in player.current_room.monsters:
                    if second_word == monster.name:
                        print(f"You swing at the {monster.name}")

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
