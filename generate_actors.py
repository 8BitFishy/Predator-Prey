import random
import mutation
from itertools import count


class Actors:
    _ids = count(0)

    def __init__(self, role, size, position, walkspeed, viewdistance, hunger, longevity, randy, birth, death, lifespan, parent1, parent2):
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
        self.randy = randy
        self.birth = birth
        self.death = death
        self.age = 0
        self.lifespan = lifespan
        self.causeofdeath = ""
        self.parent1 = parent1
        self.parent2 = parent2
        self.timesmated = 0
        self.enemieseaten = 0


def generate_actors(groundsize, parameters):

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
        randy = parameters["predrandy"]
        lifespan = parameters["predatorlifespan"]
        hunger = parameters["predrandy"] + 15

        if i >= preycount:

            for j in range(0, 2):
                position[j] = random.randint(int(-groundsize/2), int(groundsize/2))

            walkspeed = mutation.mutation(parameters["predatorwalkspeed"] - 1, parameters["predatorwalkspeed"] + 1)
            viewdistance = mutation.mutation(parameters["predatorviewdistance"] - 1, parameters["predatorviewdistance"] + 1)
            longevity = mutation.mutation(parameters["predlongevity"] - 1, parameters["predlongevity"] + 1)
            lifespan = mutation.mutation(parameters["predatorlifespan"] - 1, parameters["predatorlifespan"] + 1)
            hunger = mutation.mutation(parameters["predrandy"] + 10, parameters["predrandy"] + 20)
            role = 'predator'
            size = parameters['predatorsize']





        else:
            role = 'prey'
            size = parameters["preysize"]
            for j in range(0, 2):
                position[j] = random.randint(int(-groundsize/2), int(groundsize/2))
            walkspeed = preywalkspeed
            viewdistance = preyviewdistance


        # Create actors and print out list
        Actor = Actors(role, size, position, walkspeed, viewdistance, hunger, longevity, randy, birth, death, lifespan, parent1, parent2)
        actorlist.append(Actor)


    return actorlist





def createnewactor(actorlist, parent1, parent2, parameters, t):

        position = [0, 0]
        hunger = parameters["predrandy"]+10
        randy = parameters["predrandy"]
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


        print(f"Generating new actor:")
        # Create actors and print out list
        Actor = Actors(role, size, position, walkspeed, viewdistance, hunger, longevity, randy, birth, death, lifespan, parent1, parent2)
        actorlist.append(Actor)
        print(f"Parent 1 - {actorlist[parent1].id}")
        print(f"Parent 1 - {actorlist[parent2].id}")
        print(f"Actor{Actor.id}")
        print(f"Actor role - {Actor.role}")
        print(f"Actor size - {Actor.size}")
        print(f"Actor position - {Actor.position}")
        print(f"Actor walkspeed - {Actor.walkspeed}")
        print(f"Actor viewdistance - {Actor.viewdistance}")
        print(f"Actor hunger - {Actor.hunger}")
        print(f"Actor longevity - {Actor.longevity}")
        print(f"Actor randy - {Actor.randy}")



        return(actorlist)
