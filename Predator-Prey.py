#import bpy
import random
from itertools import count


class Predators:  # Python3 defaults to using object in classes  so you don't need to pass it in as a param in the class

    _ids = count(0)

    def __init__(self):
        self.id = next(self._ids)
        self.position = predatorstart
        self.walkspeed = 5


class Prey:  # Python3 defaults to using object in classes  so you don't need to pass it in as a param in the class

    _ids = count(0)

    def __init__(self):
        self.id = next(self._ids)
        self.position = preystart
        self.walkspeed = 2
        self.state = 1


predatorsize = 2
predatorstart = [10, -10, predatorsize / 2]
framerate = 5
preysize = 0.5
preystart = [1, 1, preysize / 2]
duration = 100
groundsize = 50
predatorcount = 1
preycount = 1
randmax = 1000
preyviewdistance = 10

predatorpositions = []
preypositions = []


def freeroam(walkspeed):
    movement = [0, 0]
    randdir = random.randint(1, randmax)
    if randdir <= randmax / 8:
        movement[0] += walkspeed
        # print("X+")
    elif randdir > randmax / 8 and randdir <= 2 * (randmax / 8):
        movement[0] += walkspeed
        movement[1] += walkspeed
        # print("X-")
    elif randdir > 2 * (randmax / 8) and randdir <= 3 * (randmax / 8):
        movement[0] += walkspeed
        movement[1] -= walkspeed

    elif randdir > 3 * (randmax / 8) and randdir <= 4 * (randmax / 8):
        movement[0] -= walkspeed
        movement[1] -= walkspeed

    elif randdir > 4 * (randmax / 8) and randdir <= 5 * (randmax / 8):
        movement[0] -= walkspeed
        movement[1] += walkspeed

    elif randdir > 5 * (randmax / 8) and randdir <= 6 * (randmax / 8):
        movement[0] -= walkspeed

    elif randdir > 6 * (randmax / 8) and randdir <= 7 * (randmax / 8):
        movement[1] += walkspeed

    else:
        movement[1] -= walkspeed
        # print("Y-")

    return movement


def boundarycheck(predatorspotted, position, movement, groundsize):
    stuck = 0
    overflow = 0
    # print("\n-------Start boundary check-------")
    # print("Starting Position: {}".format(position))
    # print("Attempting movement: {}\n".format(movement))
    pathfound = 0

    while True:

        if abs(position[0] + movement[0]) > groundsize / 2:

            if position[0] <= 0:
                overflow = position[0] + movement[0] + overflow + groundsize / 2
            else:
                overflow = position[0] + movement[0] + overflow - groundsize / 2

            # print("Predator spotted at: {}".format(predatorspotted))

            pathfound = 1

            while pathfound != 0:
                # print("overflow x = {}".format(overflow))
                randoverflow = random.randint(1, randmax)

                if predatorspotted[0] == 0:
                    movement[0] = - movement[0]
                    # print("state 3: {}".format(movement))
                    pathfound = 0

                elif randoverflow <= randmax / 3 and predatorspotted[1] <= 0:
                    movement[0] = movement[0] - overflow
                    movement[1] = movement[1] - overflow
                    # print("state 1: {}".format(movement))
                    pathfound = 0

                elif randoverflow > randmax / 3 and randoverflow < 2 * randmax / 3 and predatorspotted[1] >= 0:
                    movement[0] = movement[0] - overflow
                    movement[1] = movement[1] + overflow
                    # print("state 2: {}".format(movement))
                    pathfound = 0

                elif predatorspotted[0] != 0 and predatorspotted[1] != 0:
                    # print("CORNERED1")
                    movement[0] = movement[0] - overflow
                    pathfound = 0

            overflow = 0
            # print("movementupdate = {}\n".format(movement))

        if abs(position[1] + movement[1]) > groundsize / 2:

            if position[1] <= 0:
                overflow = position[1] + movement[1] + overflow + groundsize / 2
            else:
                overflow = position[1] + movement[1] + overflow - groundsize / 2

            # print("Predator spotted at: {}".format(predatorspotted))
            pathfound = 1

            while pathfound != 0:
                # print("overflow y = {}".format(overflow))
                randoverflow = random.randint(1, randmax)

                if predatorspotted[1] == 0:
                    movement[1] = - movement[1]
                    # print("state 6: {}".format(movement))
                    pathfound = 0

                elif randoverflow <= randmax / 3 and predatorspotted[0] <= 0:
                    movement[1] = movement[1] - overflow
                    movement[0] = movement[0] - overflow
                    # print("state 4: {}".format(movement))
                    pathfound = 0

                elif randoverflow > randmax / 3 and randoverflow < 2 * randmax / 3 and predatorspotted[0] >= 0:
                    movement[1] = movement[1] - overflow
                    movement[0] = movement[0] + overflow
                    # print("state 5: {}".format(movement))
                    pathfound = 0



                elif predatorspotted[0] != 0 and predatorspotted[1] != 0:
                    # print("CORNERED")
                    movement[1] = movement[1] - overflow
                    pathfound = 0

            overflow = 0
            # print("movementupdate = {}\n".format(movement))



        else:
            # print("no overflow")
            overflow = 0

        # print("Position: {}, Movement: {}".format(position, movement))

        if overflow == 0 and abs(movement[0] + position[0]) <= groundsize / 2 and abs(
                movement[1] + position[1]) <= groundsize / 2:
            break

        elif stuck > 10:
            movement = [0, 0]
            break

        else:
            stuck += 1
            # print("Stuck! = : {}".format(stuck))

    return movement


def updateposition(position, movement):
    position[0] = position[0] + movement[0]
    position[1] = position[1] + movement[1]

    return position


def checkforpredators(position, predatorlist):
    for predinstance in predatorlist:
        moveaway = [0, 0]
        xcheck = predinstance.position[0] - position[0]
        ycheck = predinstance.position[1] - position[1]
        if abs(xcheck) < preyviewdistance and abs(ycheck) < preyviewdistance:
            if abs(xcheck) < preyviewdistance:

                if xcheck < 0:
                    moveaway[0] = 1 * 0.5 * (preyviewdistance - xcheck)

                else:
                    moveaway[0] = -1 * 0.5 * (preyviewdistance - xcheck)

            if abs(ycheck) < preyviewdistance:
                if ycheck < 0:
                    moveaway[1] = 1 * 0.5 * (preyviewdistance - ycheck)

                else:
                    moveaway[1] = -1 * 0.5 * (preyviewdistance - ycheck)

        print("preylocation: {}, predatorlocation: {}, preyviewdistance: {}, moveaway: {}".format(position,
                                                                                                  predinstance.position,
                                                                                                  preyviewdistance,
                                                                                                  moveaway))
        return moveaway


def runawaaay(position, walkspeed, predatorspotted):
    movement = [0, 0]

    for i in range(2):
        movement[i] = predatorspotted[i] * walkspeed
    return movement


predatorlist = []
preylist = []

if __name__ == '__main__':
    # print("\n\n-----------------------RUN BEGIN------------------------\n")

    for i in range(predatorcount):
        predinstance = Predators()
        # print("Predator {} starting position: {}".format(predinstance.id, predinstance.position))
        predatorlist.append(predinstance)

    for i in range(preycount):
        preyinstance = Prey()
        # print("Prey {} starting position: {}".format(preyinstance.id, preyinstance.position))
        preylist.append(preyinstance)

    t = 0

    frame = 0

    while t < duration:

        for predinstance in predatorlist:
            predatorspotted = [0, 0]
            # print("\n\nmoving predator {}".format(predinstance.id))
            movement = freeroam(predinstance.walkspeed)
            # print("movement = {}".format(movement))
            # print("previous position: {}".format(predinstance.position))
            movement = boundarycheck(predatorspotted, predinstance.position, movement, groundsize)
            predinstance.position = updateposition(predinstance.position, movement)
            # print("Predator {} new position: {}".format(predinstance.id, predinstance.position))

        for preyinstance in preylist:
            # print("\nmoving prey {}".format(preyinstance.id))

            predatorspotted = checkforpredators(preyinstance.position, predatorlist)

            if predatorspotted == [0, 0]:
                movement = freeroam(preyinstance.walkspeed)
                preyinstance.state = 1

            else:
                movement = runawaaay(preyinstance.position, preyinstance.walkspeed, predatorspotted)
                preyinstance.state = 0

            movement = boundarycheck(predatorspotted, preyinstance.position, movement, groundsize)

            # print("previous position: {}".format(preyinstance.position))

            preyinstance.position = updateposition(preyinstance.position, movement)

            # print("New position: {}".format(preyinstance.position))

        # print("\n\nloop end positions:\n")
        for predinstance in predatorlist:
            predatorpositions.append(predinstance.position[:])
        for preyinstance in preylist:
            preypositions.append(preyinstance.position[:])

        t += 1


for predator in predatorlist:
    filename = ('pred{}vectors.txt'.format(predinstance.id))
    with open(filename, 'w') as file_object:
        for e in range (0, duration):
            stringout = str(predatorpositions[e])
            file_object.write("{}\n".format(predatorpositions[e]))



for prey in preylist:
    filename = ('prey{}vectors.txt'.format(preyinstance.id))
    with open(filename, 'w') as file_object:
        for e in range (0, duration):
            stringout = str(preypositions[e])

            file_object.write("{}\n".format(preypositions[e]))






#BLENDER SEGMENT STARTS HERE



'''
print(predatorpositions)
print("\n\n\n\n")
print(preypositions)

bpy.context.scene.frame_end = duration * framerate

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

bpy.ops.mesh.primitive_plane_add(size=groundsize, enter_editmode=False, location=(0, 0, 0))
bpy.ops.mesh.primitive_cube_add(size=preysize, enter_editmode=False, location=preystart)
bpy.ops.mesh.primitive_cube_add(size=predatorsize, enter_editmode=False, location=predatorstart)

prey = bpy.data.objects["Cube"]
predator = bpy.data.objects["Cube.001"]

frame_num = 0

for i in range(duration):
    preyposition = (preypositions[i])
    predposition = (predatorpositions[i])
    bpy.context.scene.frame_set(frame_num)

    prey.location = preyposition
    predator.location = predposition

    prey.keyframe_insert(data_path="location", index=-1)
    frame_num += framerate / 2
    print(frame_num)
    predator.keyframe_insert(data_path="location", index=-1)

    frame_num += framerate / 2
    print(frame_num)

'''