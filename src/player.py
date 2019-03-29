# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room, inventory):
        self.current_room = current_room
        self.inventory = []

    def __repr__(self):
        return f"Player is in {self.current_room}"
