import random
from itertools import count

def generate_actors(groundsize):

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
            self.lunge = walkspeed*2
            self.state = 1
            self.dying = 0
            self.hungry = 1
            self.longevity = longevity

    parameters = {}

    with open("Parameters.txt") as f:
        for line in f:
            name, value = line.split("=")
            name = name.rstrip(" ")
            parameters[name] = value.rstrip('\n')

    predatorsize = float(parameters["predatorsize"])
    preysize = float(parameters["preysize"])
    predatorcount = int(parameters["predatorcount"])
    preycount = int(parameters["preycount"])
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


    # initialise Actors and assign characteristics
    for i in range(predatorcount + preycount):
        startposition = [0, 0]
        role = 'prey'
        size = preysize
        walkspeed = preywalkspeed
        viewdistance = preyviewdistance
        longevity = 50


        if i >= preycount:
            role = 'predator'
            size = predatorsize
            for j in range(0, 2):
                startposition[j] = random.randint(int(-groundsize/2), int(groundsize/2))
            longevity = longevity + random.randint(-10, 10)
            walkspeed = predatorwalkspeed
            viewdistance = predatorviewdistance



        else:
            role = 'prey'
            size = preysize
            for j in range(0, 2):
                startposition[j] = random.randint(int(-groundsize/2), int(groundsize/2))
            walkspeed = preywalkspeed
            viewdistance = preyviewdistance


        # Create actors and print out list
        Actor = Actors()
        actorlist.append(Actor)

    return actorlist





