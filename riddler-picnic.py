from random import randint

def picnic(trials):

    fails = 0
    successes = 0
    tries = 0

    for rep in range(trials):

        # Draw arrival times independently as integer minutes after noon
        rand1 = randint(0, 60)
        rand2 = randint(0, 60)

        # Assign draws in arrival order
        first = min(rand1, rand2)
        last = max(rand1, rand2)

        if last <= first + 15:
            # They meet for a picnic
            successes += 1
        else:
            fails += 1

    print("\nFails: {}".format(fails))
    print("Successes: {}".format(successes))
    print("Tries: {}".format(trials))
    print("Success percentage: {}%\n".format((successes/trials)*100))

picnic(1000000)
