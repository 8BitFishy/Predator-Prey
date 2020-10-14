def checkforwinner(position, actorlist, lunge, target, role, id):

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
        for Actor in actorlist:

            if (abs(Actor.position[0]-(position[0])) <= lunge) and (abs(Actor.position[1]-(position[1])) <= lunge) and Actor.role == search and Actor.dying == 0 and Actor.id != id:
                winner = [1, Actor.id]
                return winner

            else:
                winner = [0, 0]

    else:
        for Actor in actorlist:

            if (abs(Actor.position[0] - (position[0])) <= lunge) and (abs(Actor.position[1] - (position[1])) <= lunge) and Actor.role == search and Actor.dying == 0 and Actor.id != id and Actor.hunger < Actor.randy:
                winner = [1, Actor.id]
                return winner

            else:
                winner = [0, 0]


    return winner


