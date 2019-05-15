# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room, inv):
        self.current_room = current_room
        self.inv = []

    def __repr__(self):
        return f"Player is in {self.current_room}"
