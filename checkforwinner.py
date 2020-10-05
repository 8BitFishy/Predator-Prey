def checkforwinner(position, actorlist, lunge):

    for Actor in actorlist:

        if (abs(Actor.position[0]-(position[0])) <= lunge) and (abs(Actor.position[1]-(position[1])) <= lunge) and Actor.role == "prey" and Actor.dying == 0:
            winner = [1, Actor.id]
            return winner

        else:
            winner = [0, 0]

    return winner


