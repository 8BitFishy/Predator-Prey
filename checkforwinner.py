def checkforwinner(position, actorlist, walkspeed):

    for Actor in actorlist:
        print("Checking for winner\n\n")
        print(f"{abs(Actor.position[0]-(position[0]))} < {walkspeed}")
        print(f"{abs(Actor.position[1]-(position[1]))} < {walkspeed}")

        print(f"Actor role = {Actor.role}")

        if (abs(Actor.position[0]-(position[0])) <= walkspeed/2) and (abs(Actor.position[1]-(position[1])) <= walkspeed/2) and Actor.role == "prey":
            print(f"Predator position = {position}, {Actor.role} position = {Actor.position}\n\n\nWINNNNNER")
            winner = [1, Actor.id]

        else:
            winner = [0, 0]

    return winner


