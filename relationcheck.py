def relationcheck(actor1, actor2, actorlist, parameters):

    fertile = False

    #if actor roles are not the same - no match
    if actorlist[actor1].role == actorlist[actor2].role:

        #if actors are sated - no match
        if actorlist[actor2].sated < 5:

            #if actors are not starving to death
            if actorlist[actor2].hunger <= actorlist[actor2].longevity*(50/100):

                # if actor 2 is infertile - no match
                if actorlist[actor1].role == 'predator':

                    if actorlist[actor2].fertility > parameters["predfertility"]:
                        fertile = True
                else:
                    if actorlist[actor2].fertility > parameters["preyfertility"]:
                        fertile = True

    if fertile is True:

        #if actors were born at the beginning of time, match
        if actorlist[actor1].parent1 == -1 and actorlist[actor2].parent1 == -1:
            return True

        else:
            #if Actor 2 is one of Actor 1's parents - no match
            if actorlist[actor1].parent1 == actorlist[actor2].id or actorlist[actor1].parent2 == actorlist[actor2].id:
                return False

            #if Actor 1 is one of Actor 2's parents - no match
            elif actorlist[actor2].parent1 == actorlist[actor1].id or actorlist[actor2].parent2 == actorlist[actor1].id:
                return False

            #if Actor 2 has Actor 1's parent 1 - no match
            elif actorlist[actor1].parent1 == actorlist[actor2].parent1 or actorlist[actor1].parent1 == actorlist[actor2].parent2:
                return False

            #if Actor 2 has Actor 1's parent 2 - no match
            elif actorlist[actor2].parent1 == actorlist[actor1].parent1 or actorlist[actor2].parent1 == actorlist[actor1].parent2:
                return False

            else:
                return True

    #otherwise no match
    else:
        return False