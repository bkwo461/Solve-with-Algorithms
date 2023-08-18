import sys


def getData():
    digraphs = []
    lst = []
    order = 0

    data = sys.stdin.read().splitlines()
    for cnt in range (0, len(data)):
        if order == 0:
            order = int(data[cnt])
            continue
        if order != 0:
            lst.append(data[cnt])
            order -= 1
            if order == 0:
                digraphs.append(lst)
                lst = []
    return digraphs


def distance(val):
    visit = [False] * len(val)
    distance = [0] * len(val)
    queue = []
    queue.append(0)
    visit[0] = True

    while queue:
        node = queue.pop(0)
        for d in val[node]:
            try:
                if visit[d] == False:
                    distance[d] = distance[node]+1
                    queue.append(d)
                    visit[d]=True
            except:
                pass

    max_distance = max(distance)
    max_distNode = distance.index(max_distance)
    print (max_distance, max_distNode)


def change_idx(lst):
    for num in lst:
        for nl in num:
            for idx in range(len(nl)):
                try:
                    nl[idx] = int(nl[idx])
                except:
                    pass
    return lst


def split_(al):
    lst = []
    for num in range(len(al)):
        al[num] = al[num].split(" ")
    lst.append(al)
    return lst


def main():
    digraphs = getData()

    for digraph in digraphs:
        lst = split_(digraph)
        lst = change_idx(lst)

        for val in lst:
            distance(val)


main()
