def relationcheck(actor1, actor2, actorsinview, parameters):
    fertile = False

    #if actor roles are not the same - no match
    if actorsinview[actor1].role == actorsinview[actor2].role:

        #if actors are sated - no match
        if actorsinview[actor2].sated < 5:

            #if actors are not starving to death
            if actorsinview[actor2].hunger <= actorsinview[actor2].longevity*(60 / 100):

                # if actor 2 is infertile - no match
                if actorsinview[actor1].role == 'predator':

                    if actorsinview[actor2].fertility > parameters["predfertility"]:
                        fertile = True
                else:
                    if actorsinview[actor2].fertility > parameters["preyfertility"]:
                        fertile = True

    if fertile is True:

        #if actors were born at the beginning of time, match
        if actorsinview[actor1].parent1 == -1 and actorsinview[actor2].parent1 == -1:
            return True

        else:
            #if Actor 2 is one of Actor 1's parents - no match
            if actorsinview[actor1].parent1 == actorsinview[actor2].id or actorsinview[actor1].parent2 == actorsinview[actor2].id:
                return False

            #if Actor 1 is one of Actor 2's parents - no match
            elif actorsinview[actor2].parent1 == actorsinview[actor1].id or actorsinview[actor2].parent2 == actorsinview[actor1].id:
                return False

            #if Actor 2 has Actor 1's parent 1 - no match
            elif actorsinview[actor1].parent1 == actorsinview[actor2].parent1 or actorsinview[actor1].parent1 == actorsinview[actor2].parent2:
                return False

            #if Actor 2 has Actor 1's parent 2 - no match
            elif actorsinview[actor2].parent1 == actorsinview[actor1].parent1 or actorsinview[actor2].parent1 == actorsinview[actor1].parent2:
                return False

            else:
                return True

    #otherwise no match
    else:
        return False