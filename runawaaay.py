def runawaaay(walkspeed, predatorspotted, viewdistance):
    movement = [0, 0]
    for i in range(2):
        if predatorspotted[i] != 0:

            print(f"Viewdistance = {viewdistance}, Predatorspotted = {predatorspotted}, Walkspeed = {walkspeed}")
            #movement[i] = (viewdistance - abs(predatorspotted[i])) * walkspeed
            movement[i] = predatorspotted[i] * walkspeed

            #if predatorspotted[i] < 0:
                #movement[i] = movement[i] * -1

            #else:
                #continue

        else:
            movement[i] = 0
    #print ("RUNNNNNNNNNNN\n\n")



    print("movement - {}".format(movement))
    return movement
