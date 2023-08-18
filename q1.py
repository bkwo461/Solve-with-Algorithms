import sys

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



def delete_sub_node(lst, value):
    ans = []

    for element in lst:
        replaced = element.replace(str(value) + " ", "")
        replaced = replaced.replace(" " + str(value), "")
        replaced = replaced.replace(str(value), "")
        ans.append(replaced)

    return ans


def delete_node(lists):
    modified_lst = []

    for lst in lists:
        d = len(lst) - 3
        lst.pop(d)
        modified = delete_sub_node(lst, d)
        modified_lst.append(modified)

    return modified_lst


def deduce(s, length):
    if len(s) > 1:
        e = s.split()

        x = []                    
        for _ in e:
            if ( (int(_) == length - 1) or (int(_) == length) ):
                val = int(_) - 1
                x.append(str(val))
            else:
                x.append(_)
        
        ans = " ".join(val for val in x)
        return ans
    
    else:
        if ( (int(s) == length - 1) or (int(s) == length) ):
            val = int(s) - 1
            return str(val)
        else:
            return s


def display(lists):
    for lst in lists:
        print(len(lst))
        for element in lst:
            if element == "":
                print(element)
            else:
                _ = deduce(element, len(lst))
                print(_)

    print("0")



output = delete_node(digraphs)
display(output)