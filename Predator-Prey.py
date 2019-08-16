#import bpy
import random
from itertools import count
import weightedfreeroam
import checkforpredators
import boundarycheck


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
        self.state = 1
        self.viewdistance = 10
        self.last_movement = [0, 0]



predatorsize = 1
predatorstart = [10, -10, predatorsize/2]
preysize = 0.5
preystart = [1, 1, preysize/2]
duration = 100
groundsize = 50
predatorcount = 1
preycount = 1
randmax = 1000

predatorpositions = []
preypositions = []

predatorlist = []
preylist = []



def updateposition(position, movement):
    position[0] = position[0] + movement[0]
    position[1] = position[1] + movement[1]
    return position


def runawaaay(position, walkspeed, predatorspotted):
    movement = [0, 0]
    for i in range(2):
        movement[i] = predatorspotted[i] * walkspeed
    return movement


if __name__ == '__main__':
    # print("\n\n-----------------------RUN BEGIN------------------------\n")

    t = 0

    frame = 0

    #Initialise Predators
    for i in range(predatorcount):
        predinstance = Predators()
        # print("Predator {} starting position: {}".format(predinstance.id, predinstance.position))
        predatorlist.append(predinstance)

    #Initialise Prey
    for i in range(preycount):
        preyinstance = Prey()
        # print("Prey {} starting position: {}".format(preyinstance.id, preyinstance.position))
        preylist.append(preyinstance)

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


    while t < duration:


        for predinstance in predatorlist:
            predatorspotted = [0, 0]
            # print("\n\nmoving predator {}".format(predinstance.id))
            movement = weightedfreeroam.weightedfreeroam(predinstance.last_movement, predinstance.walkspeed)
            # print("movement = {}".format(movement))
            # print("previous position: {}".format(predinstance.position))
            movement = boundarycheck.boundarycheck(predatorspotted, predinstance.position, movement, groundsize, randmax)
            predinstance.last_movement = movement
            predinstance.position = updateposition(predinstance.position, movement)
            # print("Predator {} new position: {}".format(predinstance.id, predinstance.position))

        for preyinstance in preylist:
            # print("\nmoving prey {}".format(preyinstance.id))

            predatorspotted = checkforpredators.checkforpredators(preyinstance.position, preyinstance.viewdistance, predatorlist)

            if predatorspotted == [0, 0]:
                movement = weightedfreeroam.weightedfreeroam(preyinstance.last_movement, preyinstance.walkspeed)
                preyinstance.state = 1

            else:
                movement = runawaaay(preyinstance.position, preyinstance.walkspeed, predatorspotted)
                preyinstance.state = 0

            movement = boundarycheck.boundarycheck(predatorspotted, preyinstance.position, movement, groundsize, randmax)

            # print("previous position: {}".format(preyinstance.position))
            preyinstance.last_movement = movement
            preyinstance.position = updateposition(preyinstance.position, movement)

            # print("New position: {}".format(preyinstance.position))

        # print("\n\nloop end positions:\n")
        for predinstance in predatorlist:
            predatorsoutput = ('pred{}vectors.txt'.format(predinstance.id))
            with open(predatorsoutput, 'a') as file_object:
                for e in range(0, 3):
                    file_object.write(str(predinstance.position[e]))
                    if e!=2:
                        file_object.write(",")
                file_object.write("\n")

        for preyinstance in preylist:
            preyoutput = ('prey{}vectors.txt'.format(preyinstance.id))
            with open(preyoutput, 'a') as file_object:
                for e in range(0, 3):
                    file_object.write(str(preyinstance.position[e]))
                    if e!=2:
                        file_object.write(",")
                file_object.write("\n")
        t += 1
