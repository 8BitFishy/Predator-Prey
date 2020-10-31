import random

def mutation(parent1, parent2):

    diceroll = random.randint(0, 100)

    if diceroll < 40:
        trait = parent1 + random.randint(-2, 2)

    elif diceroll >= 40 and diceroll < 80:
        trait = parent2 + random.randint(-2, 2)

    elif diceroll >= 80 and diceroll < 90:

        if parent2 >= parent1:
            trait = parent2 + int(parent2*(random.randint(5, 15)/100))

        else:
            trait = parent1 + int(parent1*(random.randint(5, 15)/100))

    else:
        if parent2 <= parent1:
            trait = parent2 - int(parent2*(random.randint(5, 15)/100))
        else:
            trait = parent1 - int(parent1*(random.randint(5, 15)/100))

    return trait