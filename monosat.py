# Graham Seamans - HW2 - Monopoles (the satening)

import sys

if __name__ == "__main__":

    if len(sys.argv) <= 2:
        monopoles = int(input('How many monopoles? '))
        rooms = int(input('How many rooms? '))
    else:
        monopoles = int(sys.argv[1])
        rooms = int(sys.argv[2])


    # make the lookup table thingy
    lookup = []
    count = 1

    # room lookup key
    for i in range(rooms):
        lookup.append([])
        lookup[i].append(0)
        for j in range(monopoles):
            lookup[i].append(count)
            count += 1


    # wasteful, but calculates how many clauses there are for 
    # the addition constraint
    count = 0
    for i in range(rooms):
        for j in range(1, monopoles + 1):
            for k in range(1, monopoles + 1):
                if (k != j and k + j < monopoles + 1):
                    count += 1

    no_clauses = rooms + rooms * monopoles + count
    print('p cnf', rooms * monopoles, no_clauses)

    # all numbers must be placed
    # (1 or 4) and (2 or 5) and (3 or 6)
    for i in range(1, monopoles + 1):
        for j in range(rooms):
            print(lookup[j][i], end = ' ')
        print(0)

    # can't have the same number 2x
    for i in range(1, monopoles + 1):
        for j in range(rooms):
            print('-' + str(lookup[j][i]), end = ' ')
        print(0)

    # monopoles can't add up to eachother
    for i in range(rooms):
        for j in range(1, monopoles + 1):
            for k in range(1, monopoles + 1):
                if (k != j and k + j < monopoles + 1):
                    print('-' + str(lookup[i][j]), '-' + str(lookup[i][k]), '-' + str(lookup[i][j + k]), 0)




