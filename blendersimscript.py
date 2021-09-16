import bpy
import random
from itertools import count
import os

dir = bpy.path.abspath("//")

parameters = {}
outputparams = {}

with open("{}Parameters.txt".format(dir)) as f:
    for line in f:
        if not line in ['\n', '\r\n']:
            name, value = line.split("=")
            name = name.rstrip(" ")
            parameters[name] = value.rstrip('\n')

predatorsize = float(parameters["predatorsize"])
preysize = float(parameters["preysize"])
plantsize = float(parameters["plantsize"])
groundsize = float(parameters["groundsize"])

animation_length = 250
framerate = 5
predatorpositions = []
preypositions = []
predatorlist = []
preylist = []
plantpositions = []
plantlist = []


class Predators:
    _ids = count(1)

    def __init__(self, name):
        self.id = next(self._ids)
        self.positions = []
        self.name = name
        self.predbody = bpy.data.objects["Cube"]


class Prey:
    _ids = count(1)

    def __init__(self, name):
        self.id = next(self._ids)
        self.positions = []
        self.name = name
        self.preybody = bpy.data.objects["Cube"]


class Plant:
    _ids = count(1)

    def __init__(self, name):
        self.id = next(self._ids)
        self.positions = []
        self.name = name
        self.plantbody = bpy.data.objects["Cube"]


os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':

    print("\n\n-----------------------RUN BEGIN------------------------\n\n")
    newpath = 'animation_data\\'
    # Get duration and actor counts
    with open(f"{dir}{newpath}animation_params.txt") as f:
        for line in f:
            name, value = line.split("=")
            name = name.rstrip(" ")
            outputparams[name] = value.rstrip('\n')

    duration = int(outputparams["Duration"])
    predatorcount = int(outputparams["totalpreds"])
    preycount = int(outputparams["totalprey"])
    plantcount = int(outputparams["totalplants"])

    # Clear playing field and set animation length

    bpy.context.scene.frame_end = duration * framerate
    print(f"Duration = {duration}")

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    bpy.ops.object.select_all(action='DESELECT')

    # Initialise actors, assign numerical ID, append to actor list and assign vectors

    c = 0

    for files in os.walk(f"{dir}{newpath}"):

        filelist = list(files[2])

        for file in filelist:
            if "vectors" in file:
                c += 1
                print(f"Generating actor {c} of {len(filelist)} - {int((c / len(filelist)) * 100)}%\n")
                with open(f"{dir}{newpath}{file}", "r") as f:
                    filename = file.split(" ")
                    actor_type = filename[0]
                    actor_number = filename[1]
                    line = f.read().splitlines()

                    if actor_type == 'predator':
                        bpy.ops.mesh.primitive_cube_add(size=predatorsize, enter_editmode=False, location=[0, 0, 0])
                        predinstance = Predators(str(f"{actor_type} {actor_number}"))

                        for k in line:
                            positions = k.split(',')
                            for a in range(0, 3):
                                positions[a] = float(positions[a])

                            predinstance.positions.append(positions)

                        predinstance.predbody.name = predinstance.name
                        predatorlist.append(predinstance)

                    elif actor_type == 'prey':
                        bpy.ops.mesh.primitive_cube_add(size=preysize, enter_editmode=False, location=[0, 0, 0])
                        preyinstance = Prey(str(f"{actor_type} {actor_number}"))

                        for k in line:
                            positions = k.split(',')
                            for a in range(0, 3):
                                positions[a] = float(positions[a])
                            preyinstance.positions.append(positions)

                        preyinstance.preybody.name = preyinstance.name
                        preylist.append(preyinstance)

                    elif actor_type == 'plant':
                        bpy.ops.mesh.primitive_cube_add(size=plantsize, enter_editmode=False, location=[0, 0, 0])
                        plantinstance = Plant(str(f"{actor_type} {actor_number}"))

                        for k in line:
                            positions = k.split(',')
                            for a in range(0, 3):
                                positions[a] = float(positions[a])
                            plantinstance.positions.append(positions)

                        plantinstance.plantbody.name = plantinstance.name
                        plantlist.append(plantinstance)

        # Generate and name actors

    bpy.ops.mesh.primitive_plane_add(size=groundsize + 10, enter_editmode=False, location=(0, 0, 0))

    # Assign vectors to actors for each frame

    frame_num = 0
    for i in range(0, duration):

        bpy.context.scene.frame_set(frame_num)
        print(f"Generating frame {i} of {duration}\n")

        for preyinstance in preylist:
            if len(preyinstance.positions) == i:
                del (preylist[preyinstance.id - 1])

            else:
                preyinstance.preybody.location = preyinstance.positions[i]
                preyinstance.preybody.keyframe_insert(data_path="location", index=-1)

        for predinstance in predatorlist:
            predinstance.predbody.location = predinstance.positions[i]
            predinstance.predbody.keyframe_insert(data_path="location", index=-1)

        for plantinstance in plantlist:
            plantinstance.plantbody.location = plantinstance.positions[i]
            plantinstance.plantbody.keyframe_insert(data_path="location", index=-1)

        frame_num += framerate



