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
import read_parameters
import math

parameters = {}
duration = 0
actorlist = []
dead = [9000, 9000]
predatorsleft = 0
preyleft = 0
target = 'predator'
randmax = 1000



#_________________________Start of main simulation___________________________

if __name__ == '__main__':


    clearvectorfiles.clearvectorfiles()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n-----------------------RUN BEGIN------------------------\n")

    t = 0

    #todo complete implementing parameters dictionary for use in methods
    parameters = read_parameters.read_parameters()
    groundsize = parameters["groundsize"]
    predatorcount = parameters["predatorcount"]
    preycount = parameters["preycount"]


    actorlist = generate_actors.generate_actors(groundsize, parameters)
    for Actor in actorlist:
        if Actor.role == 'predator':
            predatorsleft += 1
        elif Actor.role == 'prey':
            preyleft += 1
    print(f"{predatorsleft} predators and {preyleft} prey")
    #print("\n\nActors generated\n\n")


    while preyleft != 0 and predatorsleft != 0:
        print(f"Round {t}, Frame {t*5} - {preyleft} prey left, {predatorsleft} predators left")


        #Generate vectors for each actor
        for Actor in actorlist:

            # if actor is dead, move off the board
            if Actor.alive == 0:
                Actor.position = dead
                continue

            # If actor is alive, update stats
            else:

                #if actor is not moving this round, make relevant updates
                if Actor.dying == 1 or Actor.sated > 0 or Actor.hunger > Actor.longevity or Actor.age > Actor.lifespan:

                    #if actor is dying, set it to dead, assign no movement and decrement population count
                    if Actor.dying == 1:
                        Actor.alive = 0
                        movement = [0, 0]
                        Actor.death = t
                        if Actor.role == 'prey':
                            preyleft -= 1
                        if Actor.role == 'predator':
                            predatorsleft -= 1

                    if Actor.age > Actor.lifespan:
                        print(f"Actor{Actor.id} dies of old age after {Actor.age + 1} turns")
                        Actor.causeofdeath = "old age"
                        Actor.dying = 1

                    #if actor is starving to death set state to dying
                    if Actor.hunger > Actor.longevity:
                        print(f"Actor{Actor.id} dies of starvation")
                        Actor.causeofdeath = "starvation"
                        Actor.dying = 1

                    #if actor is sated, wait and decrement sated
                    if Actor.sated > 0:
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


                    #if target found, react accordingly, output a movement vector
                    if targetspotted != [0, 0]:

                        #if predator is spotted, flee
                        if target == 'predator':
                            # turn target vector into movement vector
                            movement = runawaaay.runawaaay(Actor.walkspeed, targetspotted)

                        #if not fleeing from predator
                        else:

                            #check for nearby targets, if found return list [1, X] signifying ['target found', actor number]
                            winner = checkforwinner.checkforwinner(Actor.position, actorlist, Actor.lunge, target, Actor.role, Actor.id)

                            #if target within lunge distance is found, move to target position and perform appropriate action
                            if winner[0] == 1:
                                for i in range(2):
                                    movement[i] = actorlist[winner[1]].position[i] - Actor.position[i]

                                #if target is food, eat food
                                if target == 'food':
                                    #set food state to dying, set actor state to sated (wait one turn to digest), decrease hunger value, remove 'dying' state
                                    print(f"Actor{Actor.id} in role {Actor.role} eats actor{actorlist[winner[1]].id}")
                                    actorlist[winner[1]].dying = 1
                                    actorlist[winner[1]].causeofdeath = f"eaten by actor {Actor.id}"
                                    Actor.sated = parameters["predeatingwait"]
                                    Actor.hunger -= parameters["predeatinggain"]
                                    Actor.dying = 0
                                    Actor.enemieseaten += 1


                                    #else:
                                        #plantpop -= 1

                                #else if target is mate, perform mating
                                else:
                                    print(f"Actor{Actor.id} mates with {actorlist[winner[1]].id}")
                                    actorlist = generate_actors.createnewactor(actorlist, Actor.id, actorlist[winner[1]].id, parameters, t)
                                    print(f"Actor{actorlist[len(actorlist)-1].id} born in role {actorlist[len(actorlist)-1].role}")
                                    outputmanager.backfill_vectors(actorlist, t, dead)
                                    Actor.timesmated += 1
                                    actorlist[winner[1]].timesmated += 1
                                    if Actor.role == 'predator':
                                        Actor.sated = actorlist[winner[1]].sated = parameters["predmatingwait"]
                                        actorlist[-1].sated = parameters["predbornwait"]
                                        Actor.hunger += parameters["predmatingpenalty"]
                                        actorlist[winner[1]].hunger += parameters["predmatingpenalty"]
                                        predatorsleft += 1
                                    else:
                                        preyleft += 1


                            #if no target found within distance, invert target spotted to ensure movement towards target
                            else:
                                for i in range(2):
                                    targetspotted[i] = targetspotted[i] * -1
                                movement = runawaaay.runawaaay(Actor.walkspeed, targetspotted)


            if Actor.role == 'predator':
                #increment hunger value
                if movement[0] == 0 and movement[1] != 0:
                    Actor.hunger += int(abs(movement[1])*0.1)

                elif movement[1] == 0 and movement[0] != 0:
                    Actor.hunger += int(abs(movement[0])*0.1)

                else:
                    Actor.hunger += (int(math.sqrt((abs(movement[0])**2) + (abs(movement[1])**2)))*0.1)
                Actor.age += 1


            #check for wall and update movement accordingly
            movement = overlapcheck.overlapcheck(actorlist, Actor.position, movement, Actor.role, randmax, Actor.size, Actor.id, Actor.walkspeed)
            movement = boundarycheck.boundarycheck(targetspotted, Actor.position, movement, groundsize, randmax)

            #update actor position and last movement
            Actor.position = updateposition.updateposition(Actor.position, movement)
            Actor.lastmovement = movement



        #write vectors to vector files and increment round
        outputmanager.populateoutputfiles(actorlist, dead)
        t += 1


    predatortotal = preytotal = 0
    predsleft = preysleft = 0

    for Actor in actorlist:
        if Actor.role == 'predator':
            predatortotal += 1
            if Actor.alive == 1:
                predsleft += 1
        else:
            preytotal += 1
            if Actor.alive == 1:
                preysleft += 1

    print(f"{predsleft} of {predatortotal} predators left alive")
    print(f"{preysleft} of {preytotal} prey left alive")


    if preyleft > 0:
        print(f"\n\n{preyleft} prey escaped")

    else:
        print("\n\nPredators Wins")

    print(f"\n{t} rounds played, {t*5} frames in animation")


    outputmanager.print_outputparams(actorlist, t)
    outputmanager.output_characteristics(actorlist)





