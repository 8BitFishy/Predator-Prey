

def Actors_In_View(actorsinview, livingactors, position, viewdistance, role):

    for Actor in livingactors:
        if role == 'predator' and Actor.role == 'plant':
            continue

        else:
            xcheck = Actor.position[0] - position[0]
            ycheck = Actor.position[1] - position[1]

            # if creature is within view distance
            if abs(xcheck) < viewdistance and abs(ycheck) < viewdistance:
                actorsinview.append(Actor)

    return(actorsinview)