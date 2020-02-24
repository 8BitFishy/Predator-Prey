def checkforpredators(position, viewdistance, actorlist, actornumber, predatorcount):
    moveaway = [0, 0]
    for Actor in actorlist:
        preycount = predcount = 1




        if (actornumber >= predatorcount):
            xcheck = Actor.position[0] - position[0]
            ycheck = Actor.position[1] - position[1]

            if abs(xcheck) < viewdistance and abs(ycheck) < viewdistance:
                if abs(xcheck) < viewdistance:

                    if xcheck < 0:
                        moveaway[0] = 1 * 0.5 * (viewdistance - xcheck)

                    else:
                        moveaway[0] = -1 * 0.5 * (viewdistance - xcheck)

                if abs(ycheck) < viewdistance:
                    if ycheck < 0:
                        moveaway[1] = 1 * 0.5 * (viewdistance - ycheck)

                    else:
                        moveaway[1] = -1 * 0.5 * (viewdistance - ycheck)



    return moveaway
