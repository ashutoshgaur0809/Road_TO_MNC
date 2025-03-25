
def brute(a):

    maxi = 0
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            
            if a[i] < a[j]:
                sumi = a[j] - a[i]
                maxi = max(sumi, maxi)

    print("Maxi profit from this array is ",maxi)
    
def optimal(a):
    
    min_price = float("inf")
    max_profit = 0
    
    for i in range(len(a)):
        min_price = min(a[i],min_price)
        max_profit = max(max_profit,a[i]-min_price)
    
    print("Maxi profit from this array is ",max_profit)
    
a = [7,1,5,3,6,4]

brute(a)
optimal(a)

    