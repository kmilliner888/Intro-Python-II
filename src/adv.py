from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
class Adv:
    def __init__(self, name, player, room):
        self.name = name
        self.player = player
        self.room = room

    def __str__(self):
        return self.name
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player("Player1", "outside")
print(new_player)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
selection = ""
while selection != len(new_player.current_room)+1:
    selection = input("Select 'n', 's', 'e', or 'w: ")
    try:
        selection = str(selection)
        if new_player.current_room == "outside" and selection  == "n":
            new_player.current_room == "foyer"
            print("You are now in the foyer")
        if new_player.current_room == "foyer" and selection == "s":
            new_player.current_room == "outside"
            print("You are now outside")
        if new_player.current_room == "foyer" and selection == "n":
            new_player.current_room == "overlook"
            print("You are now in the overlook")
        if new_player.current_room == "foyer" and selection == "e":
            new_player.current_room == "narrow"
            print("You are now in the narrow")
        if new_player.current_room == "overlook" and selection == "s":
            new_player.current_room == "foyer"
            print("You are now in the foyer")
        if new_player.current_room == "narrow" and selection == "w":
            new_player.current_room == "foyer"
            print("You are now in the foyer")
        if new_player.current_room == "narrow" and selection == "n":
            new_player.current_room == "treasure"
            print("You are now in the Treasure")
        if new_player.current_room == "treasure" and selection == "s":
            new_player.current_room == "narrow"
            print("You are now in the narrow")
    except ValueError:
        print("Please enter 'n' to begin the game")
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

# If the user enters "q", quit the game.
