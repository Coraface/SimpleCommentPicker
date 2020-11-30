##### Description #####
# Assuming you have 3 lifetimes and want to win a giveaway
# Also, assuming you can enter y of these giveaways with 20000 participants each
# Let's see how many of these you can win

import numpy as np
import string
import time
from multiprocessing import Pool

USERS = np.array(list(string.ascii_lowercase + ' ')) 
NUM_OF_USERS = 20000
NUM_OF_LIVES = 200
GIVEAWAYS = 200

users = []

#### Randomly generating users 
def generate_users(length):
    users.clear()
    for id in range(length):
        users.append(''.join(np.random.choice(USERS) for i in range(4)))
    users[np.random.randint(0, length-1)] = "XRHS"

def win_function(lengths):
    flag = 0
    winner = ""
    low = l = int(lengths[0])
    high = h = int(lengths[1])
    giveaways_count = max_wins_of_one_life = previous_max_wins = 0
    while low < high:
        win_count = giveaway = 0
        while giveaway < GIVEAWAYS:
            winner = np.random.choice(users)
            if winner == "XRHS":
                giveaways_count = giveaways_count + 1
                win_count = win_count + 1
                flag = 1
            giveaway = giveaway + 1
        if win_count > previous_max_wins:
            previous_max_wins = win_count
            max_wins_of_one_life = previous_max_wins
        low = low + 1
    d = dict();
    d['give'] = giveaways_count
    d['max_wins'] = max_wins_of_one_life
    return d


######### Main #########

# Everything at far left runs in parallel
# so generate different users for every process
generate_users(NUM_OF_USERS)

if __name__ == '__main__':
    
    # Setup segmentation
    procs = 8
    sizeSegment = NUM_OF_LIVES / procs
    print("Running",procs,"processes in parallel")
    print("Calculating...")
    print("For NUM_OF_LIVES > 1000 expect more than 13 seconds runtime")
    print("For NUM_OF_LIVES > 10000 expect more than 130 seconds runtime")

    jobs = []
    for i in range(0, procs):
        jobs.append((i*sizeSegment, (i+1)*sizeSegment, i))

    # Start
    start = time.perf_counter()

    # Parallelization
    pool = Pool(procs).map(win_function, jobs)

    # Finish
    finish = time.perf_counter()
    
    #print(pool)

    # Extracting sum of won giveaways and max wins of a single lifetime
    max_wins = max(item['max_wins'] for item in pool)
    give = sum(item['give'] for item in pool)

    # Mathematical formula of probability (credits to Vsauce2)
    formula1 = 1 - (1 - 1 / NUM_OF_USERS) ** GIVEAWAYS
    formula2 = (1 - 1 / NUM_OF_USERS) ** (GIVEAWAYS * NUM_OF_LIVES)
    print("\nThe probability of winning at least 1 giveaway out of", GIVEAWAYS, "with", NUM_OF_USERS, "participants is:",round(formula1 * 100,3),"%")
    if give != 0:
        print("\nFor", NUM_OF_LIVES, "lifetimes, each of", GIVEAWAYS, "giveaways\nyou won:", give)
        print("\nThe probability of not winning any giveaway in any lifetime is:",round(formula2 * 100,3),"%")
        print("\nMost wins for a single lifetime:", max_wins)
    else:
        print("\nYou will never win ma friend .|.")
    print(f'\nFinished in {round(finish-start,2)} seconds')
