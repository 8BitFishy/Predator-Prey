import random
from itertools import count


class Actors:
    _ids = count(0)

    def __init__(self, role, size, position, walkspeed, viewdistance, hunger, longevity, randy, birth, death, lifespan):
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
        self.lifespan = lifespan


def generate_actors(groundsize, parameters):

    predatorsize = parameters["predatorsize"]
    preysize = parameters["preysize"]
    predatorcount = parameters["predatorcount"]
    preycount = parameters["preycount"]
    predatorwalkspeed = parameters["predatorwalkspeed"]
    preywalkspeed = parameters["preywalkspeed"]
    predatorviewdistance = parameters["predatorviewdistance"]
    preyviewdistance = parameters["preyviewdistance"]
    actorlist = []

    birth = 0
    death = -1

    # initialise Actors and assign characteristics
    for i in range(predatorcount + preycount):
        position = [0, 0]
        role = 'prey'
        size = preysize
        walkspeed = preywalkspeed
        viewdistance = preyviewdistance
        longevity = parameters["predlongevity"]
        hunger = 30
        randy = parameters["predrandy"]
        lifespan = parameters["predatorlifespan"]


        if i >= preycount:
            role = 'predator'
            size = predatorsize
            for j in range(0, 2):
                position[j] = random.randint(int(-groundsize/2), int(groundsize/2))
            longevity = parameters["predlongevity"] + random.randint(-10, 10)
            walkspeed = predatorwalkspeed
            viewdistance = predatorviewdistance
            lifespan = parameters["predatorlifespan"]



        else:
            role = 'prey'
            size = preysize
            for j in range(0, 2):
                position[j] = random.randint(int(-groundsize/2), int(groundsize/2))
            walkspeed = preywalkspeed
            viewdistance = preyviewdistance


        # Create actors and print out list
        Actor = Actors(role, size, position, walkspeed, viewdistance, hunger, longevity, randy, birth, death, lifespan)
        actorlist.append(Actor)


    return actorlist





def createnewactor(actorlist, parent1, parent2, parameters, t):

        position = [0, 0]

        for j in range(0, 2):
            position[j] = int((actorlist[parent1].position[j] + actorlist[parent2].position[j])/2)

        predatorsize = parameters["predatorsize"]
        preysize = parameters["preysize"]
        predatorwalkspeed = parameters["predatorwalkspeed"]
        preywalkspeed = parameters["preywalkspeed"]
        predatorviewdistance = parameters["predatorviewdistance"]
        preyviewdistance = parameters["preyviewdistance"]


        longevity = parameters["predlongevity"]
        hunger = 30
        randy = parameters["predrandy"]

        birth = t
        death = -1


        if actorlist[parent1].role == 'predator':
            role = actorlist[parent1].role
            size = actorlist[parent1].size

            print(f"Parent 1 longevity - {actorlist[parent1].longevity}")
            print(f"Parent 2 longevity - {actorlist[parent2].longevity}")

            diceroll = random.randint(0, 100)
            print(f"Diceroll = {diceroll}")

            if diceroll < 40:
                longevity = actorlist[parent1].longevity

            elif diceroll >= 40 and diceroll < 80:
                longevity = actorlist[parent2].longevity

            elif diceroll >= 80 and diceroll < 90:
                if actorlist[parent2].longevity >= actorlist[parent1].longevity:
                    longevity = actorlist[parent2].longevity + random.randint(1, 20)
                    print("Mutation!")

                else:
                    longevity = actorlist[parent1].longevity + random.randint(1, 20)
                    print("Mutation!")
            else:
                if actorlist[parent2].longevity >= actorlist[parent1].longevity:
                    longevity = actorlist[parent1].longevity - random.randint(1, 20)
                    print("Mutation!")
                else:
                    longevity = actorlist[parent2].longevity - random.randint(1, 20)
                    print("Mutation!")

            walkspeed = actorlist[parent1].walkspeed
            viewdistance = actorlist[parent1].viewdistance
            lifespan = parameters["predatorlifespan"]


        else:
            role = 'prey'
            size = preysize
            walkspeed = preywalkspeed
            viewdistance = preyviewdistance


        print(f"Generating new actor:")
        # Create actors and print out list
        Actor = Actors(role, size, position, walkspeed, viewdistance, hunger, longevity, randy, birth, death, lifespan)
        actorlist.append(Actor)

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
