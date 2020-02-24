#import bpy
import random
from itertools import count
import os

predatorsize = 2
predatorstart = [10, -10, predatorsize/2]
framerate = 5
preysize = 0.5
preystart = [1, 1, preysize/2]
duration = 100
groundsize = 50
predatorcount = 1
preycount = 1
predatorpositions = []
preypositions = []
predatorlist = []
preylist = []

class Predators:
    def __init__(self):
        self.id = 0
        self.positions = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

class Prey:
    def __init__(self):
        self.id = 0
        self.positions = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]



newpath = r'vectors'


os.system('cls' if os.name == 'nt' else 'clear')



if __name__ == '__main__':
    

    
    print("\n\n-----------------------RUN BEGIN------------------------\n\n")

    
    for i in range(predatorcount):
        predinstance = Predators()
        print("Predator {} starting position: {}".format(predinstance.id, predinstance.positions))
        predatorlist.append(predinstance)

    for i in range(preycount):
        preyinstance = Prey()
        # print("Predator {} starting position: {}".format(predinstance.id, predinstance.position))
        preylist.append(preyinstance)



    for j in range(1, predatorcount+1):
        print(newpath)
        
        
        
        filename = ('{}\Actorpredator{}vectors.txt'.format(newpath, j))
        predinstance.id = j+1

        with open(filename) as f:
            line = f.read().splitlines()
            for k in line: 
                positions = k.split(',')
                for a in range (0, 3):
                    positions[a] = float(positions[a])
                print(positions)
                predinstance.positions.append(positions)




        

    for j in range(0, preycount):
        filename = ('\\vectors\\Actorprey{}vectors.txt'.format(j))
        preyinstance.id = j
        with open(filename) as f:
            line = f.read().splitlines()
            for k in line: 
                positions = k.split(',')
                for a in range (0, 3):
                    positions[a] = float(positions[a])
                preyinstance.positions.append(positions)
 
                print(preyinstance.positions)






    bpy.context.scene.frame_end = duration * framerate


    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete() 


    bpy.ops.mesh.primitive_plane_add(size = groundsize, enter_editmode = False, location = (0, 0, 0))
    
    
    print("AQUI")
    for preyinstance in preylist:
        print(preyinstance.positions)
    
    
    for i in range (0, preycount):
        bpy.ops.mesh.primitive_cube_add(size = preysize, enter_editmode = False, location = preystart)
        prey = bpy.data.objects["Cube"]
        prey.name = ("Prey{}".format(i))
     
    for i in range (0, predatorcount):   
        bpy.ops.mesh.primitive_cube_add(size = predatorsize, enter_editmode = False, location = predatorstart)
        predator = bpy.data.objects["Cube"]
        predator.name = ("Predator{}".format(i))


    frame_num = 0

    for i in range(duration):

        bpy.context.scene.frame_set(frame_num)
        
        for preyinstance in preylist:
            print("YOOOOOOOOOOOOOOOOO")
            print (preyinstance.positions)
            print("-------------HERE--------------")
            prey.location = preyinstance.positions[i]
            prey.keyframe_insert(data_path="location", index = -1)
            
        for predinstance in predatorlist:
            
            predator.location = predinstance.positions[i]
            predator.keyframe_insert(data_path="location", index = -1)
       
       
        frame_num += framerate/2
        print(frame_num)



        
        
