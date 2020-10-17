import os

def print_log(log):

    newpath = 'log'

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    with open(f'{newpath}\\log.txt', 'a')as file_object:
        file_object.write(str(log))
        file_object.write("\n")



def populateoutputfiles(actorlist, dead):
    actorcount = 0
    preycount = 0
    predcount = 0
    plantcount = 0



    for Actor in actorlist:

        newpath = 'vectors'

        if Actor.role == "prey":
            preycount += 1
            actorcount = preycount
        elif Actor.role == 'predator':
            predcount += 1
            actorcount = predcount

        else:
            plantcount += 1
            actorcount = plantcount
            newpath = 'plantvectors'

        if not os.path.exists(newpath):
            os.makedirs(newpath)

        actoroutput = ('{}\\{}{}vectors.txt'.format(newpath, Actor.role, actorcount))

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



def backfill_vectors(actorlist, t, dead):

    actorcount = 0
    preycount = 0
    predcount = 0
    position = dead
    plantcount = 0
    newpath = 'vectors'

    if actorlist[-1].role == 'plant':
        newpath = 'plantvectors'

    else:
        newpath = 'vectors'

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    for Actor in actorlist:

        if (actorlist[-1].role == Actor.role):

            if actorlist[-1].role == 'predator':
                predcount += 1
                actorcount = predcount

            elif actorlist[-1].role == 'prey':
                preycount += 1
                actorcount = preycount

            else:
                plantcount += 1
                actorcount = plantcount


    actoroutput = ('{}\\{}{}vectors.txt'.format(newpath, Actor.role, actorcount))



    for i in range(0, t):

        if i < t:
            position = dead
            position.append(dead[1])
        else:
            position = Actor.position
            position.append(Actor.size / 2)
        with open(actoroutput, 'a')as file_object:
            for e in range(0, 3):
                file_object.write(str(position[e]))
                if e != 2:
                    file_object.write(",")
            file_object.write("\n")

            del position[2]


def output_characteristics(actorlist):

    newpath = 'actors'
    actorcount = preycount = predcount = plantcount = 0


    for Actor in actorlist:

        newpath = 'actors'

        if Actor.role == "prey":
            preycount += 1
            actorcount = preycount
        elif Actor.role == 'predator':
            predcount += 1
            actorcount = predcount

        else:
            plantcount += 1
            actorcount = plantcount
            newpath = 'plantactors'

        if not os.path.exists(newpath):
            os.makedirs(newpath)


        actoroutput = ('{}\\{}{} - actor {} characteristics.txt'.format(newpath, Actor.role, actorcount, Actor.id))

        if Actor.causeofdeath == "":
            Actor.causeofdeath = "survived"

        with open(actoroutput, 'a')as file_object:
            if Actor.role != "plant":
                file_object.write(str(f"Actor Number = {Actor.id}"))
                file_object.write(str(f"\nActor role = {Actor.role}"))
                file_object.write(str(f"\nActor size = {Actor.size}"))
                file_object.write(str(f"\nActor walkspeed = {Actor.walkspeed}"))
                file_object.write(str(f"\nActor viewdistance = {Actor.viewdistance}"))
                file_object.write(str(f"\nActor longevity = {Actor.longevity}"))
                file_object.write(str(f"\nActor birth = {Actor.birth}"))
                file_object.write(str(f"\nActor parent1 = {Actor.parent1}"))
                file_object.write(str(f"\nActor parent2 = {Actor.parent2}"))
                file_object.write(str(f"\nActor death = {Actor.death}"))
                file_object.write(str(f"\nActor age = {Actor.age}"))
                file_object.write(str(f"\nActor lifespan = {Actor.lifespan}"))
                file_object.write(str(f"\nCause of death = {Actor.causeofdeath}"))
                file_object.write(str(f"\nOffspring = {Actor.timesmated}"))
                file_object.write(str(f"\nEnemies eaten = {Actor.enemieseaten}"))
            else:
                file_object.write(str(f"Actor Number = {Actor.id}"))
                file_object.write(str(f"\nActor role = {Actor.role}"))
                file_object.write(str(f"\nActor birth = {Actor.birth}"))
                file_object.write(str(f"\nActor death = {Actor.death}"))


    return()



def print_outputparams(actorlist, t):
    totalpreds = 0
    totalprey = 0
    totalplants = 0

    for Actor in actorlist:
        if Actor.role == 'predator':
            totalpreds += 1
        elif Actor.role == 'prey':
            totalprey += 1
        else:
            totalplants += 1

    f = open("Outputparams.txt", "w")
    f.write(str(f"Duration = {t}"))
    f.write(str(f"\ntotalpreds = {totalpreds}"))
    f.write(str(f"\ntotalprey = {totalprey}"))
    f.write(str(f"\ntotalplants = {totalplants}"))
    f.close()
