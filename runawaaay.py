def runawaaay(walkspeed, predatorspotted):
    movement = [0, 0]
    for i in range(2):
        movement[i] = predatorspotted[i] * walkspeed
    #print ("RUNNNNNNNNNNN\n\n")
    print("predator spotted at - {}".format(predatorspotted))
    print("walkspeed - {}".format(walkspeed))
    print("movement - {}".format(movement))
    return movement
