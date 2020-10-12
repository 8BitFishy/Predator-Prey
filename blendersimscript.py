import bpy
import random
from itertools import count
import os

dir = "C:/Users/Finn Sowerbutts/Documents/Work/Programming/Python/Predator-Prey/"

parameters = {}

with open("{}Parameters.txt".format(dir)) as f:
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

predatorstart = [int(parameters['predatorstartx']), int(parameters['predatorstarty']), predatorsize / 2]
preystart = [int(parameters['preystartx']), int(parameters['preystarty']), preysize / 2]

animation_length = 250
framerate = 5
predatorpositions = []
preypositions = []
predatorlist = []
preylist = []


class Predators:
    _ids = count(1)

    def __init__(self):
        self.id = next(self._ids)
        self.positions = []
        self.name = "Predator{}".format(self.id)
        self.predbody = bpy.data.objects["Cube"]


class Prey:
    _ids = count(1)

    def __init__(self):
        self.id = next(self._ids)
        self.positions = []
        self.name = "Prey{}".format(self.id)
        self.preybody = bpy.data.objects["Cube"]


os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':

    print("\n\n-----------------------RUN BEGIN------------------------\n\n")

    # Clear playing field and set animation length

    bpy.context.scene.frame_end = duration * framerate
    print(f"Duration = {duration}")

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    bpy.ops.object.select_all(action='DESELECT')

    # Initialise actors, assign numerical ID, append to actor list and assign vectors

    for i in range(predatorcount):

        bpy.ops.mesh.primitive_cube_add(size=predatorsize, enter_editmode=False, location=[0, 0, 0])

        predinstance = Predators()

        filename = ('{}vectors\Actorpredator{}vectors.txt'.format(dir, predinstance.id))

        with open(filename) as f:
            line = f.read().splitlines()
            for k in line:
                positions = k.split(',')
                for a in range(0, 3):
                    positions[a] = float(positions[a])
                predinstance.positions.append(positions)

        predinstance.predbody.name = predinstance.name

        print(f"Pred ID = {predinstance.id}\nPred start = {predinstance.positions[0]}")

        predatorlist.append(predinstance)

    for i in range(preycount):

        bpy.ops.mesh.primitive_cube_add(size=preysize, enter_editmode=False, location=[0, 0, 0])

        preyinstance = Prey()

        filename = ('{}vectors\Actorprey{}vectors.txt'.format(dir, preyinstance.id))
        with open(filename) as f:
            line = f.read().splitlines()
            for k in line:
                positions = k.split(',')
                for a in range(0, 3):
                    positions[a] = float(positions[a])
                preyinstance.positions.append(positions)

        preyinstance.preybody.name = preyinstance.name

        print(f"Prey ID = {preyinstance.id}\nPrey start = {preyinstance.positions[0]}")
        preylist.append(preyinstance)

    duration = len(predatorlist[0].positions)
    print(f"Duration = {duration}")

    # Generate and name actors

    bpy.ops.mesh.primitive_plane_add(size=groundsize, enter_editmode=False, location=(0, 0, 0))

    print("AQUI")

    # Assign vectors to actors for each frame

    frame_num = 0
    for i in range(0, duration):

        bpy.context.scene.frame_set(frame_num)
        print(f"Frame number - {frame_num}\n")

        for preyinstance in preylist:
            if len(preyinstance.positions) == i:
                print(f"Prey {preyinstance.id} DEAD!")
                del (preylist[preyinstance.id - 1])


            else:
                print(f"Prey instance {preyinstance.id} at position {preyinstance.positions[i]}")
                preyinstance.preybody.location = preyinstance.positions[i]
                preyinstance.preybody.keyframe_insert(data_path="location", index=-1)

        for predinstance in predatorlist:
            print(f"Pred instance {predinstance.id} at position {predinstance.positions[i]}")
            predinstance.predbody.location = predinstance.positions[i]
            predinstance.predbody.keyframe_insert(data_path="location", index=-1)

        frame_num += framerate



