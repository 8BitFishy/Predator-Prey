def relationcheck(actor1, actor2, livingactors, parameters):

    fertile = False

    #if actor roles are not the same - no match
    if livingactors[actor1].role == livingactors[actor2].role:

        #if actors are sated - no match
        if livingactors[actor2].sated < 5:

            #if actors are not starving to death
            if livingactors[actor2].hunger <= livingactors[actor2].longevity*(45 / 100):

                # if actor 2 is infertile - no match
                if livingactors[actor1].role == 'predator':

                    if livingactors[actor2].fertility > parameters["predfertility"]:
                        fertile = True
                else:
                    if livingactors[actor2].fertility > parameters["preyfertility"]:
                        fertile = True

    if fertile is True:

        #if actors were born at the beginning of time, match
        if livingactors[actor1].parent1 == -1 and livingactors[actor2].parent1 == -1:
            return True

        else:
            #if Actor 2 is one of Actor 1's parents - no match
            if livingactors[actor1].parent1 == livingactors[actor2].id or livingactors[actor1].parent2 == livingactors[actor2].id:
                return False

            #if Actor 1 is one of Actor 2's parents - no match
            elif livingactors[actor2].parent1 == livingactors[actor1].id or livingactors[actor2].parent2 == livingactors[actor1].id:
                return False

            #if Actor 2 has Actor 1's parent 1 - no match
            elif livingactors[actor1].parent1 == livingactors[actor2].parent1 or livingactors[actor1].parent1 == livingactors[actor2].parent2:
                return False

            #if Actor 2 has Actor 1's parent 2 - no match
            elif livingactors[actor2].parent1 == livingactors[actor1].parent1 or livingactors[actor2].parent1 == livingactors[actor1].parent2:
                return False

            else:
                return True

    #otherwise no match
    else:
        return False