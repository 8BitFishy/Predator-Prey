
def checkforpredators(position, viewdistance, predatorlist):
    for predinstance in predatorlist:
        moveaway = [0, 0]
        xcheck = predinstance.position[0] - position[0]
        ycheck = predinstance.position[1] - position[1]
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

        print("preylocation: {}, predatorlocation: {}, viewdistance: {}, moveaway: {}".format(position,
                                                                                                  predinstance.position,
                                                                                                  viewdistance,
                                                                                                  moveaway))
        return moveaway

