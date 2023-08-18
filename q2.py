import sys


def DFS(digraph, checklst):

    no_of_nodes = len(digraph)
    
    color = ["white"] * no_of_nodes
    pred = [None] * no_of_nodes
    seen = [0] * no_of_nodes
    done = [0] * no_of_nodes

    time = 0

    for node in range(0, no_of_nodes):
        if color[node] == "white":
            output = RecursiveDFSvisit(digraph, node, color, pred, seen, done, time, checklst)
            digraph, node, color, pred, seen, done, time, checklst = output[0], output[1], output[2], output[3], output[4], output[5], output[6], output[7]
        else:
            pass

    return seen, done, checklst


def RecursiveDFSvisit(digraph, node, color, pred, seen, done, time, checklst):
    node = int(node)
    color[node] = "grey"
    seen[node] = time
    time += 1
    
    _ = digraph[node]
    subnodes = _.split(" ")

    for subnode in subnodes:

        c = getColor(node, subnode, color)
        if c[0] == "grey" and c[1] == "black":
            arc = [node, subnode]
            checklst.append(arc)


        if subnode == "":
            pass
        elif color[int(subnode)] == "white":
            pred[int(subnode)] = int(node)
            output = RecursiveDFSvisit(digraph, subnode, color, pred, seen, done, time, checklst)

            digraph, subnode, color, pred, seen, done, time = output[0], output[1], output[2], output[3], output[4], output[5], output[6]
    
    color[node] = "black"
    done[node] = time
    time += 1

    return digraph, node, color, pred, seen, done, time, checklst


def getColor(n1, n2, color):
    if n1 == "" or n2 == "":
        return "", ""
    else:
        return color[int(n1)], color[int(n2)]


def Forward(checklst, seen, done):
    for element in checklst:

        v = int(element[0])
        w = int(element[1])

        if seen[v] < seen[w] and seen[w] < done[w] and done[w] < done[v]:
            return str(v), str(w)
        else:
            pass

    return ""
        
    
def Cross(checklst, seen, done):
    for element in checklst:
    
        v = int(element[0])
        w = int(element[1])
        
        if seen[w] < done[w] and done[w] < seen[v] and seen[v] < done[v]:
            return str(v), str(w)
        else:
            pass

    return ""


def getData():
    file = sys.stdin.read().splitlines()

    digraphs = []
    lst = []
    order = 0

    for cnt in range (0, len(file)):
        if order == 0:
            order = int(file[cnt])
            continue

        if order != 0:
            lst.append(file[cnt])
            order -= 1
            if order == 0:
                digraphs.append(lst)
                lst = []
    
    return digraphs


def main():
    digraphs = getData()
    for digraph in digraphs:

        checklst = []
        output = DFS(digraph, checklst)
        seen, done, checklst = output[0], output[1], output[2]

        forward = Forward(checklst, seen, done)
        cross = Cross(checklst, seen, done)

        if forward == "":
            print(forward)
        else:
            print(forward[0] + "," + forward[1])
        
        if cross == "":
            print(cross)
        else:
            print(cross[0] + "," + cross[1])

    print(end="")



main()

