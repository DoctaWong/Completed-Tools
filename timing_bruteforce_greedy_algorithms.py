import time


def greedy_cow_transport(cows,limit=10):
    start = time.time()
    trip = []
    next = []
    cows_dupe = dict(cows)
    newLimit = limit
    working_cows = []
    while len(working_cows) < len(cows):
        for e in cows:
            working_cows.append(max(cows_dupe, key = lambda x: cows_dupe.get(x)))
            del cows_dupe[(max(cows_dupe, key = lambda x: cows_dupe.get(x)))]
    while working_cows != []:       
        for e in working_cows: 
            if newLimit - cows[e] >= 0:
                next.append(e)
                newLimit -= cows[e]
        trip.append(next)
        newLimit = limit
        for i in next:
            working_cows.remove(i)
        next = []
    end = time.time()
    print(end-start)
    return trip

def brute_force_cow_transport(cows,limit=10):
    start = time.time()
    sum = 0
    n = True
    possible = []
    tot = 0
    count =0
    shortest = len(cows)
    ans = None
    for e in get_partitions(cows):
        n = True    
        for l in e:
            sum = 0
            for i in l:
                sum += cows[i]
                if sum > limit:
                    n = False
                    break
            if n == False:
                break
        if n == True:
            possible.append(e)
            tot += 1
    for e in possible:
        count = 0
        for i in e:
            count += 1
        if count <= shortest:
            shortest = count
            ans = e
        end = time.time()
    print(end-start)
    return ans
