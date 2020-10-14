import random


class Actors:
    _ids = count(0)

    def __init__(self):
        self.id = id
        self.role = role
        self.size = size
        self.position = startposition
        self.walkspeed = walkspeed
        self.viewdistance = viewdistance
        self.lastmovement = [0, 0]
        self.lunge = walkspeed * 2
        self.alive = 1
        self.dying = 0
        self.hunger = starthunger
        self.sated = 0
        self.longevity = startlongevity
        self.randy = startrandy


def createnewactor(actorlist, parent1, parent2, t):

        for j in range(0, 2):
            startposition[j] = actorlist[parent1].position[j]
        role = 'prey'
        size = preysize
        walkspeed = preywalkspeed
        viewdistance = preyviewdistance
        startlongevity = 100
        starthunger = 30
        startrandy = 15
        diceroll = 100
        id = len(actorlist)-1

        if actorlist[parent1].id == 'predator':
            role = 'predator'
            size = predatorsize
            for j in range(0, 2):
                startposition[j] = actorlist[parent1].position[j]


            print(f"Parent 1 longevity - {actorlist[parent1].longevity}")
            print(f"Parent 2 longevity - {actorlist[parent2].longevity}")

            diceroll = random.randint(0, 100)
            print(f"Diceroll = {diceroll}")

            if diceroll < 40:
                longevity = actorlist[parent1].longevity

            elif diceroll => 40 and < 80:
                longevity = actorlist[parent2].longevity

            elif diceroll >= 80 and < 90:
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


        else:
            role = 'prey'
            size = preysize
            walkspeed = preywalkspeed
            viewdistance = preyviewdistance

        print(f"Generating new actor:")
        # Create actors and print out list
        Actor = Actors()
        print(f"actorlist length = {len(actorlist)}")
        actorlist.append(Actor)
        print(f"Actor{actorlist.len - 1} born")
        print(f"New Actor in role {role}")
        print(f"New Actor longevity {longevity}")
