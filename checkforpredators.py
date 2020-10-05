def checkforpredators(position, viewdistance, actorlist, role):
    moveaway = [0, 0]
    closest = [viewdistance, viewdistance]
    for Actor in actorlist:

        if (role != Actor.role):
            # check for predators in x and y direction
            xcheck = Actor.position[0] - position[0]
            ycheck = Actor.position[1] - position[1]

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
