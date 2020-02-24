# import bpy
import random
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




predatorsize = 1
predatorstart = [10, -10, predatorsize / 2]
preysize = 0.5
preystart = [1, 1, preysize / 2]
duration = 10
groundsize = 50
predatorcount = 5
preycount =3
randmax = 1000

predatorpositions = []
preypositions = []
actorpositions = []

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
            startposition = [int(groundsize/2-i), int(groundsize/2+i)]
            walkspeed = 2
            viewdistance = 4
        else:
            role = 'prey'
            size = preysize
            startposition = [int(groundsize/2+i), int(groundsize/2 - i)]
            walkspeed = 4
            viewdistance = 4

        # Create actors and print out list
        Actor = Actors()
        #print("{} is {}, start position {}, walkspeed {}, viewdistance {}, size = {}".format(Actor.id, Actor.role, Actor.position, Actor.walkspeed, Actor.viewdistance, Actor.size))
        actorlist.append(Actor)

    #print("\n\nActors generated\n\n")

    outputmanager.createoutputfiles(actorlist)



    while t < duration:
        print("------------Round {}------------".format(t))
        for Actor in actorlist:
            #if Actor.id == 0:
                #print('\nRound starting position{}\n'.format(Actor.position))

            predatorspotted = checkforpredators.checkforpredators(Actor.position, Actor.viewdistance, actorlist, Actor.id, predatorcount)

            if predatorspotted == [0, 0]:
                print("Actor {} safe\n".format(Actor.id))

                movement = weightedfreeroam.weightedfreeroam(Actor.lastmovement, Actor.walkspeed)

            else:
                print("Actor {} predator spotted at {}\n".format(Actor.id, predatorspotted))

                movement = runawaaay.runawaaay(Actor.walkspeed, predatorspotted)
                print("Actor {} running from predator at vector {} with movement {}".format(Actor.id, predatorspotted, movement))
            movement = boundarycheck.boundarycheck(predatorspotted, Actor.position, movement, groundsize, randmax)
            Actor.lastmovement = movement
            Actor.position = updateposition.updateposition(Actor.position, movement)


            #if Actor.id == 0:
             #   print('\nRound ending position{}\n'.format(Actor.position))





            #if Actor.id == 0:
               # print("{} position - \n\n{}\n\n".format(Actor.id, Actor.position))


        outputmanager.populateoutputfiles(actorlist)
        t += 1

