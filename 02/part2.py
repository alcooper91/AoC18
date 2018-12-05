import itertools
ids = open("Input.txt", "r")

for i, j in (itertools.combinations(ids.read().splitlines(), 2)):
    diff_pos = -1
    for x in range(len(i)):
        if i[x] != j[x]:
            if diff_pos != -1:
                diff_pos = -1
                break
            else:
                diff_pos = x
    if diff_pos != -1:
        print(diff_pos)
        strList = list(i)
        strList.pop(diff_pos)
        print("2nd part: %s" % ''.join(strList))
        break

ids.close()