import os
import csv


def print_log(log):

    newpath = 'log'

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    with open(f'{newpath}\\log.txt', 'w')as file_object:
        file_object.write(str(log))
        file_object.write("\n")

    return

def print_inputs(parameters):

    newpath = 'log'

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    with open(f'{newpath}\\Input Parameters.txt', 'w')as file_object:
        for x in parameters:
            file_object.write(str(f"{x} = {parameters[x]}"))
            file_object.write("\n")

    return


def populateoutputfiles(actorlist):

    for Actor in actorlist:

        newpath = 'vectors'

        if Actor.role == "plant":
            newpath = 'plantvectors'

        if not os.path.exists(newpath):
            os.makedirs(newpath)

        actoroutput = ('{}\\{} {} vectors.txt'.format(newpath, Actor.role, Actor.actorcount))


        with open(actoroutput, 'w')as file_object:


            file_object.write(str(Actor.birth))
            file_object.write("\n")
            file_object.write(str(Actor.death))
            file_object.write("\n")

            for i in Actor.vectors:

                for e in i:
                    file_object.write(str(e))
                    file_object.write(",")
                file_object.write(str(Actor.size / 2))
                file_object.write("\n")


    return




def output_characteristics(actorlist):

    newpath = 'actors'
    for Actor in actorlist:

        newpath = 'actors'

        if not os.path.exists(newpath):
            os.makedirs(newpath)


        actoroutput = ('{}\\{} {} - actor {} characteristics.txt'.format(newpath, Actor.role, Actor.actorcount, Actor.id))

        if Actor.causeofdeath == "":
            Actor.causeofdeath = "survived"

        with open(actoroutput, 'w')as file_object:
            if Actor.role != "plant":
                file_object.write(str(f"Actor ID = {Actor.id}"))
                file_object.write(str(f"\nActor role = {Actor.role}"))
                file_object.write(str(f"\nActor size = {Actor.size}"))
                file_object.write(str(f"\nActor walkspeed = {Actor.walkspeed}"))
                file_object.write(str(f"\nActor viewdistance = {Actor.viewdistance}"))
                file_object.write(str(f"\nActor longevity = {Actor.longevity}"))
                file_object.write(str(f"\nActor parent1 = {Actor.parent1}"))
                file_object.write(str(f"\nActor parent2 = {Actor.parent2}"))
                file_object.write(str(f"\nActor birth = {Actor.birth}"))
                file_object.write(str(f"\nActor death = {Actor.death}"))
                file_object.write(str(f"\nActor age = {Actor.age}"))
                file_object.write(str(f"\nActor lifespan = {Actor.lifespan}"))
                file_object.write(str(f"\nCause of death = {Actor.causeofdeath}"))
                file_object.write(str(f"\nOffspring = {Actor.timesmated}"))
                file_object.write(str(f"\nEnemies eaten = {Actor.enemieseaten}"))
            else:
                file_object.write(str(f"Actor ID = {Actor.id}"))
                file_object.write(str(f"\nActor role = {Actor.role}"))
                file_object.write(str(f"\nActor birth = {Actor.birth}"))
                file_object.write(str(f"\nActor death = {Actor.death}"))


    return()


def generate_learning_data(t, parameters):

    newpath = 'learning_data'

    if not os.path.exists(newpath):
        os.makedirs(newpath)
    filename = "learning_data.csv"
    #fields = ['Rounds']
    row = [t]

    for x in parameters:
        #fields.append(x)
        row.append(parameters[x])


    # writing to csv file
    with open(f"{newpath}//{filename}", 'a', newline="") as csvfile:

        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        #csvwriter.writerow(fields)


        csvwriter.writerow(row)
    return


def print_outputparams(predatortotal, preytotal, plantstotal, t):


    newpath = 'log'

    if not os.path.exists(newpath):
        os.makedirs(newpath)
    filename = "Outputparams.txt"

    with open(f'{newpath}\\{filename}', 'w')as f:
        f.write(str(f"Duration = {t}"))
        f.write(str(f"\ntotalpreds = {predatortotal}"))
        f.write(str(f"\ntotalprey = {preytotal}"))
        f.write(str(f"\ntotalplants = {plantstotal}"))
        f.close()

    return