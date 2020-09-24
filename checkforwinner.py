def checkforwinner(position, actorlist):
    for Actor in actorlist:
        if position == Actor.position and Actor.role == "prey":
            return 1
        else:
            return 0