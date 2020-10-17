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


if __name__ == '__main__':
    outputparams = {}
    with open("Outputparams.txt") as f:
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


    for files in os.walk("actors"):
        filelist = list(files[2])
        for file in filelist:
            actorstats = {}
            if "characteristics" in file:
                dir = os.path.join("actors/", file)
                with open(dir) as f:
                    for line in f:
                        name, value = line.split("=")
                        name = name.rstrip(" ")
                        actorstats[name] = value.rstrip('\n')

            id = actorstats["Actor Number"]
            role = actorstats["Actor role"]
            walkspeed = int(actorstats["Actor walkspeed"])
            viewdistance = int(actorstats["Actor viewdistance"])
            birth = int(actorstats["Actor birth"])
            death = int(actorstats["Actor death"])
            age = int(actorstats["Actor age"])
            lifespan = int(actorstats["Actor lifespan"])
            timesmated = int(actorstats["Offspring"])
            enemieseaten = int(actorstats["Enemies eaten"])
            longevity = int(actorstats["Actor longevity"])

            if 'eaten' in actorstats["Cause of death"]:
                causeofdeath = 1
            elif 'starvation' in actorstats["Cause of death"]:
                causeofdeath = 2
            elif 'old' in actorstats["Cause of death"]:
                causeofdeath = 3

            Actor = Actors(id, role, walkspeed, viewdistance, birth, death, age, lifespan, causeofdeath, timesmated, enemieseaten, longevity)
            actorlist.append(Actor)



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

        else:

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

    # field names
    fields = ['Round', 'Predator Pop', 'Prey Pop', 'av_predlifespan', 'av_preylifespan', 'av_predwalkspeed', 'av_preywalkspeed', 'av_predviewdistance', 'av_preyviewdistance']

    # name of csv file
    filename = "stats.csv"

    # writing to csv file
    with open(filename, 'w', newline = "") as csvfile:

        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        predpop = preypop = 0


        for i in range(duration):
            row = []
            av_predwalkspeed = 0
            av_preywalkspeed = 0
            av_predviewdistance = 0
            av_preyviewdistance = 0
            av_predlifespan = 0
            av_preylifespan = 0

            for Actor in actorlist:

                if Actor.death == -1:
                    Actor.death = duration + 1

                if i < Actor.birth or i > Actor.death:
                    continue

                else:

                    if Actor.birth == i:

                        if 'predator' in Actor.role:
                            predpop += 1


                        else:
                            preypop += 1

                    if Actor.death == i:
                        if 'predator' in Actor.role:
                            predpop -= 1


                        else:
                            preypop -= 1


                    elif i > Actor.birth or i < Actor.death:

                        if 'predator' in Actor.role:

                            av_predwalkspeed += Actor.walkspeed
                            av_predviewdistance += Actor.viewdistance
                            av_predlifespan += Actor.lifespan

                        else:

                            av_preywalkspeed += Actor.walkspeed
                            av_preyviewdistance += Actor.viewdistance
                            av_preylifespan += Actor.lifespan


            if predpop == 0:
                av_predlifespan = 0
                av_predviewdistance = 0
                av_predwalkspeed = 0

            else:
                av_predlifespan = av_predlifespan / predpop
                av_predviewdistance = av_predviewdistance / predpop
                av_predwalkspeed = av_predwalkspeed / predpop

            if preypop == 0:
                av_preylifespan = 0
                av_preyviewdistance = 0
                av_preywalkspeed = 0

            else:
                av_preylifespan = av_preylifespan / preypop
                av_preyviewdistance = av_preyviewdistance / preypop
                av_preywalkspeed = av_preywalkspeed / preypop


            row = [i, predpop, preypop, av_predlifespan, av_preylifespan, av_predwalkspeed, av_preywalkspeed, av_predviewdistance, av_preyviewdistance]

            csvwriter.writerow(row)


