def runawaaay(walkspeed, targetspotted):
    movement = [0, 0]
    for i in range(2):

        if targetspotted[i] != 0:
            movement[i] = targetspotted[i] * walkspeed

        else:
            movement[i] = 0

    return movement
