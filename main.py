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


#TODO delete these two classes
class Predators:  # Python3 defaults to using object in classes  so you don't need to pass it in as a param in the class

    _ids = count(0)

    def __init__(self):
        self.id = next(self._ids)
        self.position = predatorstart
        self.walkspeed = 5
        self.last_movement = [0, 0]
class Prey:  # Python3 defaults to using object in classes  so you don't need to pass it in as a param in the class

    _ids = count(0)

    def __init__(self):
        self.id = next(self._ids)
        self.position = preystart
        self.walkspeed = 2
        self.viewdistance = 10
        self.last_movement = [0, 0]


predatorsize = 1
predatorstart = [10, -10, predatorsize / 2]
preysize = 0.5
preystart = [1, 1, preysize / 2]
duration = 100
groundsize = 50
predatorcount = 3
preycount = 2
randmax = 1000

predatorpositions = []
preypositions = []
actorpositions = []

predatorlist = []
preylist = []
actorlist = []

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n-----------------------RUN BEGIN------------------------\n")

    t = 0

    frame = 0

    # initialise Actors and assign characteristics
    for i in range(predatorcount + preycount):

        if i < predatorcount:
            role = 'predator'
            size = predatorsize
            startposition = [groundsize/2-i, groundsize/2+i]
            walkspeed = 2
            viewdistance = 4
        else:
            role = 'prey'
            size = preysize
            startposition = [groundsize/2+i, groundsize/2 - i]
            walkspeed = 10
            viewdistance = 5

        # Create actors and print out list
        Actor = Actors()
        print("{} is {}, start position {}, walkspeed {}, viewdistance {}, size = {}".format(Actor.id, Actor.role, Actor.position, Actor.walkspeed, Actor.viewdistance, Actor.size))
        actorlist.append(Actor)

    print("\n\nActors generated\n\n")


#TODO delete these two functions
    # Initialise Predators
    for i in range(predatorcount):
        predinstance = Predators()
        # print("Predator {} starting position: {}".format(predinstance.id, predinstance.position))
        predatorlist.append(predinstance)

    # Initialise Prey
    for i in range(preycount):
        preyinstance = Prey()
        # ##print("Prey {} starting position: {}".format(preyinstance.id, preyinstance.position))
        preylist.append(preyinstance)

'''
    #Create blank files for predator vectors
    for predinstance in predatorlist:
        predatorsoutput = ('pred{}vectors.txt'.format(predinstance.id))
        with open(predatorsoutput, 'w') as file_object:
            file_object.write("")

    #Create blank files for prey vectors
    for preyinstance in preylist:
        preyoutput = ('prey{}vectors.txt'.format(preyinstance.id))
        with open(preyoutput, 'w') as file_object:
            file_object.write("")
'''

#TODO delete this function and move to populate
outputmanager.createoutputfiles(actorlist)



while t < duration:

    for Actor in actorlist:
        predatorspotted = [0, 0]

        movement = weightedfreeroam.weightedfreeroam(Actor.lastmovement, Actor.walkspeed)
        movement = boundarycheck.boundarycheck(predatorspotted, Actor.position, movement, groundsize, randmax)
        Actor.lastmovement = movement
        Actor.position = updateposition.updateposition(Actor.position, movement)


    for predinstance in predatorlist:
        predatorspotted = [0, 0]
        movement = weightedfreeroam.weightedfreeroam(predinstance.last_movement, predinstance.walkspeed)
        movement = boundarycheck.boundarycheck(predatorspotted, predinstance.position, movement, groundsize, randmax)
        predinstance.last_movement = movement
        predinstance.position = updateposition.updateposition(predinstance.position, movement)
        # ##print("Predator {} new position: {}".format(predinstance.id, predinstance.position))




    for preyinstance in preylist:
        # ##print("\nmoving prey {}".format(preyinstance.id))

        predatorspotted = checkforpredators.checkforpredators(preyinstance.position, preyinstance.viewdistance,
                                                              predatorlist)

        if predatorspotted == [0, 0]:
            movement = weightedfreeroam.weightedfreeroam(preyinstance.last_movement, preyinstance.walkspeed)

        else:
            movement = runawaaay.runawaaay(preyinstance.position, preyinstance.walkspeed, predatorspotted)

        movement = boundarycheck.boundarycheck(predatorspotted, preyinstance.position, movement, groundsize, randmax)

        # ##print("previous position: {}".format(preyinstance.position))
        preyinstance.last_movement = movement
        preyinstance.position = updateposition.updateposition(preyinstance.position, movement)

        # ##print("New position: {}".format(preyinstance.position))







    # ##print("\n\nloop end positions:\n")
    '''
    for predinstance in predatorlist:
        predatorsoutput = ('pred{}vectors.txt'.format(predinstance.id))
        with open(predatorsoutput, 'a') as file_object:
            for e in range(0, 3):
                file_object.write(str(predinstance.position[e]))
                if e != 2:
                    file_object.write(",")
            file_object.write("\n")

    for preyinstance in preylist:
        preyoutput = ('prey{}vectors.txt'.format(preyinstance.id))
        with open(preyoutput, 'a') as file_object:
            for e in range(0, 3):
                file_object.write(str(preyinstance.position[e]))
                if e != 2:
                    file_object.write(",")
            file_object.write("\n")
            '''
    for Actor in actorlist:
        Actor.position.append(int(Actor.size)/2)
        if Actor.id == 0:
            print("{} position - \n\n{}\n\n".format(Actor.id, Actor.position))
    outputmanager.populateoutputfiles(actorlist)
    t += 1
