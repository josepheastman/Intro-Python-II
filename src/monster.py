class Monster:
    def __init__(self, name, description, health=10):
        self.name = name
        self.description = description
        self.health = health

    def __repr__(self):
        return f"{self.name}, {self.description}"
