from itertools import count
import weightedfreeroam
import checkforpredators
import boundarycheck
import updateposition
import runawaaay
import outputmanager
import os


class Actors:
    _ids = count(0)

    def __init__(self):
        self.id = next(self._ids)
        self.role = role
        self.size = size
        self.position = startposition
        self.walkspeed = walkspeed
        self.viewdistance = viewdistance
        self.lastmovement = [0, 0]


parameters = {}

with open("Parameters.txt") as f:
    for line in f:
        name, value = line.split("=")
        name = name.rstrip(" ")
        parameters[name] = value.rstrip('\n')

predatorsize = float(parameters["predatorsize"])
preysize = float(parameters["preysize"])
duration = int(parameters["duration"])
groundsize = float(parameters["groundsize"])
predatorcount = int(parameters["predatorcount"])
preycount = int(parameters["preycount"])
randmax = int(parameters["randmax"])
predatorwalkspeed = int(parameters["predatorwalkspeed"])
preywalkspeed = int(parameters["preywalkspeed"])
predatorviewdistance = int(parameters["predatorviewdistance"])
preyviewdistance = int(parameters["preyviewdistance"])
predatorstart = [int(parameters['predatorstartx']), int(parameters['predatorstarty'])]
preystart = [int(parameters['preystartx']), int(parameters['preystarty'])]


predatorpositions = []
preypositions = []
predatorlist = []
preylist = []
actorlist = []



#_________________________Start of main simulation___________________________




if __name__ == '__main__':

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n-----------------------RUN BEGIN------------------------\n")

    t = 0






    # initialise Actors and assign characteristics
    for i in range(predatorcount + preycount):

        if i < predatorcount:
            role = 'predator'
            size = predatorsize
            startposition = predatorstart
            walkspeed = predatorwalkspeed
            viewdistance = predatorviewdistance
        else:
            role = 'prey'
            size = preysize
            startposition = preystart
            walkspeed = preywalkspeed
            viewdistance = preyviewdistance

        # Create actors and print out list
        Actor = Actors()
        #print("{} is {}, start position {}, walkspeed {}, viewdistance {}, size = {}".format(Actor.id, Actor.role, Actor.position, Actor.walkspeed, Actor.viewdistance, Actor.size))
        actorlist.append(Actor)

    #print("\n\nActors generated\n\n")



    while t < duration:
        print("\n------------Round {}------------\n".format(t))
        for Actor in actorlist:
            print(f"\nActor {Actor.id} operating as {Actor.role} starts round at position {Actor.position}")
            #if Actor.id == 0:
                #print('\nRound starting position{}\n'.format(Actor.position))

            predatorspotted = checkforpredators.checkforpredators(Actor.position, Actor.viewdistance, actorlist, Actor.id, predatorcount)

            if predatorspotted == [0, 0]:
                if Actor.role == "prey":
                    print("Prey {} safe".format(Actor.id))

                movement = weightedfreeroam.weightedfreeroam(Actor.lastmovement, Actor.walkspeed)
                print(f"Movement for actor {Actor.id} in weighted freeroam = {movement}")
            else:
                print("Actor {} predator spotted at {}\n".format(Actor.id, predatorspotted))

                movement = runawaaay.runawaaay(Actor.walkspeed, predatorspotted, Actor.viewdistance)
                print("Actor {} running from predator at vector {} with movement {}".format(Actor.id, predatorspotted, movement))
            print(f"{Actor.role} movement before boundary check = {movement}")
            movement = boundarycheck.boundarycheck(predatorspotted, Actor.position, movement, groundsize, randmax)
            print(f"{Actor.role} movement after boundary check = {movement}")
            print(f"{Actor.role} position before update = {Actor.position}")
            Actor.position = updateposition.updateposition(Actor.position, movement)
            print(f"{Actor.role} position after update = {Actor.position}")
            Actor.lastmovement = movement

            #if Actor.id == 0:
             #   print('\nRound ending position{}\n'.format(Actor.position))





            #if Actor.id == 0:
               # print("{} position - \n\n{}\n\n".format(Actor.id, Actor.position))

        outputmanager.populateoutputfiles(actorlist)

        t += 1

