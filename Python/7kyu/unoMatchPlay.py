
def can_play(hand, face_up):
    
    face_up_split = face_up.split()
    
    for card in hand:
        hand_split = card.split()
        if hand_split[0] == face_up_split[0] or hand_split[1] == face_up_split[1]:
            return True
        
    return False


print(can_play(["yellow 3", "yellow 7", "blue 8", "red 9", "red 2"], "red 1"))
print(can_play(["yellow 3", "yellow 5", "red 8"], "blue 5"))
print(can_play(["yellow 3", "blue 5", "red 8", "red 9"], "green 4"))


# Task
# Write a function that takes in two arguments: (1) a player's current hand and (2) the current face-up card on the table. 
# The function will return True if the player can make a play, or False if the player has to draw from the deck.

# A player can make a play if they have a card:
# that is the same color as the face-up card,
# OR that is the same number as the face-up card.

# Cards Format
# Colors are always lowercase: `"red", "yellow", "blue", "green".
# Numbers are digits from 0 to 9.
# Each card is formatted as "color number", e.g., "blue 5"

# Notes
# Return False if the player is not holding any cards (an empty list).
# There are no special cards or wildcards in this deck.

# Examples
# ["yellow 3", "yellow 7", "blue 8", "red 9", "red 2"], "red 1" ➞ True   "red 9" or "red 2"
# ["yellow 3", "yellow 7"], "blue 7"                   ➞ True   "yellow 7"
# ["yellow 3", "blue 5", "red 8", "red 9"], "green 4"  ➞ False