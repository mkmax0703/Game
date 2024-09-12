from flask import Flask, render_template, redirect, url_for
from player import Player
from room import Room
from character import Character
from puzzle_piece import PuzzlePiece

app = Flask(__name__)

# Define Tetris-like puzzle pieces
piece1 = PuzzlePiece("L-Shaped Piece", [
    [1, 0],
    [1, 0],
    [1, 1]
])

piece2 = PuzzlePiece("T-Shaped Piece", [
    [0, 1, 0],
    [1, 1, 1]
])

piece3 = PuzzlePiece("Square Piece", [
    [1, 1],
    [1, 1]
])

# Create rooms where these pieces are found
living_room = Room("Living Room", "A cozy living room filled with memories.", piece1)
kitchen = Room("Kitchen", "A clean kitchen with a puzzle piece.", piece2)
bedroom = Room("Bedroom", "A small bedroom with a wooden puzzle piece.", piece3)

# Create family members as characters
mother = Character("Mother", "Your mother is here, smiling warmly.")
father = Character("Father", "Your father is sitting at the table.")
sibling = Character("Sibling", "Your sibling is holding an old toy.")

# Add characters to rooms
living_room.add_character(mother)
kitchen.add_character(father)
bedroom.add_character(sibling)

# Create player
player = Player("Hero", starting_room=living_room)

# Room connections
living_room.add_neighbor("north", kitchen)
kitchen.add_neighbor("south", living_room)
kitchen.add_neighbor("east", bedroom)
bedroom.add_neighbor("west", kitchen)

# Flask routes
@app.route('/')
def home():
    # Determine movement possibilities
    neighbors = player.current_room.neighbors
    can_move_north = 'north' in neighbors
    can_move_south = 'south' in neighbors
    can_move_east = 'east' in neighbors
    can_move_west = 'west' in neighbors
    item_available = player.current_room.item is not None

    return render_template(
        'game.html', 
        room=player.current_room, 
        inventory=player.inventory,
        can_move_north=can_move_north, 
        can_move_south=can_move_south,
        can_move_east=can_move_east, 
        can_move_west=can_move_west,
        item_available=item_available,
        puzzle_solved=player.puzzle_solved
    )

@app.route('/move/<direction>')
def move(direction):
    player.move(direction)
    return redirect(url_for('home'))

@app.route('/take')
def take_item():
    player.take_item()
    return redirect(url_for('home'))

@app.route('/assemble')
def assemble_puzzle():
    try:
        if len(player.inventory) >= 3:  # All pieces collected
            pieces = player.inventory  # Pass the pieces collected to the template
            return render_template('puzzle.html', pieces=pieces)
        else:
            return redirect(url_for('home'))  # Redirect if not all pieces are collected
    except Exception as e:
        print(f"Error assembling puzzle: {e}")
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
