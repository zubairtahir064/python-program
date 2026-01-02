import random

def print_dice(face):
    print("  _____________")
    print(" |             |")

    if face == 1:
        print(" |             |")
        print(" |      ●      |")
        print(" |             |")

    elif face == 2:
        print(" |  ●          |")
        print(" |             |")
        print(" |          ●  |")

    elif face == 3:
        print(" |  ●          |")
        print(" |      ●      |")
        print(" |          ●  |")

    elif face == 4:
        print(" |  ●       ● |")
        print(" |             |")
        print(" |  ●       ● |")

    elif face == 5:
        print(" |  ●       ● |")
        print(" |      ●      |")
        print(" |  ●       ● |")

    elif face == 6:
        print(" |  ●       ● |")
        print(" |  ●       ● |")
        print(" |  ●       ● |")

    print(" |_____________|")


# roll the dice
roll = random.randint(1, 6)
print("You rolled:", roll)
print_dice(roll)

