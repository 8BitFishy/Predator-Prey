import random

def boundarycheck(predatorspotted, position, movement, groundsize, randmax):
    stuck = 0
    overflow = 0
    # print("\n-------Start boundary check-------")
    # print("Starting Position: {}".format(position))
    # print("Attempting movement: {}\n".format(movement))
    pathfound = 0

    while True:

        if abs(position[0] + movement[0]) > groundsize / 2:

            if position[0] <= 0:
                overflow = position[0] + movement[0] + overflow + groundsize / 2
            else:
                overflow = position[0] + movement[0] + overflow - groundsize / 2

            # print("Predator spotted at: {}".format(predatorspotted))

            pathfound = 1

            while pathfound != 0:
                # print("overflow x = {}".format(overflow))
                randoverflow = random.randint(1, randmax)

                if predatorspotted[0] == 0:
                    movement[0] = - movement[0]
                    # print("state 3: {}".format(movement))
                    pathfound = 0

                elif randoverflow <= randmax / 3 and predatorspotted[1] <= 0:
                    movement[0] = movement[0] - overflow
                    movement[1] = movement[1] - overflow
                    # print("state 1: {}".format(movement))
                    pathfound = 0

                elif randoverflow > randmax / 3 and randoverflow < 2 * randmax / 3 and predatorspotted[1] >= 0:
                    movement[0] = movement[0] - overflow
                    movement[1] = movement[1] + overflow
                    # print("state 2: {}".format(movement))
                    pathfound = 0

                elif predatorspotted[0] != 0 and predatorspotted[1] != 0:
                    # print("CORNERED1")
                    movement[0] = movement[0] - overflow
                    pathfound = 0

            overflow = 0
            # print("movementupdate = {}\n".format(movement))

        if abs(position[1] + movement[1]) > groundsize / 2:

            if position[1] <= 0:
                overflow = position[1] + movement[1] + overflow + groundsize / 2
            else:
                overflow = position[1] + movement[1] + overflow - groundsize / 2

            # print("Predator spotted at: {}".format(predatorspotted))
            pathfound = 1

            while pathfound != 0:
                # print("overflow y = {}".format(overflow))
                randoverflow = random.randint(1, randmax)

                if predatorspotted[1] == 0:
                    movement[1] = - movement[1]
                    # print("state 6: {}".format(movement))
                    pathfound = 0

                elif randoverflow <= randmax / 3 and predatorspotted[0] <= 0:
                    movement[1] = movement[1] - overflow
                    movement[0] = movement[0] - overflow
                    # print("state 4: {}".format(movement))
                    pathfound = 0

                elif randoverflow > randmax / 3 and randoverflow < 2 * randmax / 3 and predatorspotted[0] >= 0:
                    movement[1] = movement[1] - overflow
                    movement[0] = movement[0] + overflow
                    # print("state 5: {}".format(movement))
                    pathfound = 0



                elif predatorspotted[0] != 0 and predatorspotted[1] != 0:
                    # print("CORNERED")
                    movement[1] = movement[1] - overflow
                    pathfound = 0

            overflow = 0
            # print("movementupdate = {}\n".format(movement))



        else:
            # print("no overflow")
            overflow = 0

        # print("Position: {}, Movement: {}".format(position, movement))

        if overflow == 0 and abs(movement[0] + position[0]) <= groundsize / 2 and abs(
                movement[1] + position[1]) <= groundsize / 2:
            break

        elif stuck > 10:
            movement = [0, 0]
            break

        else:
            stuck += 1
            # print("Stuck! = : {}".format(stuck))

    return movement
