import random
import mutation
import outputmanager
from itertools import count


class Actors:
    _ids = count(0)

    def __init__(self, role, size, position, walkspeed, viewdistance, hunger, longevity, birth, death, age, lifespan, parent1, parent2, fertility, vectors, index):
        self.id = next(self._ids)
        self.role = role
        self.size = size
        self.position = position
        self.walkspeed = walkspeed
        self.viewdistance = viewdistance
        self.lastmovement = [0, 0]
        self.lunge = walkspeed * 2
        self.alive = 1
        self.dying = 0
        self.hunger = hunger
        self.sated = 0
        self.longevity = longevity
        self.birth = birth
        self.death = death
        self.age = age
        self.lifespan = lifespan
        self.causeofdeath = ""
        self.parent1 = parent1
        self.parent2 = parent2
        self.timesmated = 0
        self.enemieseaten = 0
        self.fertility = fertility
        self.vectors = vectors
        self.index = index

def generate_actors(groundsize, parameters):
    plantcount = parameters["plantcount"]
    predatorcount = parameters["predatorcount"]
    preycount = parameters["preycount"]
    preywalkspeed = parameters["preywalkspeed"]
    preyviewdistance = parameters["preyviewdistance"]
    actorlist = []
    parent1 = -1
    parent2 = -1
    birth = 0
    death = -1

    # initialise Actors and assign characteristics
    for i in range(predatorcount + preycount):
        position = [0, 0]
        longevity = parameters["predlongevity"]
        lifespan = parameters["predatorlifespan"]
        hunger = parameters["predlongevity"] /2
        fertility = parameters["predfertility"]
        index = i

        if i >= preycount:

            walkspeed = random.randint(parameters["predatorwalkspeed"] - 1, parameters["predatorwalkspeed"] + 1)
            viewdistance = random.randint(parameters["predatorviewdistance"] - 1, parameters["predatorviewdistance"] + 1)
            longevity = random.randint(parameters["predlongevity"] - 1, parameters["predlongevity"] + 1)
            lifespan = random.randint(parameters["predatorlifespan"] - 50, parameters["predatorlifespan"] + 50)
            age = random.randint(int(lifespan*0.2), int(lifespan * 0.8))
            hunger = random.randint(int(longevity/2 - 10), int(longevity/2 + 10))
            role = 'predator'
            size = parameters['predatorsize']
            fertility = random.randint(int(parameters["predfertility"]*0.1), int(parameters["predfertility"]*1.5))

            for j in range(0, 2):
                position[j] = random.randint(int(-groundsize/2), int(groundsize/2))

        else:

            walkspeed = random.randint(parameters["preywalkspeed"] - 1, parameters["preywalkspeed"] + 1)
            viewdistance = random.randint(parameters["preyviewdistance"] - 1, parameters["preyviewdistance"] + 1)
            longevity = random.randint(parameters["preylongevity"] - 1, parameters["preylongevity"] + 1)
            lifespan = random.randint(parameters["preylifespan"] - 50, parameters["preylifespan"] + 50)
            hunger = random.randint(int(longevity/2 - 10), int(longevity/2 + 10))
            role = 'prey'
            size = parameters['preysize']
            age = random.randint(int(lifespan*0.2), int(lifespan * 0.8))
            fertility = random.randint(int(parameters["preyfertility"]*0.1), int(parameters["preyfertility"]*1.5))



            for j in range(0, 2):
                position[j] = random.randint(int(-groundsize/2), int(groundsize/2))

        vectors = [[position[0], position[1]]]


        # Create actors and print out list
        Actor = Actors(role, size, position, walkspeed, viewdistance, hunger, longevity, birth, death, age, lifespan, parent1, parent2, fertility, vectors, index)
        actorlist.append(Actor)


    return actorlist





def createnewactor(livingactors, actorsinview, parent1, parent2, parameters, t, dead):

        position = [0, 0]
        birth = t
        death = -1
        age = 0
        for j in range(0, 2):
            position[j] = int((actorsinview[parent1].position[j] + actorsinview[parent2].position[j])/2)

        walkspeed = mutation.mutation(actorsinview[parent1].walkspeed, actorsinview[parent2].walkspeed)
        viewdistance = mutation.mutation(actorsinview[parent1].viewdistance, actorsinview[parent2].viewdistance)
        longevity = mutation.mutation(actorsinview[parent1].longevity, actorsinview[parent2].longevity)
        lifespan = mutation.mutation(actorsinview[parent1].lifespan, actorsinview[parent2].lifespan)
        role = actorsinview[parent1].role
        size = actorsinview[parent1].size
        fertility = 0
        hunger = longevity/2
        vectors = [[dead[0], dead[1]]]

        for i in range(1, t):
            vectors.append([dead[0], dead[1]])
        vectors.append([position[0], position[1]])


        index = len(livingactors)
        # Create actors and print out list
        Actor = Actors(role, size, position, walkspeed, viewdistance, hunger, longevity, birth, death, age, lifespan, actorsinview[parent1].id, actorsinview[parent2].id, fertility, vectors, index)
        livingactors.append(Actor)




        return(livingactors)


def generateplants(livingactors, groundsize, plantcount, t, dead, parameters):

    for i in range(plantcount):

        role = 'plant'
        position = [0, 0]

        for j in range(0, 2):
            position[j] = random.randint(int(-groundsize/2), int(groundsize/2))

        hunger = -1
        birth = t
        death = -1
        walkspeed = 0
        viewdistance = 0
        longevity = -1
        lifespan = -1
        size = parameters["plantsize"]
        parent1 = -1
        parent2 = -1
        fertility = -1
        age = 0

        if t == 0:
            vectors = [[position[0], position[1]]]
        else:
            vectors = [[dead[0], dead[1]]]
            for l in range(1, t):
                vectors.append([dead[0], dead[1]])

        vectors.append([position[0], position[1]])
        index = len(livingactors)
        Actor = Actors(role, size, position, walkspeed, viewdistance, hunger, longevity, birth, death, age, lifespan, parent1, parent2, fertility, vectors, index)
        livingactors.append(Actor)

    return(livingactors)