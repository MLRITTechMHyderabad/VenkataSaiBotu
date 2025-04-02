def transpose(*a) :
   li = []
   pos = 0
   for i in a :
      temp =[]
      for j in a :
        temp.append(j[pos])
      li.append(temp)
      pos += 1
   return li

print(transpose([1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]))