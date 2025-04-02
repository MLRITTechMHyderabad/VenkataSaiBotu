def frequency(a) :
    dict = {}
    for i in a :
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

print(frequency([1,1,1,2,3,4,4,5,6]))
