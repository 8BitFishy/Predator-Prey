import random

def mutation(parent1, parent2):

    diceroll = random.randint(0, 100)

    #somewhere betweem the two
    if diceroll <= 81:
        if parent1 == parent2:
            trait = parent1
        elif parent1 < parent2:
            trait = random.randint(parent1, parent2)
        else:
            trait = random.randint(parent2, parent1)

    #take after parent 1
    elif diceroll > 81 and diceroll <= 90:
        trait = parent1 + int(parent1*(((random.randint(-5, 5))/100)))

    #take after parent 2
    elif diceroll > 90 and diceroll <= 98:
        trait = parent2 + int(parent2*((random.randint(-5, 5))/100))

    elif diceroll > 98 and diceroll <= 99:

        #if parent 2 has higher value than parent 1, take after parent 2 + 5 - 15%
        if parent2 >= parent1:
            trait = parent2 + int(parent2*((random.randint(5, 10))/100))

        #if parent 1 has higher value than parent 2, take after parent 1 + 5 - 15%
        else:
            trait = parent1 + int(parent1*((random.randint(5, 10))/100))

    else:

        #if parent 2 has lower value than parent 1, take after parent 2 - 5 - 15%
        if parent2 <= parent1:
            trait = parent2 - int(parent2*((random.randint(5, 10)/100)))

        #if parent 1 has lower value than parent 2, take after parent 1 - 5 - 15%
        else:
            trait = parent1 - int(parent1*((random.randint(5, 10)/100)))

    return trait