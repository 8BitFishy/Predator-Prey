def relationcheck(actor1, actor2, actorlist):

    if actorlist[actor1].parent1 == -1 and actorlist[actor2].parent1 == -1:
        return True

    else:
        #if Actor 2 is one of Actor 1's parents
        if actorlist[actor1].parent1 == actorlist[actor2].id or actorlist[actor1].parent2 == actorlist[actor2].id:
            return False

        #if Actor 1 is one of Actor 2's parents
        elif actorlist[actor2].parent1 == actorlist[actor1].id or actorlist[actor2].parent2 == actorlist[actor1].id:
            return False

        #if Actor 2 has Actor 1's parent 1
        elif actorlist[actor1].parent1 == actorlist[actor2].parent1 or actorlist[actor1].parent1 == actorlist[actor2].parent2:
            return False

        #if Actor 2 has Actor 1's parent 2
        elif actorlist[actor2].parent1 == actorlist[actor1].parent1 or actorlist[actor2].parent1 == actorlist[actor1].parent2:
            return False

        else:
            return True
