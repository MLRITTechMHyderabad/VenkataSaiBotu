def max(*a) :
    max = 0
    for i in a :
        for j in i :
            if j > max :
                max = j
    return max

def min(*a) :
    min = a[1][1]
    for i in a :
        for j in i :
            if j < min :
                min = j
    return min

print('max =',max([1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]))
print('min =',min([1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]))