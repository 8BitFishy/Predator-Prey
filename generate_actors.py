import random
import mutation
import outputmanager
from itertools import count


class Actors:
    _ids = count(0)

    def __init__(self, role, size, position, walkspeed, viewdistance, hunger, longevity, birth, death, lifespan, parent1, parent2, fertility, vectors):
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
        self.age = 0
        self.lifespan = lifespan
        self.causeofdeath = ""
        self.parent1 = parent1
        self.parent2 = parent2
        self.timesmated = 0
        self.enemieseaten = 0
        self.fertility = fertility
        self.vectors = vectors

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


        if i >= preycount:

            walkspeed = random.randint(parameters["predatorwalkspeed"] - 1, parameters["predatorwalkspeed"] + 1)
            viewdistance = random.randint(parameters["predatorviewdistance"] - 1, parameters["predatorviewdistance"] + 1)
            longevity = random.randint(parameters["predlongevity"] - 1, parameters["predlongevity"] + 1)
            lifespan = random.randint(parameters["predatorlifespan"] - 20, parameters["predatorlifespan"] + 20)
            hunger = random.randint(parameters["predlongevity"]/2 - 10, parameters["predlongevity"]/2 + 10)
            walkspeed = random.randint(parameters["predatorwalkspeed"] - 1, parameters["predatorwalkspeed"] + 1)
            viewdistance = random.randint(parameters["predatorviewdistance"] - 1, parameters["predatorviewdistance"] + 1)
            longevity = random.randint(parameters["predlongevity"] - 1, parameters["predlongevity"] + 1)
            lifespan = random.randint(parameters["predatorlifespan"] - 50, parameters["predatorlifespan"] + 50)
            hunger = random.randint(parameters["predlongevity"]/2 - 10, parameters["predlongevity"]/2 + 10)
            role = 'predator'
            size = parameters['predatorsize']
            fertility = parameters["predfertility"]

            for j in range(0, 2):
                position[j] = random.randint(int(-groundsize/2), int(groundsize/2))

        else:
            walkspeed = random.randint(parameters["preywalkspeed"] - 1, parameters["preywalkspeed"] + 1)
            viewdistance = random.randint(parameters["preyviewdistance"] - 1, parameters["preyviewdistance"] + 1)
            longevity = random.randint(parameters["preylongevity"] - 1, parameters["preylongevity"] + 1)
            lifespan = random.randint(parameters["preylifespan"] - 20, parameters["preylifespan"] + 20)
            hunger = random.randint(parameters["preylongevity"]/2 - 10, parameters["preylongevity"]/2 + 10)
            walkspeed = random.randint(parameters["preywalkspeed"] - 1, parameters["preywalkspeed"] + 1)
            viewdistance = random.randint(parameters["preyviewdistance"] - 1, parameters["preyviewdistance"] + 1)
            longevity = random.randint(parameters["preylongevity"] - 1, parameters["preylongevity"] + 1)
            lifespan = random.randint(parameters["preylifespan"] - 50, parameters["preylifespan"] + 50)
            hunger = random.randint(parameters["preylongevity"]/2 - 10, parameters["preylongevity"]/2 + 10)
            role = 'prey'
            size = parameters['preysize']
            fertility = parameters["preyfertility"]

            for j in range(0, 2):
                position[j] = random.randint(int(-groundsize/2), int(groundsize/2))

        vectors = [[position[0], position[1]]]

        # Create actors and print out list
        Actor = Actors(role, size, position, walkspeed, viewdistance, hunger, longevity, birth, death, lifespan, parent1, parent2, fertility, vectors)
        actorlist.append(Actor)


    return actorlist





def createnewactor(actorlist, parent1, parent2, parameters, t, dead):

        position = [0, 0]
        birth = t
        death = -1

        for j in range(0, 2):
            position[j] = int((actorlist[parent1].position[j] + actorlist[parent2].position[j])/2)

        walkspeed = mutation.mutation(actorlist[parent1].walkspeed, actorlist[parent2].walkspeed)
        viewdistance = mutation.mutation(actorlist[parent1].viewdistance, actorlist[parent2].viewdistance)
        longevity = mutation.mutation(actorlist[parent1].longevity, actorlist[parent2].longevity)
        lifespan = mutation.mutation(actorlist[parent1].lifespan, actorlist[parent2].lifespan)
        role = actorlist[parent1].role
        size = actorlist[parent1].size
        fertility = 0
        hunger = longevity/2
        vectors = [[dead[0], dead[1]]]

        for i in range(1, t):
            vectors.append([dead[0], dead[1]])
        vectors.append([position[0], position[1]])

        # Create actors and print out list
        Actor = Actors(role, size, position, walkspeed, viewdistance, hunger, longevity, birth, death, lifespan, parent1, parent2, fertility, vectors)
        actorlist.append(Actor)




        return(actorlist)


def generateplants(actorlist, groundsize, plantcount, t, dead, parameters):

    for i in range(plantcount):

        role = 'plant'
        position = [0, 0]

        for j in range(0, 2):
            position[j] = random.randint(int(-groundsize/2), int(groundsize/2))

        hunger = -1
        birth = -1
        death = -1
        walkspeed = 0
        viewdistance = 0
        longevity = -1
        lifespan = -1
        size = parameters["plantsize"]
        parent1 = -1
        parent2 = -1
        fertility = -1


        if t == 0:
            vectors = [[position[0], position[1]]]
        else:
            vectors = [[dead[0], dead[1]]]
            for l in range(1, t):
                vectors.append([dead[0], dead[1]])

        vectors.append([position[0], position[1]])

        Actor = Actors(role, size, position, walkspeed, viewdistance, hunger, longevity, birth, death, lifespan, parent1, parent2, fertility, vectors)
        actorlist.append(Actor)

    return(actorlist)