#import bpy
import random
from itertools import count
import weightedfreeroam
import checkforpredators
import boundarycheck
import updateposition
import runawaaay


class Actors:

  _ids = count(0)

  def __init__(self):
    self.id = next(self._ids)
    self.role = role
    self.startposition = startposition
    self.walkspeed = walkspeed
    self.viewdistance = viewdistance
    self.lastmovement = [0, 0]
    

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
predatorstart = [10, -10, predatorsize/2]
preysize = 0.5
preystart = [1, 1, preysize/2]
duration = 100
groundsize = 50
predatorcount = 3
preycount = 2
randmax = 1000

predatorpositions = []
preypositions = []

predatorlist = []
preylist = []



if __name__ == '__main__':
    # print("\n\n-----------------------RUN BEGIN------------------------\n")

    t = 0

    frame = 0

    for i in range (predatorcount+preycount):
    
      if i<predatorcount:
        role = 'predator'
        startposition = [2, 2]
        walkspeed = 2
        viewdistance = 4
      else:
        role = 'prey'
        startposition = [8, 8]
        walkspeed = 10
        viewdistance = 5
  
      Actor = Actors()
      print("{} is {}, start position {}, walkspeed {}, viewdistance {}".format(Actor.id, Actor.role, Actor.startposition, Actor.walkspeed, Actor.viewdistance))





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
            predinstance.position = updateposition.updateposition(predinstance.position, movement)
            # print("Predator {} new position: {}".format(predinstance.id, predinstance.position))

        for preyinstance in preylist:
            # print("\nmoving prey {}".format(preyinstance.id))

            predatorspotted = checkforpredators.checkforpredators(preyinstance.position, preyinstance.viewdistance, predatorlist)

            if predatorspotted == [0, 0]:
                movement = weightedfreeroam.weightedfreeroam(preyinstance.last_movement, preyinstance.walkspeed)

            else:
                movement = runawaaay.runawaaay(preyinstance.position, preyinstance.walkspeed, predatorspotted)

            movement = boundarycheck.boundarycheck(predatorspotted, preyinstance.position, movement, groundsize, randmax)

            # print("previous position: {}".format(preyinstance.position))
            preyinstance.last_movement = movement
            preyinstance.position = updateposition.updateposition(preyinstance.position, movement)

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
