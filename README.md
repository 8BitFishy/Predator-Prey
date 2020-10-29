# Predator-Prey
Blender &amp; Python sim experimentation

A simulation of a natural predator-prey cycle using python, with a script to generate an animation in blender.

General Use:-
----------------------------------------------------------------
Step 1:

Edit parameters to change starting conditions for simulation. Parameters are as follows:

General Parameters:-
predatorsize - Size of predator in animation
preysize - Size of prey in animation
plantsize - Size of plant in animation
groundsize - Size of playing field (eg. 10 results in playing field of 10x10m = 100m^2)

Predator Parameters:-
predatorcount - Starting predator count
predatorlifespan - Average starting age 'dying of old age' for predators 
predatorwalkspeed - Average starting walk speed for predators
predatorviewdistance - Average predator view distance
predlongevity - Average length of time predator can go without eating
predmatingpenalty - Hunger penalty for mating
predeatinggain - Hunger gain for eating
predmatingwait - Duration for predator mating cycle
predbornwait - Duration for newborn predator before movement
predeatingwait - Duration for predator eating
predfertility - Duration between producing offspring for predators

Prey Parameters:-
preycount - Starting prey count
preylifespan - Average starting age 'dying of old age' for prey
preywalkspeed - Average starting walk speed for prey
preyviewdistance - Average prey view distance
preylongevity - Average length of time prey can go without eating
preymatingpenalty - Hunger penalty for mating
preyeatinggain - Hunger gain for eating
preymatingwait - Duration for prey mating cycle
preybornwait - Duration for newborn prey before movement
preyeatingwait - Duration for prey eating
preyfertility - Duration between producing offspring for prey

Plant Parameters:-
plantcount - Starting plant count (plants regrow randomly)

----------------------------------------------------------------
Step 2:

Run 'main' script and wait for sim to finish. This will generate vector files, actor characteristic files and output parameters to inform blender script.

----------------------------------------------------------------
Step 3:
To inspect Actor characteristics & population data run 'Generate_CSV' script to generate a spreadsheet plotting these values over time.

----------------------------------------------------------------
Step 4:
To generate an animation in blender open 'Predator-Prey.blend' file. 
Open 'Window->Toggle System Console' for progress updates. 
Select 'Scripting' tab and run script.
The animation will generate, with progress being reported in the system console window.
Once this is complete, return to the 'Layout' tab and play the animation.



Additional info:

Walk speed is used to determine hunger cost of movement, so high walk speed is not necessarily advantageous
Due to heirarchy of actions (Fleeing from predators > looking for mate > looking for food > freeroaming) long view distance in prey or small groundsize will result in prey seeing predators more easily. This may reduce liklihood of being eaten but at the cost of less time spend looking for food/mate.
Plants are regrown on a dice roll. If the plant count drops below 'plantcount' parameter a dice roll determines if new plants will grow. If successful a diceroll will determine number of plants regrown (based on 'groundsize' parameter).
Creatures will not mate with siblings or parents, so more than two individuals of each species is required





