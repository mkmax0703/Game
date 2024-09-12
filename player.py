class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.inventory = []
        self.puzzle_solved = False  # Track puzzle completion

    def move(self, direction):
        if direction in self.current_room.neighbors:
            self.current_room = self.current_room.neighbors[direction]
        else:
            print("You can't go that way.")

    def take_item(self):
        if self.current_room.item:
            self.inventory.append(self.current_room.item)
            print(f"Item {self.current_room.item.name} taken.")
            self.current_room.item = None  # Remove the item from the room after taking
        else:
            print("No item to take.")

    def assemble_puzzle(self):
        if len(self.inventory) >= 3:  # All pieces collected
            self.puzzle_solved = True
            print("Puzzle solved!")
        else:
            print("You need more pieces to assemble the puzzle.")
