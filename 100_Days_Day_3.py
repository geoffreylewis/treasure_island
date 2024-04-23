###################
# Treasure Island #
###################

# Banner Image (courtesy of [TomekK] on https://ascii.co.uk/art/treasure)
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')

# Beginning of Game
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.  Let\'s see if you can find it...\n")

# Possible Scenarios
cross_road = str(input("You\'re walking for awhile, and you eventually find yourself at a cross road.  Where do you want to go?  Type \"left\" or \"right\".\n").lower())
# Scenario 1
if cross_road == "left":
    print("You turn left and almost immediately fall into a hidden pit with spikes at the bottom.  You have met quite the untimely demise.")
elif cross_road == "right":
    # Scenario 2
    island_lake = str(input("You come to a lake.  There is an island in the middle of the lake.  Type \"wait\" to wait for a boat, or type \"swim\" to swim across.\n").lower())
    if island_lake == "wait":
        print("You wait and wait and wait, but no boat ever comes.  You eventually walk back to the cross road, take a wrong turn, and fall down to your death in a hidden pit full of spikes.")
    elif island_lake == "swim":
        # Scenario 3
        house_3_doors = str(input("You arrive at the island unharmed.  There is a house with 3 doors.  One is red, one is yellow, and one is blue.  Type which color you choose.\n").lower())
        if house_3_doors == "red":
            print("You open the door, and there, placed on the floor, is a bottle of some red liquid.  Your curiousity gets the better of you, and you take a sip.  A cold chill takes hold of you...")
        elif house_3_doors == "yellow":
            print("You open the door, and there, placed on the floor, is an open treasure chest full of gold coins.  Congratulations on having found the treasure!")
        elif house_3_doors == "blue":
            print("You open the door, and there is a large, murky pool of water in the center of the room.  You cautiously dip your hand in, but something suddenly wraps a tentacle around you and pulls you in...")
        else:
            print("Seriously?  You typed that?\n")
    else:
        print("Uh...  That ain\'t an option.\n")
else:
    print("You don\'t follow instructions well, do you?\n")

# End of Game
print()
if cross_road == "right" and island_lake == "swim" and house_3_doors == "yellow":
    print("YOU WIN!")
else:
    print("GAME OVER")