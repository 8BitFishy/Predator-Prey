import relationcheck

def checkforwinner(position, livingactors, lunge, target, role, id, parameters, index):



    #if target is food, search for appropriate food
    if target == 'food':
        if role == 'predator':
            search = 'prey'
        else:
            search = 'plant'

    #if target is not food, search for mate
    else:
        search = role

    if target == 'food':

        for Actor in livingactors:
            if Actor.alive == 0 or Actor.role != search:
                continue


            else:
                if (abs(Actor.position[0] - (position[0])) <= lunge) and (
                        abs(Actor.position[1] - (position[1])) <= lunge) and Actor.dying == 0 and Actor.id != id:
                    winner = [1, Actor.index]
                    return winner

                else:
                    winner = [0, 0]

    else:
        for Actor in livingactors:
            if Actor.alive == 0 or Actor.role != search or Actor.role == 'plant':
                continue

            else:
                if (abs(Actor.position[0] - (position[0])) <= lunge) and (abs(Actor.position[1] - (position[1])) <= lunge) and Actor.dying == 0 and Actor.index != index:
                    if relationcheck.relationcheck(index, Actor.index, livingactors, parameters):

                        winner = [1, Actor.index]
                        return winner
                    else:
                        winner = [0, 0]

                else:
                    winner = [0, 0]


    return winner


