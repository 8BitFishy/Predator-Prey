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
#import createnewactor

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
target = 'predator'

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

        #for Actor in actorlist:
         #   print(f"Actor{Actor.id} in role {Actor.role} starts round with traits:\nState - {Actor.state}\nWaiting - {Actor.waiting}\nHungry - {Actor.hungry}\nLongevity - {Actor.longevity}\nDying - {Actor.dying}")

        print("")
        #Generate vectors for each actor
        for Actor in actorlist:

            # if actor is dead, move off the board
            if Actor.alive == 0:
                Actor.position = dead
                print(f"Actor{Actor.id} dead")
                continue

            # If actor is alive, update stats
            else:

                #if actor is not moving this round, make relevant updates
                if Actor.dying == 1 or Actor.sated > 0 or Actor.hunger > Actor.longevity:

                    #if actor is dying, set it to dead, assign no movement and decrement population count
                    if Actor.dying == 1:
                        print(f"Actor{Actor.id} in role {Actor.role}, dying = {Actor.dying}")
                        Actor.alive = 0
                        Actor.dying = 0
                        movement = [0, 0]
                        if Actor.role == 'prey':
                            preyleft -= 1
                        if Actor.role == 'predator':
                            predatorsleft -= 1

                    #if actor is starving to death set state to dying
                    if Actor.hunger > Actor.longevity:
                        print(f"Actor{Actor.id} dies of starvation")
                        Actor.dying = 1

                    #if actor is sated, wait and decrement sated
                    if Actor.sated > 0:
                        print(f"Actor{Actor.id} sated")
                        movement = [0, 0]
                        Actor.sated -= 1

                #otherwise if actor is fine to move, generate movement vectors
                else:
                    #reset winner and targetspotted values
                    #todo redefine 'winner' variable to more descriptive name
                    winner = [0, 0]
                    targetspotted = [0, 0]

                    #if actor is prey, check fro predators
                    if Actor.role == 'prey':
                        #Check for enemigos, return vector for nearest enemy or 0, 0 if none found
                        target = 'predator'
                        direction = 'flee'
                        #todo refactor 'checkforpredators' to more accurate name
                        targetspotted = checkforpredators.checkforpredators(Actor.position, Actor.viewdistance, actorlist, target, Actor.role, Actor.id)


                    #if no enemigo found, search for mate or food
                    if targetspotted == [0, 0]:

                        # assign search target. If actor hunger is less than randy threshold (i.e. has enough food), look for loooooove. Otherwise look for food
                        if Actor.hunger < Actor.randy:
                            target = 'mate'
                        else:
                            target = 'food'

                        #search area for food or mate
                        targetspotted = checkforpredators.checkforpredators(Actor.position, Actor.viewdistance, actorlist, target, Actor.role, Actor.id)

                        #if no target spotted, freeroam
                        if targetspotted == [0, 0]:
                            movement = weightedfreeroam.weightedfreeroam(Actor.lastmovement, Actor.walkspeed)
                            print(f"Actor{Actor.id} freeroams")


                    #if target found, react accordingly, output a movement vector
                    if targetspotted != [0, 0]:

                        #if predator is spotted, flee
                        if target == 'predator':
                            # turn target vector into movement vector
                            print(f"Actor{Actor.id} flees predator")
                            movement = runawaaay.runawaaay(Actor.walkspeed, targetspotted)

                        #if not fleeing from predator
                        else:

                            #check for nearby targets, if found return list [1, X] signifying ['target found', actor number]
                            winner = checkforwinner.checkforwinner(Actor.position, actorlist, Actor.lunge, target,Actor.role, Actor.id)

                            #if target within lunge distance is found, move to target position and perform appropriate action
                            if winner[0] == 1:
                                for i in range(2):
                                    movement[i] = actorlist[winner[1]].position[i] - Actor.position[i]

                                #if target is food, eat food
                                if target == 'food':
                                    #set food state to dying, set actor state to sated (wait one turn to digest), decrease hunger value, remove 'dying' state
                                    print(f"Actor{Actor.id} in role {Actor.role} eats actor{actorlist[winner[1]].id}")
                                    actorlist[winner[1]].dying = 1
                                    Actor.sated = 3
                                    Actor.hunger -= 20
                                    Actor.dying = 0


                                    #else:
                                        #plantpop -= 1

                                #else if target is mate, perform mating
                                else:
                                    #actorlist = generate_actors.createnewactor(actorlist, Actor.id, actorlist[winner[1]].id, t)
                                    #todo implement generate offspring
                                    Actor.sated = actorlist[winner[1]].sated = 10
                                    print(f"Actor{Actor.id} mates with {actorlist[winner[1]].id}")
                                    print(f"Actor{actorlist[len(actorlist)-1].id} born in role {actorlist[len(actorlist)-1].role}")
                                    Actor.hunger += 20
                                    actorlist[winner[1]].hunger += 20

                                    #if actorlist[len(actorlist)-1].role == 'predator':
                                     #   predatorsleft += 1
                                    #elif Actor.role == 'prey':
                                     #   preyleft += 1

                            #if no target found within distance, invert target spotted to ensure movement towards target
                            else:
                                for i in range(2):
                                    targetspotted[i] = targetspotted[i] * -1
                                print(f"Actor{Actor.id} moves towards {target} at vector {targetspotted}")
                                movement = runawaaay.runawaaay(Actor.walkspeed, targetspotted)


            if Actor.role == 'predator':
                #increment hunger value
                Actor.hunger += 1


            #check for wall and update movement accordingly
            if target != 'mate':
                movement = overlapcheck.overlapcheck(actorlist, Actor.position, movement, Actor.role, randmax, Actor.size, Actor.id, Actor.walkspeed)
            movement = boundarycheck.boundarycheck(targetspotted, Actor.position, movement, groundsize, randmax)

            print(f"Actor{Actor.id} moves {movement}\n")

            #update actor position and last movement
            Actor.position = updateposition.updateposition(Actor.position, movement)
            Actor.lastmovement = movement


        print(f"{preyleft} prey left, {predatorsleft} predators left")

        #write vectors to vector files and increment round
        outputmanager.populateoutputfiles(actorlist, dead)
        t += 1




    if preyleft > 0:
        print(f"\n\n{preyleft} prey escaped")

    else:
        print("\n\nPredators Wins")

    print(f"\n{t} rounds played, {t*5} frames in animation")

    f = open("Duration.txt", "w")
    f.write(str(t))
    f.close()





