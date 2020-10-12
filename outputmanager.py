import os

def populateoutputfiles(actorlist, dead):



    actorcount = 0
    preycount = 0
    predcount = 0

    newpath = 'vectors'

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    for Actor in actorlist:
        if Actor.role == "prey":
            preycount += 1
            actorcount = preycount
        else:
            predcount += 1
            actorcount = predcount

        actoroutput = ('{}\\Actor{}{}vectors.txt'.format(newpath, Actor.role, actorcount))

        if Actor.alive == 1:
            Actor.position.append(Actor.size/2)
        else:
            Actor.position.append(dead[1])

        
        with open(actoroutput, 'a')as file_object:

            for e in range(0, 3):
                file_object.write(str(Actor.position[e]))
                if e != 2:
                    file_object.write(",")
            file_object.write("\n")

            del Actor.position[2]






