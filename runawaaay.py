def runawaaay(walkspeed, predatorspotted, viewdistance):
    movement = [0, 0]
    for i in range(2):
        if predatorspotted[i] != 0:

            print(f"Viewdistance = {viewdistance}, Predatorspotted = {predatorspotted}, Walkspeed = {walkspeed}")
            movement[i] = predatorspotted[i] * walkspeed

        else:
            movement[i] = 0



    print("movement - {}".format(movement))
    return movement
