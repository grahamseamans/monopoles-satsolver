import fileinput
import sys

if __name__ == "__main__":

    monopoles = int(sys.argv[1])
    rooms = int(sys.argv[2])

    # make the lookup table thingy
    lookup = {}
    count = 1
    ans = []
    t_table = []

    #where the answer will go
    for i in range(rooms):
        ans.append([])

    #where the lookup dict
    for i in range(rooms):
        for j in range(1, monopoles + 1):
            lookup[count] = (i,j)
            count += 1 

    for line in sys.stdin:
        t_table.append(line)

    if t_table[0] == 'UNSAT\n':
        print('UNSAT')
    else:
        t_table = t_table[1]
        t_table = t_table.split(' ')
        t_table = t_table[:-1]
        for i in range(len(t_table)):
            t_table[i] = int(t_table[i])
        
        for i in t_table:
            if i > 0:
                (x, y) = lookup.get(i)
                ans[x].append(y)
                pass

        for room in ans:
            if room:
                print(room)
            