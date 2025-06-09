a = [3,30,34,5,9] 
# o/p -> 9534330
# a = [0,0] o/p -> [o]

if len(set(a)) == 1 and a[0] == 0:
    print(set(a))
else:
    
    maxi = ""
    for i in range(len(a)):
        
        for j in range(i+1,len(a)):
            
            num_ij = int(str(a[i]) + str(a[j]))
            num_ji = int(str(a[j]) + str(a[i]))
            
            if num_ji > num_ij:
                a[i],a[j] = a[j],a[i]
                print(num_ji)
                
        
        maxi += str(a[i])

    print(maxi)