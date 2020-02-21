def runawaaay(position, walkspeed, predatorspotted):
    movement = [0, 0]
    for i in range(2):
        movement[i] = predatorspotted[i] * walkspeed
    #print ("RUNNNNNNNNNNN\n\n")
    return movement
