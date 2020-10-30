import relationcheck

def checkforpredators(position, viewdistance, actorsinview, target, role, id, parameters, index):
    moveaway = [0, 0]
    closest = [viewdistance, viewdistance]
    search = 'predator'
    match = True

    #if target is food, search for appropriate food
    if target == 'food':
        if role == 'predator':
            search = 'prey'
        else:
            search = 'plant'


    #if target is mate, search for mate
    elif target == 'mate':
        search = role


    #else search for predator
    else:
        search == 'predator'

    for Actor in actorsinview:
        if Actor.alive == 0:
            continue

        if role == 'predator' and Actor.role == 'plant':
            continue

        if Actor.role == 'plant' and role != 'prey' and target != 'plant':
            continue


        if (Actor.role == search and Actor.id != id and Actor.dying == 0):

            #if target is a mate, target must not be sated
            if target == 'mate':
                match = relationcheck.relationcheck(index, Actor.index, actorsinview, parameters)
            else:
                match = True

            if match is True:
                # check for predators in x and y direction
                xcheck = Actor.position[0] - position[0]
                ycheck = Actor.position[1] - position[1]

                if abs(xcheck) > (abs(ycheck) * 10):
                    ycheck = 0

                if abs(ycheck) > (abs(xcheck) * 10):
                    xcheck = 0

                if abs(xcheck) < closest[0] and abs(ycheck) < closest[1]:
                    closest[0] = xcheck
                    closest[1] = ycheck
                    # if predator is within view distance
                    if abs(xcheck) < viewdistance and abs(ycheck) < viewdistance:
                        # if predator is in x plane
                        if abs(xcheck) < viewdistance:
                            # if predator is in negative x direction, set movement direction as positive x direction
                            if xcheck < 0:
                                moveaway[0] = 1
                            # if predator is in positive x direction, set movement direction as negative x direction
                            elif xcheck > 0:
                                moveaway[0] = -1
                            # otherwise no x movement
                            else:
                                moveaway[0] = 0

                        if abs(ycheck) < viewdistance:

                            if ycheck < 0:
                                moveaway[1] = 1

                            elif ycheck > 0:
                                moveaway[1] = -1

                            else:
                                moveaway[0] = 0

    return moveaway
