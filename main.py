import weightedfreeroam
import checkforpredators
import boundarycheck
import updateposition
import runawaaay
import outputmanager
import clearvectorfiles
import checkforwinner
import generate_actors
import os


parameters = {}

with open("Parameters.txt") as f:
    for line in f:
        name, value = line.split("=")
        name = name.rstrip(" ")
        parameters[name] = value.rstrip('\n')

duration = int(parameters["duration"])
groundsize = float(parameters["groundsize"])
predatorcount = int(parameters["predatorcount"])
preycount = int(parameters["preycount"])
randmax = int(parameters["randmax"])

actorlist = []



#_________________________Start of main simulation___________________________

if __name__ == '__main__':


    clearvectorfiles.clearvectorfiles()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n-----------------------RUN BEGIN------------------------\n")

    t = 0



    actorlist = generate_actors.generate_actors()

    #print("\n\nActors generated\n\n")
    winner = [0, 0]
    for Actor in actorlist:
        print(f"Actor {Actor.id} operating as {Actor.role} starts game at position {Actor.position}")

    while t < duration and winner[0] != 1:
        print("\n------------Round {}------------\n".format(t))

        for Actor in actorlist:
            print(f"Actor {Actor.id} in role {Actor.role} starting round at position {Actor.position}")
        print("")
        for Actor in actorlist:

            predatorspotted = checkforpredators.checkforpredators(Actor.position, Actor.viewdistance, actorlist, Actor.role)

            if predatorspotted == [0, 0]:
                if Actor.role == "prey":
                    print("Prey {} safe".format(Actor.id))
                else:
                    print(f"Predator {Actor.id} can't see food")

                movement = weightedfreeroam.weightedfreeroam(Actor.lastmovement, Actor.walkspeed)

                print(f"Movement for actor {Actor.id} in weighted freeroam = {movement}")

            else:
                print("{}{} spots enemy at {}\n".format(Actor.role, Actor.id, predatorspotted))

                if Actor.role == "predator":
                    for i in range(2):
                        predatorspotted[i] = predatorspotted[i]*-1

                movement = runawaaay.runawaaay(Actor.walkspeed, predatorspotted, Actor.viewdistance)

                if Actor.role == "prey":
                    print("\n\n\n{}{} running from predator at  vector {} with movement {}".format(Actor.role, Actor.id, predatorspotted, movement))
                else:
                    print("\n\n\n------------------------------------{}{} running to prey at vector {} with movement {}".format(Actor.role, Actor.id, predatorspotted, movement))

            movement = boundarycheck.boundarycheck(predatorspotted, Actor.position, movement, groundsize, randmax)
            print(f"{Actor.role} position before update = {Actor.position}")
            Actor.position = updateposition.updateposition(Actor.position, movement)
            print(f"{Actor.role} position after update = {Actor.position}")
            Actor.lastmovement = movement



            #if Actor.id == 0:
             #   print('\nRound ending position{}\n'.format(Actor.position))

            if Actor.role == 'predator':
                winner = checkforwinner.checkforwinner(Actor.position, actorlist, Actor.walkspeed)
                print(f"Winner = {winner}")

            else:
                winner = [0, 0]

            if winner[0] == 1:
                for i in range(2):
                    movement[i] = actorlist[winner[1]].position[i] - Actor.position[i]
                print(f"Movement = {movement}")
                updateposition.updateposition(Actor.position, movement)
                del(actorlist[winner[1]])
                print(f"Actor {winner[1]} killed!")
            #if Actor.id == 0:
               # print("{} position - \n\n{}\n\n".format(Actor.id, Actor.position))

        outputmanager.populateoutputfiles(actorlist)

        t += 1

    if winner[0] == 0:
        print("\n\nPrey escapes")
    else:
        print("\n\nPredator Wins")
    print(f"\n{t} rounds played")

