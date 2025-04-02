def mergeDict(a,b) :
    dict = a
    for i in b:
        if i in dict :
            li = []
            li.append(dict[i])
            li.append(b[i])
            dict[i] = li
        else :
            dict[i] = b[i]
    return dict

a = {1:3,2:5}
b = {1:3,3:6}
print(mergeDict(a,b))
