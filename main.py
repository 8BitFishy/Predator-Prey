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
livingactors = []
dead = [99999, 99999, 99999]
target = 'predator'
randmax = 1000
t = 0
newplant = growplant = 0
preyav = []
predav = []
plantav = []
deadactors = []

predatortotal = preytotal = 0
predsleft = preyleft = 0
plantsleft = plantstotal = 0

#_________________________Start of main simulation___________________________

if __name__ == '__main__':

    clearvectorfiles.clearvectorfiles()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n-----------------------RUN BEGIN------------------------\n")

    #todo build system to dump dead actors out of memory, fill in vectors with second script pre-blender load up
    #todo every thousand cycles print dead actor characteristics and vector files
    #todo early system end system
    #todo remove vector backfilling and move system to end


    #Read parameter file and add to parameters dict
    parameters = read_parameters.read_parameters()
    groundsize = parameters["groundsize"]
    predatorcount = parameters["predatorcount"]
    preycount = parameters["preycount"]
    plantcount = parameters["plantcount"]

    #Generate starting actors and fill out population count
    livingactors = generate_actors.generate_actors(groundsize, parameters)
    livingactors = generate_actors.generateplants(livingactors, groundsize, plantcount, t, parameters)

    for Actor in livingactors:
        if Actor.role == 'predator':
            predsleft += 1
            predatortotal += 1
        elif Actor.role == 'prey':
            preyleft += 1
            preytotal += 1
        else:
            plantsleft += 1
            plantstotal += 1


    print(f"{predsleft} predators, {preyleft} prey and {plantsleft} plants")
    #print("\n\nActors generated\n\n")
    log = ''

    #Start simulation
    while predsleft != 0 and preyleft != 0:

        #Update living actors list and assign new index
        livingactors = [Actor for Actor in livingactors if Actor.alive == 1]
        for i in range(len(livingactors)):
            livingactors[i].index = i

        #print output files for dead actors
        if t%parameters["offload"] == 0:
            outputmanager.populateoutputfiles(deadactors)
            outputmanager.output_characteristics(deadactors)
            outputmanager.print_outputparams(predatortotal, preytotal, plantstotal, t)
            deadactors = []


        #log updates
        print(f"Round {t} - {len(livingactors)} total, {predsleft} predators, {preyleft} prey, {plantsleft} plants - ", end = "")
        log = log + (f"\nRound {t}, Frame {t * 5} - {len(livingactors)} total, {predsleft} predators left, {preyleft} prey left, {plantsleft} plants left - ")

        #zero pop change data
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


                    #if actor is dying, set it to dead, assign no movement, decrement population count and append actor to deadactors list
                    if Actor.dying == 1:
                        Actor.alive = 0
                        movement = [0, 0]
                        Actor.dying = 0
                        Actor.death = t+2
                        if Actor.role == 'prey':
                            preyleft -= 1
                        elif Actor.role == 'predator':
                            predsleft -= 1
                        else:
                            plantsleft -= 1
                        deadactors.append(Actor)

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
                        if Actor.fertility > fertilitythreshold and Actor.hunger <= Actor.longevity*(50/100):
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
                                    littersize = 0
                                    litterchance = random.randint(0, 100)
                                    if litterchance < 85:
                                        littersize = 1
                                    elif litterchance >= 85 and litterchance < 93:
                                        littersize = 2
                                    elif litterchance >= 93 and litterchance < 98:
                                        littersize = 3
                                    else:
                                        littersize = 4

                                    for i in range(littersize):
                                        livingactors = generate_actors.createnewactor(livingactors, actorsinview, Actor.index, actorsinview[winner[1]].index, t)
                                        if Actor.role == 'predator':
                                            livingactors[-1].sated = parameters["predbornwait"]
                                            log = log + f"Predator born({livingactors[-1].id}), "
                                            predsleft += 1
                                            predborn += 1
                                            predatortotal += 1
                                        else:
                                            livingactors[-1].sated = parameters["preybornwait"]
                                            log = log + f"Prey born({livingactors[-1].id}), "
                                            preyleft += 1
                                            preyborn += 1
                                            preytotal += 1

                                    Actor.timesmated += 1
                                    actorsinview[winner[1]].timesmated += 1
                                    Actor.fertility = actorsinview[winner[1]].fertility = 0

                                    if Actor.role == 'predator':
                                        Actor.sated = actorsinview[winner[1]].sated = parameters["predmatingwait"]
                                        Actor.hunger += parameters["predmatingpenalty"]
                                        actorsinview[winner[1]].hunger += parameters["predmatingpenalty"]


                                    else:
                                        Actor.sated = actorsinview[winner[1]].sated = parameters["preymatingwait"]
                                        Actor.hunger += parameters["preymatingpenalty"]
                                        actorsinview[winner[1]].hunger += parameters["preymatingpenalty"]



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

            #append vectors to actor vector list
            Actor.vectors.append([Actor.position[0], Actor.position[1]])


        #Grow new plants
        if plantsleft < plantcount:
            growplants = random.randint(0, 100)
            if growplants > 80:
                newplants = random.randint(0, 10)
                plantsgrown = newplants
                livingactors = generate_actors.generateplants(livingactors, groundsize, newplants, t, parameters)
                plantsleft += newplants
                plantstotal += newplants



        #write vectors to vector files and increment round
        print(f"{predborn} preds born, {predstarved} starved, {predoldage} old age", end = '')
        print(f" - {preyborn} prey born, {preyeaten} eaten, {preystarved} starved, {preyoldage} old age", end = '')
        print(f" - plants ", end = '')
        if (plantsgrown-plantseaten) >= 0 and (plantsgrown-plantseaten) <= 9:
            print(" ", end = '')
        print(f"{plantsgrown-plantseaten}", end = '')

        #generate population growth/reduction rate
        preyav.append(preyborn - (preystarved + preyoldage + preyeaten))
        predav.append(predborn - (predstarved + predoldage))
        plantav.append(plantsgrown-plantseaten)
        avrate = 50

        if len(preyav) > avrate:
            del preyav[0]
        if len(predav) > avrate:
            del predav[0]
        if len(plantav) > avrate:
            del plantav[0]

        print(f" - pred ", end = '')
        if round(sum(predav) / len(predav), 2) >= 0:
            print(" ", end = '')
        print(f"{round(sum(predav) / len(predav), 2)}", end = '')

        print(f"  prey ", end = '')
        if round(sum(preyav) / len(preyav), 2) >= 0:
            print(" ", end = '')
        print(f"{round(sum(preyav) / len(preyav), 2)} ", end = '')

        print(f" plants ", end = '')
        if round(sum(plantav) / len(plantav), 2) >= 0:
            print(" ", end = '')
        print(f"{round(sum(plantav) / len(plantav), 2)} ")


        #increment time
        t += 1


    #add unexported dead actors to livingactors
    for Actor in deadactors:
        if Actor not in livingactors:
            livingactors.append(Actor)

    #generate exit files
    print(f"\nGenerating Parameter File")
    outputmanager.print_inputs(parameters)
    print(f"Generating log")
    outputmanager.print_log(log)
    print(f"Generating vectors")
    outputmanager.populateoutputfiles(livingactors)
    print(f"Generating actor characteristics files")
    outputmanager.output_characteristics(livingactors)
    print(f"Generating animation parameters")
    outputmanager.print_outputparams(predatortotal, preytotal, plantstotal, t)
    print(f"Generating stats files")
    print(f"\n{predsleft} of {predatortotal} predators left alive")
    print(f"{preyleft} of {preytotal} prey left alive")
    print(f"{plantsleft} of {plantstotal} plants left alive")
    print(f"{t} rounds played, {t*5} frames in animation\n")
    Generate_CSV.Generate_CSV()





