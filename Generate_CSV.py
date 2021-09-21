import csv
from itertools import count
import os

class Actors:
    _ids = count(0)

    def __init__(self, id, role, walkspeed, viewdistance, birth, death, age, lifespan, causeofdeath, timesmated, enemieseaten, longevity):
        self.id = id
        self.role = role
        self.walkspeed = walkspeed
        self.viewdistance = viewdistance
        self.longevity = longevity
        self.birth = birth
        self.death = death
        self.age = age
        self.lifespan = lifespan
        self.causeofdeath = causeofdeath
        self.timesmated = timesmated
        self.enemieseaten = enemieseaten


def Generate_CSV():
    outputparams = {}
    newpath = 'log'
    filename = "Outputparams.txt"

    with open(f'{newpath}\\{filename}') as f:
        for line in f:
            name, value = line.split("=")
            name = name.rstrip(" ")
            outputparams[name] = value.rstrip('\n')

    duration = int(outputparams["Duration"])
    predatorcount = int(outputparams["totalpreds"])
    preycount = int(outputparams["totalprey"])
    plantcount = int(outputparams["totalplants"])
    actorlist = []
    preynum = prednum = 0

    directory = "actors"

    for files in os.walk(directory):
        filelist = list(files[2])
        for file in filelist:
            actorstats = {}

            if "characteristics" in file:
                dir = os.path.join(f"{directory}/", file)
                with open(dir) as f:
                    for line in f:
                        name, value = line.split("=")
                        name = name.rstrip(" ")
                        actorstats[name] = value.rstrip('\n')

            id = actorstats["Actor ID"]
            role = actorstats["Actor role"]
            birth = int(actorstats["Actor birth"])
            death = int(actorstats["Actor death"])

            if 'plant' not in role:
                walkspeed = int(actorstats["Actor walkspeed"])
                viewdistance = int(actorstats["Actor viewdistance"])
                lifespan = int(actorstats["Actor lifespan"])
                timesmated = int(actorstats["Offspring"])
                enemieseaten = int(actorstats["Enemies eaten"])
                longevity = int(actorstats["Actor longevity"])
                age = int(actorstats["Actor age"])
                if 'eaten' in actorstats["Cause of death"]:
                    causeofdeath = 1
                elif 'starvation' in actorstats["Cause of death"]:
                    causeofdeath = 2
                elif 'old' in actorstats["Cause of death"]:
                    causeofdeath = 3
                else:
                    causeofdeath = 0

            else:
                walkspeed = 0
                viewdistance = 0
                lifespan = 0
                timesmated = 0
                enemieseaten = 0
                longevity = 0
                age = 0
                causeofdeath = -1






            Actor = Actors(id, role, walkspeed, viewdistance, birth, death, age, lifespan, causeofdeath, timesmated, enemieseaten, longevity)
            actorlist.append(Actor)


    predeaten = predstarved = predold = 0
    preyeaten = preystarved = preyold = 0
    preylongestlifeactor = 0
    predlongestlifeactor = 0
    preyfastestactor = 0
    predfastestactor = 0
    preyhungriestactor = 0
    predhungriestactor = 0
    preyhorniestactor = 0
    predhorniestactor = 0
    predmostlongevityactor = 0
    preymostlongevityactor = 0
    predfastest = predoldest = predhungriest = predhorniest = predlongevist = 0
    preyfastest = preyoldest = preyhungriest = preyhorniest = preylongevist = 0
    predsborn = preyborn = 0

    for Actor in actorlist:

        if 'predator' in Actor.role:

            if Actor.walkspeed > predfastest:
                predfastestactor = Actor.id
                predfastest = Actor.walkspeed

            if Actor.age > predoldest:
                predlongestlifeactor = Actor.id
                predoldest = Actor.age

            if Actor.enemieseaten > predhungriest:
                predhungriestactor = Actor.id
                predhungriest = Actor.enemieseaten

            if Actor.timesmated > predhorniest:
                predhorniestactor = Actor.id
                predhorniest = Actor.timesmated

            if Actor.longevity > predlongevist:
                predmostlongevityactor = Actor.id
                predlongevist = Actor.longevity

            if Actor.causeofdeath == 1:
                predeaten += 1
            elif Actor.causeofdeath == 2:
                predstarved += 1
            elif Actor.causeofdeath == 3:
                predold += 1

            if Actor.birth != 0:
                predsborn += 1

        elif 'prey' in Actor.role:

            if Actor.walkspeed > preyfastest:
                preyfastestactor = Actor.id
                preyfastest = Actor.walkspeed

            if Actor.age > preyoldest:
                preylongestlifeactor = Actor.id
                preyoldest = Actor.age

            if Actor.enemieseaten > preyhungriest:
                preyhungriestactor = Actor.id
                preyhungriest = Actor.enemieseaten

            if Actor.timesmated > preyhorniest:
                preyhorniestactor = Actor.id
                preyhorniest = Actor.timesmated

            if Actor.longevity > preylongevist:
                preymostlongevityactor = Actor.id
                preylongevist = Actor.longevity

            if Actor.causeofdeath == 1:
                preyeaten += 1
            elif Actor.causeofdeath == 2:
                preystarved += 1
            elif Actor.causeofdeath == 3:
                preyold += 1

            if Actor.birth != 0:
                preyborn += 1

    print(f"Fastest predator = {predfastestactor} with speed {predfastest}")
    print(f"Fastest prey = {preyfastestactor} with speed {preyfastest}")

    print(f"Hungriest predator = {predhungriestactor} with {predhungriest} eaten enemies")
    print(f"Hungriest prey = {preyhungriestactor} with {preyhungriest} eaten plants")

    print(f"Horniest predator = {predhorniestactor} with {predhorniest} offspring")
    print(f"Horniest prey = {preyhorniestactor} with {preyhorniest} offspring")

    print(f"Oldest predator = {predlongestlifeactor} at {predoldest} rounds")
    print(f"Oldest prey = {preylongestlifeactor} at {preyoldest} rounds")

    print(f"Predator with most longevity = {predmostlongevityactor} at {predlongevist} rounds")
    print(f"Prey with most longevity = {preymostlongevityactor} at {preylongevist} rounds")

    print(f"Predators born = {predsborn}")
    print(f"Predators died of starvation = {predstarved}")
    print(f"Predators died of old age = {predold}")

    print(f"Prey born = {preyborn}")
    print(f"Prey eaten = {preyeaten}")
    print(f"Prey died of starvation = {preystarved}")
    print(f"Prey died of old age = {preyold}")

    filename = "Sim Actor Stats.txt"

    newpath = 'log'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    with open(f'{newpath}\\Actor Stats.txt', 'w')as f:
        f.write(str((f"Fastest predator = {predfastestactor} with speed {predfastest}")))
        f.write(str((f"\nFastest prey = {preyfastestactor} with speed {preyfastest}")))
        f.write(str((f"\nHungriest predator = {predhungriestactor} with {predhungriest} eaten enemies")))
        f.write(str((f"\nHungriest prey = {preyhungriestactor} with {preyhungriest} eaten plants")))
        f.write(str((f"\nHorniest predator = {predhorniestactor} with {predhorniest} offspring")))
        f.write(str((f"\nHorniest prey = {preyhorniestactor} with {preyhorniest} offspring")))
        f.write(str((f"\nOldest predator = {predlongestlifeactor} at {predoldest} rounds")))
        f.write(str((f"\nOldest prey = {preylongestlifeactor} at {preyoldest} rounds")))
        f.write(str((f"\nPredator with most longevity = {predmostlongevityactor} at {predlongevist} rounds")))
        f.write(str((f"\nPrey with most longevity = {preymostlongevityactor} at {preylongevist} rounds\n\n")))
        f.write(str((f"\nPredators born = {predsborn}")))
        f.write(str((f"\nPredators died of starvation = {predstarved}")))
        f.write(str((f"\nPredators died of old age = {predold}")))
        f.write(str((f"\nPrey born = {preyborn}")))
        f.write(str((f"\nPrey eaten = {preyeaten}")))
        f.write(str((f"\nPrey died of starvation = {preystarved}")))
        f.write(str((f"\nPrey died of old age = {preyold}")))



    # field names
    fields = ['Round', 'Predator Pop', 'Prey Pop', 'Plant pop', 'predstarved', 'predold', 'preyeaten', 'preystarved', 'preyold', 'av_predlifespan', 'av_preylifespan', 'av_predage', 'av_preyage',  'av_predwalkspeed', 'av_preywalkspeed', 'av_predviewdistance', 'av_preyviewdistance']

    # name of csv file
    filename = "Stats.csv"
    # writing to csv file
    with open(f"{newpath}//{filename}", 'w', newline = "") as csvfile:

        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        predpop = preypop = plantpop = 0
        predeaten = predstarved = predold = 0
        preyeaten = preystarved = preyold = 0

        for i in range(duration):

            row = []
            av_predwalkspeed = 0
            av_preywalkspeed = 0
            av_predviewdistance = 0
            av_preyviewdistance = 0
            av_predlifespan = 0
            av_preylifespan = 0
            av_predage = 0
            av_preyage = 0
#            predstarved = predold = 0
#            preyeaten = preyold = preystarved = 0

            for Actor in actorlist:

                if Actor.death == -1:
                    Actor.death = duration + 1

                if i < Actor.birth or i > Actor.death:
                    continue

                else:


                    if Actor.birth == i:

                        if 'predator' in Actor.role:
                            predpop += 1


                        elif 'prey' in Actor.role:
                            preypop += 1

                        else:
                            plantpop += 1

                    if Actor.death == i:
                        if 'predator' in Actor.role:
                            predpop -= 1
                            if Actor.causeofdeath == 1:
                                predeaten += 1
                            elif Actor.causeofdeath == 2:
                                predstarved += 1
                            elif Actor.causeofdeath == 3:
                                predold += 1

                        elif 'prey' in Actor.role:
                            preypop -= 1
                            if Actor.causeofdeath == 1:
                                preyeaten += 1
                            elif Actor.causeofdeath == 2:
                                preystarved += 1
                            elif Actor.causeofdeath == 3:
                                preyold += 1

                        else:
                            plantpop -= 1


                    elif i > Actor.birth or i < Actor.death:

                        if 'predator' in Actor.role:

                            av_predwalkspeed += Actor.walkspeed
                            av_predviewdistance += Actor.viewdistance
                            av_predlifespan += Actor.lifespan
                            if Actor.birth == 0:
                                av_predage += Actor.age
                            else:
                                av_predage += (i - Actor.birth)


                        elif 'prey' in Actor.role:

                            av_preywalkspeed += Actor.walkspeed
                            av_preyviewdistance += Actor.viewdistance
                            av_preylifespan += Actor.lifespan
                            if Actor.birth == 0:
                                av_preyage += Actor.age
                            else:
                                av_preyage += (i - Actor.birth)


            if predpop == 0:
                av_predlifespan = 0
                av_predviewdistance = 0
                av_predwalkspeed = 0
                av_predage = 0

            else:
                av_predlifespan = av_predlifespan / predpop
                av_predviewdistance = av_predviewdistance / predpop
                av_predwalkspeed = av_predwalkspeed / predpop
                av_predage = av_predage / predpop


            if preypop == 0:
                av_preylifespan = 0
                av_preyviewdistance = 0
                av_preywalkspeed = 0
                av_preyage = 0

            else:
                av_preylifespan = av_preylifespan / preypop
                av_preyviewdistance = av_preyviewdistance / preypop
                av_preywalkspeed = av_preywalkspeed / preypop
                av_preyage = av_preyage / preypop
            row = [i, predpop, preypop, plantpop,  predstarved, predold, preyeaten, preystarved, preyold, av_predlifespan, av_preylifespan, av_predage, av_preyage, av_predwalkspeed, av_preywalkspeed, av_predviewdistance, av_preyviewdistance]

            csvwriter.writerow(row)

    return

if __name__ == '__main__':
    Generate_CSV()
