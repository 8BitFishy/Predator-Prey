import random

def weightedfreeroam(last_movement, walkspeed):
    offset = 10
    weight = 9
    weighted_random = [0, 0]
    movement = [0, 0]
    xweight = int(last_movement[0]) * weight
    yweight = int(last_movement[1]) * weight

    weighted_random[0] = ['1'] * (offset+xweight) + ['-1'] * (offset-xweight) + ['0'] * offset

    weighted_random[1] = ['1'] * (offset+yweight) + ['-1'] * (offset-yweight) + ['0'] * offset

    ##print("last movement - {}".format(last_movement))
    ##print("Stats: X+: {}, X-: {}, X0: {}".format(offset+xweight, offset-xweight, offset))
    ##print("Stats: Y+: {}, Y-: {}, Y0: {}".format(offset+yweight, offset-yweight, offset))


    for i in range(0, 2):
        movement[i] = int(random.choice(weighted_random[i]))
        movement[i] = movement[i] * walkspeed

    #print(movement)
    return(movement)
