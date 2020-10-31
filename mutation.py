import random

def mutation(parent1, parent2):

    diceroll = random.randint(0, 100)

    #take after parent 1
    if diceroll < 40:
        trait = parent1 + random.randint(-2, 2)

    #take after parent 2
    elif diceroll >= 40 and diceroll < 80:
        trait = parent2 + random.randint(-2, 2)

    elif diceroll >= 80 and diceroll < 90:

        #if parent 2 has higher value than parent 1, take after parent 2 + 5 - 15%
        if parent2 >= parent1:
            trait = parent2 + int(parent2*(1+(random.randint(5, 15))/100))

        #if parent 1 has higher value than parent 2, take after parent 1 + 5 - 15%
        else:
            trait = parent1 + int(parent1*(1+(random.randint(5, 15))/100))

    else:

        #if parent 2 has lower value than parent 1, take after parent 2 - 5 - 15%
        if parent2 <= parent1:
            trait = parent2 - int(parent2*(1-(random.randint(5, 15)/100)))

            # if parent 1 has lower value than parent 2, take after parent 1 - 5 - 15%
        else:
            trait = parent1 - int(parent1*(1-(random.randint(5, 15)/100)))

    return trait