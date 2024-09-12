class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def talk(self):
        print(f"{self.name}: {self.description}")
