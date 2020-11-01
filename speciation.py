def speciation (actor1, actor2, actorsinview):

    samespecies = True
    speciesthreshold = 75

    if abs(((actorsinview[actor1].walkspeed - actorsinview[actor2].walkspeed) /
            (actorsinview[actor1].walkspeed)) * 100) > speciesthreshold:

        if abs(((actorsinview[actor1].longevity - actorsinview[actor2].longevity) /
                (actorsinview[actor1].longevity)) * 100) > speciesthreshold:

            if abs(((actorsinview[actor1].lifespan - actorsinview[actor2].lifespan) /
                    (actorsinview[actor1].lifespan)) * 100) > speciesthreshold:

                samespecies = False
                print("\nNew subspecies evolved")


    return samespecies