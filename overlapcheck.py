import random

def overlapcheck(livingactors, position, movement, role, randmax, size, id, walkspeed):
    doublecheck = 0
    stuck = 0
    while doublecheck < 2:
        for Actor in livingactors:
            if Actor.role == 'plant' or Actor.alive == 0:
                continue

            else:
                if Actor.role == role and Actor.id != id and Actor.alive != 0:
                    stuck = 0

                    if abs(Actor.position[0] - (position[0] + movement[0])) <= size and abs(Actor.position[1] - (position[1] + movement[1])) <= size and stuck <= 10:

                        if movement[0] == 0 and movement[1] == 0:
                            randoverflow = random.randint(1, randmax)

                            if randoverflow < randmax / 4:
                                movement[0] += walkspeed

                            elif randoverflow >= randmax / 4 and randoverflow < randmax / 2:
                                movement[0] -= walkspeed

                            elif randoverflow >= randmax / 2 and randoverflow <= 3*randmax / 4:
                                movement[1] += walkspeed

                            else:
                                movement[1] -= walkspeed



                        while Actor.position[0] - (position[0] + movement[0]) <= (size) and Actor.position[1] - (position[1] + movement[1]) <= size and stuck < 10:

                            randoverflow = random.randint(1, randmax)


                            if movement[0] > 0:

                                if randoverflow > randmax / 2:
                                    movement[0] = movement[0] - int(size / 2) - 1

                                else:
                                    movement[0] = movement[0] + 0

                            elif movement[0] < 0:

                                if randoverflow > randmax / 2:

                                    movement[0] = movement[0] + int(size / 2) + 1

                                else:

                                    movement[0] = movement[0] + 0


                            randoverflow = random.randint(1, randmax)

                            if movement[1] > 0:

                                if randoverflow >= randmax / 2:

                                    movement[1] = movement[1] - int(size / 2) - 1

                                else:

                                    movement[1] = movement[1] + 0

                            elif movement[1] < 0:

                                if randoverflow >= randmax / 2:

                                    movement[1] = movement[1] + int(size / 2) + 1

                                else:

                                    movement[1] = movement[1] - 1

                            stuck += 1

                else:
                    continue

        if stuck >= 10:
            movement = [0, 0]

        doublecheck += 1

    return movement
