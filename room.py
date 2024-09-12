class Room:
    def __init__(self, name, description, item=None):
        self.name = name
        self.description = description
        self.item = item
        self.characters = {}
        self.neighbors = {}
    
    def enter(self):
        print(f"You are now in the {self.name}.")
        print(self.description)
        if self.item:
            print(f"There is a {self.item.name} here.")
        if self.characters:
            print("You see:")
            for name in self.characters:
                print(f"- {name}")
    
    def add_character(self, character):
        self.characters[character.name] = character
    
    def get_character(self, name):
        return self.characters.get(name)
    
    def add_neighbor(self, direction, neighbor):
        self.neighbors[direction] = neighbor
