from pyvirtualdisplay import Display
import tkinter as tk
from player import Player
from room import Room
from character import Character
from puzzle_piece import PuzzlePiece

# Start a virtual display
display = Display(visible=0, size=(800, 600))
display.start()

# Create puzzle pieces
piece1 = PuzzlePiece("L-Shaped Piece", [
    ['X', ' '],
    ['X', ' '],
    ['X', 'X']
])

piece2 = PuzzlePiece("Square Piece", [
    ['X', 'X'],
    ['X', 'X']
])

piece3 = PuzzlePiece("T-Shaped Piece", [
    [' ', 'X', ' '],
    ['X', 'X', 'X']
])

# Create rooms
living_room = Room("Living Room", "A cozy living room.", piece1)
kitchen = Room("Kitchen", "A clean kitchen.", piece2)
bedroom = Room("Bedroom", "A small bedroom with a bed and a table.", piece3)

# Create characters
dealer = Character("Dealer", "A mysterious man with cards in hand.")
friend = Character("Friend", "Your old friend who knows the casino well.")

# Add characters to rooms
living_room.add_character(dealer)
kitchen.add_character(friend)

# Create player
player = Player("Hero", starting_room=living_room)

# Create a map (adjacent rooms)
living_room.add_neighbor("north", kitchen)
kitchen.add_neighbor("south", living_room)
kitchen.add_neighbor("east", bedroom)
bedroom.add_neighbor("west", kitchen)

# Game GUI Setup
class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Adventure Game")

        self.room_label = tk.Label(root, text="", font=("Arial", 14))
        self.room_label.pack(pady=10)

        self.desc_label = tk.Label(root, text="", wraplength=300)
        self.desc_label.pack(pady=10)

        self.inventory_label = tk.Label(root, text="Inventory: ")
        self.inventory_label.pack(pady=10)

        self.create_buttons()

        # Display the starting room
        self.update_room()

    def create_buttons(self):
        # Directional buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="North", command=lambda: self.move_player("north")).grid(row=0, column=1)
        tk.Button(button_frame, text="South", command=lambda: self.move_player("south")).grid(row=2, column=1)
        tk.Button(button_frame, text="East", command=lambda: self.move_player("east")).grid(row=1, column=2)
        tk.Button(button_frame, text="West", command=lambda: self.move_player("west")).grid(row=1, column=0)

        # Interaction buttons
        tk.Button(self.root, text="Look", command=self.look).pack(pady=5)
        tk.Button(self.root, text="Take Piece", command=self.take_item).pack(pady=5)
        tk.Button(self.root, text="Assemble Puzzle", command=self.open_puzzle_window).pack(pady=5)
        tk.Button(self.root, text="Quit", command=self.root.quit).pack(pady=5)

    def move_player(self, direction):
        player.move(direction)
        self.update_room()

    def look(self):
        self.update_room()

    def take_item(self):
        player.take_item()
        self.update_inventory()

    def update_room(self):
        self.room_label.config(text=f"You are in the {player.current_room.name}")
        self.desc_label.config(text=player.current_room.description)
        self.update_inventory()

    def update_inventory(self):
        inventory_text = "Inventory: " + ", ".join([item.name for item in player.inventory]) if player.inventory else "Inventory: (empty)"
        self.inventory_label.config(text=inventory_text)

    def open_puzzle_window(self):
        if len(player.inventory) < 3:
            tk.messagebox.showinfo("Puzzle", "You don't have all the puzzle pieces yet.")
        else:
            self.show_puzzle_popup()

    def show_puzzle_popup(self):
        puzzle_window = tk.Toplevel(self.root)
        puzzle_window.title("Puzzle Assembly")
        
        for piece in player.inventory:
            piece.display()

        label = tk.Label(puzzle_window, text="You solved the puzzle!")
        label.pack(pady=20)
        
        # Once the puzzle is opened, assume it's solved for simplicity
        player.assemble_puzzle()

# Initialize the game window
root = tk.Tk()
game_gui = GameGUI(root)
root.mainloop()

# Stop the virtual display after the game ends
display.stop()
