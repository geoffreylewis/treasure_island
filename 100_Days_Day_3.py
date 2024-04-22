###################
# Treasure Island #
###################

# Beginning of Game
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

# Scenarios
cross_road = input("You\'re at a cross road.  Where do you want to go?  Type \"left\" or \"right\".\n")
if cross_road == "left":
    print("You choose left.")
else:
    print("You choose right.")

island_lake = input("You come to a lake.  There is an island in the middle of the lake.  Type \"wait\" to wait for a boat, or type \"swim\" to swim across.\n")
if island_lake == "wait":
    print("You choose wait.")
else:
    print("You choose swim.")

house_3_doors = input("You arrive at the island unharmed.  There is a house with 3 doors.  One is red, one is yellow, and one is blue.  Type which color you choose.\n")
if house_3_doors == "red":
    print("You choose red.")
elif house_3_doors == "yellow":
    print("You chose yellow.")
else:
    print("You choose blue.")

# Final Outcome
print()
print(f"GAME OVER")