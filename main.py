import weightedfreeroam
import checkforpredators
import boundarycheck
import updateposition
import runawaaay
import outputmanager
import clearvectorfiles
import checkforwinner
import generate_actors
import overlapcheck
import os


parameters = {}

with open("Parameters.txt") as f:
    for line in f:
        name, value = line.split("=")
        name = name.rstrip(" ")
        parameters[name] = value.rstrip('\n')

duration = 0
groundsize = float(parameters["groundsize"])
predatorcount = int(parameters["predatorcount"])
preycount = int(parameters["preycount"])
randmax = int(parameters["randmax"])

actorlist = []
dead = [9000, 9000]
predatorsleft = 0
preyleft = 0

#_________________________Start of main simulation___________________________

if __name__ == '__main__':


    clearvectorfiles.clearvectorfiles()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n-----------------------RUN BEGIN------------------------\n")

    t = 0

    actorlist = generate_actors.generate_actors(groundsize)
    for Actor in actorlist:
        if Actor.role == 'predator':
            predatorsleft += 1
        elif Actor.role == 'prey':
            preyleft += 1
    print(f"{predatorsleft} predators and {preyleft} prey")
    #print("\n\nActors generated\n\n")

    for Actor in actorlist:
        print(f"Actor {Actor.id} operating as {Actor.role} starts game at position {Actor.position}")

    while preyleft != 0 and predatorsleft != 0:
        print("\n------------Round {}, frame {}------------\n".format(t, t*5))



        #Generate movement vectors for

        for Actor in actorlist:

            if Actor.dying == 1:
                print(f"Actor{Actor.id} state = {Actor.state}, dying = {Actor.dying}")
                Actor.state = 0
                Actor.dying = 0

            if Actor.state == 0:
                Actor.position = dead
                continue

            if Actor.hungry > Actor.longevity:
                print(f"{Actor.role}{Actor.id} dies of starvation")
                Actor.dying = 1
                predatorsleft -= 1
                continue

            if Actor.hungry != 0 and Actor.dying != 1:
                winner = [0, 0]
                #Check for enemigos, return vector for nearest enemy or 0, 0 if none found
                predatorspotted = checkforpredators.checkforpredators(Actor.position, Actor.viewdistance, actorlist, Actor.role)

                #if no enemigo found, movement is freeroam
                if predatorspotted == [0, 0]:

                    movement = weightedfreeroam.weightedfreeroam(Actor.lastmovement, Actor.walkspeed)

                #if enemy found, react accordingly, output a movement vector
                else:

                    #if actor is a predator, invert movement into chase
                    if Actor.role == "predator":
                        for i in range(2):
                            predatorspotted[i] = predatorspotted[i]*-1

                    #convert spotted enemy vector to movement vector
                    movement = runawaaay.runawaaay(Actor.walkspeed, predatorspotted, Actor.viewdistance)


                #if actor is a predator, check for enemies within lunge distance and return a movement
                if Actor.role == 'predator':
                    winner = checkforwinner.checkforwinner(Actor.position, actorlist, Actor.lunge)

                    #if enemy within lunge distance is found, move predator to prey position and delete prey
                    if winner[0] == 1:
                        print(f"{actorlist[winner[1]].role}{actorlist[winner[1]].id} killed")
                        for i in range(2):
                            movement[i] = actorlist[winner[1]].position[i] - Actor.position[i]
                        actorlist[winner[1]].dying = 1
                        print(f"Actor{actorlist[winner[1]].id} dying = {actorlist[winner[1]].dying}")
                        preyleft -= 1
                        Actor.hungry = 0

                    else:
                        Actor.hungry += 1

            else:
                movement = [0, 0]

                if Actor.dying != 1:
                    Actor.hungry = 1

            #check for wall and update movement accordingly

            movement = overlapcheck.overlapcheck(actorlist, Actor.position, movement, Actor.role, randmax, Actor.size, Actor.id, Actor.walkspeed)
            movement = boundarycheck.boundarycheck(predatorspotted, Actor.position, movement, groundsize, randmax)
            #update actor position
            Actor.position = updateposition.updateposition(Actor.position, movement)
            Actor.lastmovement = movement

        #write vectors to vector files
        outputmanager.populateoutputfiles(actorlist, dead)

        t += 1


    survivors = 0
    for Actor in actorlist:
        if Actor.role == 'prey' and Actor.state == 1:
            survivors += 1
    if survivors > 0:
        print(f"\n\n{survivors} prey escaped")

        print(f"\n\n{preyleft} prey escaped")

    else:
        print("\n\nPredators Wins")

    print(f"\n{t} rounds played")

    f = open("Duration.txt", "w")
    f.write(str(t))
    f.close()





