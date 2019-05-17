# Implement a class to hold room information. This should have name and
# description attributes..


class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.items = items
        self.description = description

    def __repr__(self):
        return f"{self.name}, {self.description}"
