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
import random
import Generate_CSV
import Actors_In_View

parameters = {}
duration = 0
actorlist = []
livingactors = []
dead = [9000, 9000]
predatorsleft = 0
preyleft = 0
plantsleft = 0
target = 'predator'
randmax = 1000
t = 0
newplant = growplant = 0

#_________________________Start of main simulation___________________________

if __name__ == '__main__':


    clearvectorfiles.clearvectorfiles()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n-----------------------RUN BEGIN------------------------\n")


    #Read parameter file and add to parameters dict
    parameters = read_parameters.read_parameters()
    groundsize = parameters["groundsize"]
    predatorcount = parameters["predatorcount"]
    preycount = parameters["preycount"]
    plantcount = parameters["plantcount"]

    #Generate starting actors and fill out population count
    actorlist = generate_actors.generate_actors(groundsize, parameters)
    actorlist = generate_actors.generateplants(actorlist, groundsize, plantcount, t, dead, parameters)
    livingactors = actorlist.copy()

    for Actor in livingactors:
        if Actor.role == 'predator':
            predatorsleft += 1
        elif Actor.role == 'prey':
            preyleft += 1
        else:
            plantsleft += 1

    print(f"{predatorsleft} predators, {preyleft} prey and {plantsleft} plants")
    #print("\n\nActors generated\n\n")
    log = ''

    #Start simulation
    while t < 20:
    #while predatorsleft != 0:
        livingactors = [Actor for Actor in livingactors if Actor.alive == 1]
        for i in range(len(livingactors)):
            livingactors[i].index = i

        print(f"Round {t} - {len(livingactors)} total creatures, {plantsleft} plants left, {preyleft} prey left, {predatorsleft} predators left - ", end = "")
        log = log + (f"\nRound {t}, Frame {t * 5} - {len(livingactors)} total creatures, {plantsleft} plants left, {preyleft} prey left, {predatorsleft} predators left - ")


        predborn = preyborn = plantsgrown = 0
        predoldage = preyoldage = predstarved = preystarved = preyeaten = plantseaten = 0


        #Generate vectors for each actor
        for Actor in livingactors:

            # if actor is dead, move off the board
            if Actor.alive == 0:
                Actor.position = dead


            # If actor is alive, update stats
            else:
                #if actor is not moving this round, make relevant updates
                if Actor.dying == 1 or Actor.sated > 0 or Actor.hunger > Actor.longevity or Actor.age > Actor.lifespan or Actor.role == 'plant':


                    #if actor is dying, set it to dead, assign no movement and decrement population count
                    if Actor.dying == 1:
                        Actor.alive = 0
                        movement = [0, 0]
                        Actor.dying = 0
                        Actor.death = t
                        if Actor.role == 'prey':
                            preyleft -= 1
                        elif Actor.role == 'predator':
                            predatorsleft -= 1
                        else:
                            plantsleft -= 1

                    #if actor is not dying
                    else:
                        #if actor is plant, no movement
                        if Actor.role == 'plant':
                            movement = [0, 0]

                        #if actor is not plant
                        else:

                            #if actor is sated, wait and decrement sated
                            if Actor.sated > 0:
                                movement = [0, 0]
                                Actor.sated -= 1

                            #if actor is not sated
                            else:

                                #If actor exceeds lifespan, DIE
                                if Actor.age > Actor.lifespan and Actor.role != 'plant':
                                    if Actor.role == 'prey':
                                        preyoldage += 1
                                        log = log + f"Prey dies of old age({Actor.id}), "
                                    else:
                                        predoldage += 1
                                        log = log + f"Predator dies of old age({Actor.id}), "
                                    Actor.causeofdeath = "old age"
                                    Actor.dying = 1

                                else:
                                    #if actor is starving to death set state to dying
                                    if Actor.hunger > Actor.longevity and Actor.role != 'plant':
                                        Actor.causeofdeath = "starvation"
                                        Actor.dying = 1
                                        if Actor.role == 'prey':
                                            preystarved += 1
                                            log = log + f"Prey dies of starvation({Actor.id}), "
                                        else:
                                            predstarved += 1
                                            log = log + f"Predator dies of starvation({Actor.id}), "


                #otherwise if actor is fine to move, generate movement vectors
                else:
                    actorsinview = []
                    actorsinview.append(Actor)
                    actorsinview = Actors_In_View.Actors_In_View(actorsinview, livingactors, Actor.position, Actor.viewdistance, Actor.role)
                    for i in range(len(actorsinview)):
                        actorsinview[i].index = i

                    #reset winner and targetspotted values
                    #todo redefine 'winner' variable to more descriptive name
                    winner = [0, 0]
                    targetspotted = [0, 0]
                    movement = [0, 0]

                    if Actor.role == 'predator':
                        fertilitythreshold = parameters["predfertility"]

                    #if actor is prey, check for predators
                    if Actor.role == 'prey':
                        #Check for enemigos, return vector for nearest enemy or 0, 0 if none found
                        target = 'predator'
                        direction = 'flee'
                        fertilitythreshold = parameters["preyfertility"]
                        #todo refactor 'checkforpredators' to more accurate name
                        targetspotted = checkforpredators.checkforpredators(Actor.position, Actor.viewdistance, actorsinview, target, Actor.role, Actor.id, parameters, Actor.index)

                    #if no enemigo found, search for mate or food
                    if targetspotted == [0, 0]:

                        # assign search target. If actor hunger is less than randy threshold (i.e. has enough food), look for loooooove
                        if Actor.fertility > fertilitythreshold and Actor.hunger <= Actor.longevity*(45/100):
                            target = 'mate'

                            targetspotted = checkforpredators.checkforpredators(Actor.position, Actor.viewdistance, actorsinview, target, Actor.role, Actor.id, parameters, Actor.index)

                        #if no target spotted and actor is hungry, search for food
                        if targetspotted == [0, 0]:
                            #if Actor is not hungry, freeroam
                            if Actor.hunger <= Actor.longevity*0.2:
                                targetspotted = [0, 0]
                            #otherwise look for food
                            else:
                                target = 'food'

                                targetspotted = checkforpredators.checkforpredators(Actor.position, Actor.viewdistance,
                                                                                actorsinview, target, Actor.role, Actor.id,parameters, Actor.index)

                        # if still no target spotted, freeroam
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

                            winner = checkforwinner.checkforwinner(Actor.position, actorsinview, Actor.lunge, target, Actor.role, Actor.index, parameters, Actor.index)

                            #if target within lunge distance is found, move to target position and perform appropriate action
                            if winner[0] == 1:
                                for i in range(2):
                                    movement[i] = actorsinview[winner[1]].position[i] - Actor.position[i]

                                #if target is food, eat food
                                if target == 'food':

                                    #set food state to dying, set actor state to sated (wait for digestion), decrease hunger value, remove 'dying' state and add characteristics info
                                    actorsinview[winner[1]].dying = 1
                                    actorsinview[winner[1]].causeofdeath = f"eaten by actor {Actor.id}"
                                    if Actor.role == 'predator':
                                        Actor.sated = parameters["predeatingwait"]
                                        Actor.hunger -= parameters["predeatinggain"]
                                    else:
                                        Actor.sated = parameters["preyeatingwait"]
                                        Actor.hunger -= parameters["preyeatinggain"]
                                    Actor.dying = 0
                                    Actor.enemieseaten += 1

                                    if actorsinview[winner[1]].role == 'prey':
                                        preyeaten += 1
                                        log = log + f"Prey eaten({actorsinview[winner[1]].id}), "

                                    else:
                                        plantseaten += 1
                                        #print("Plant eaten", end = ", ")
                                        log = log + "Plant eaten, "

                                #else if target is mate, generate new actor from parents. Backfill baby vectors. Perform appropriate updates
                                else:

                                    livingactors = generate_actors.createnewactor(livingactors, actorsinview, Actor.index, actorsinview[winner[1]].index, parameters, t, dead)
                                    Actor.timesmated += 1
                                    actorsinview[winner[1]].timesmated += 1
                                    Actor.fertility = actorsinview[winner[1]].fertility = 0
                                    if Actor.role == 'predator':
                                        Actor.sated = actorsinview[winner[1]].sated = parameters["predmatingwait"]
                                        actorsinview[-1].sated = parameters["predbornwait"]
                                        Actor.hunger += parameters["predmatingpenalty"]
                                        actorsinview[winner[1]].hunger += parameters["predmatingpenalty"]
                                        predatorsleft += 1
                                        predborn += 1
                                        log = log + f"Predator born({actorsinview[-1].id}), "

                                    else:
                                        Actor.sated = actorsinview[winner[1]].sated = parameters["preymatingwait"]
                                        actorsinview[-1].sated = parameters["preybornwait"]
                                        Actor.hunger += parameters["preymatingpenalty"]
                                        actorsinview[winner[1]].hunger += parameters["preymatingpenalty"]
                                        preyleft += 1
                                        preyborn += 1
                                        log = log + f"Prey born({actorsinview[-1].id}), "

                            #if no target found within distance, invert target spotted to ensure movement towards target
                            else:
                                for i in range(2):
                                    targetspotted[i] = targetspotted[i] * -1
                                movement = runawaaay.runawaaay(Actor.walkspeed, targetspotted)


                #Age actors
                Actor.age += 1
                Actor.fertility += 1

                #increment hunger value
                if movement[0] == 0 and movement[1] != 0:
                    Actor.hunger += abs(movement[1])*0.1

                elif movement[1] == 0 and movement[0] != 0:
                    Actor.hunger += abs(movement[0])*0.1

                else:
                    Actor.hunger += (math.sqrt((abs(movement[0])**2) + (abs(movement[1])**2))*0.1)


                #check for wall and update movement accordingly
                if Actor.role != 'plant':
                    movement = overlapcheck.overlapcheck(actorsinview, Actor.position, movement, Actor.role, randmax, Actor.size, Actor.id, Actor.walkspeed)
                    movement = boundarycheck.boundarycheck(targetspotted, Actor.position, movement, groundsize, randmax)
                    #update actor position and last movement
                    Actor.lastmovement = movement
                    Actor.position = updateposition.updateposition(Actor.position, movement)


            Actor.vectors.append([Actor.position[0], Actor.position[1]])





        if plantsleft < plantcount:
            growplants = random.randint(0, 100)
            if growplants > 85:
                newplants = random.randint(1, groundsize / 50)
                plantsgrown = newplants
                livingactors = generate_actors.generateplants(livingactors, groundsize, newplants, t, dead, parameters)
                plantsleft += newplants

        #write vectors to vector files and increment round
        print(f"{preyborn} prey born, {preyeaten} prey eaten, {preystarved} prey starved, {preyoldage} prey died of old age, {predborn} preds born, {predstarved} preds starved, {predoldage} preds died of old age, {plantsgrown} plants grown, {plantseaten} plants eaten")

        for Actor in livingactors:
            if Actor not in actorlist:
                actorlist.append(Actor)


        t += 1


    #Generate exit messages
    predatortotal = preytotal = 0
    predsleft = preysleft = 0
    plantsleft = plantstotal = 0

    for Actor in actorlist:
        if Actor.role == 'predator':
            predatortotal += 1
            if Actor.alive == 1:
                predsleft += 1
        elif Actor.role == 'prey':
            preytotal += 1
            if Actor.alive == 1:
                preysleft += 1
        else:
            plantstotal += 1
            if Actor.alive == 1:
                plantsleft += 1



    #generate exit files
    print(f"\nGenerating log")
    outputmanager.print_log(log)
    outputmanager.populateoutputfiles(actorlist, dead, t)
    outputmanager.output_characteristics(actorlist)
    print(f"\nGenerating animation parameters")
    outputmanager.print_outputparams(actorlist, t)
    print(f"Generating stats files")
    print(f"\n{predsleft} of {predatortotal} predators left alive")
    print(f"{preysleft} of {preytotal} prey left alive")
    print(f"{plantsleft} of {plantstotal} plants left alive")
    print(f"{t} rounds played, {t*5} frames in animation\n")
    Generate_CSV.Generate_CSV()





