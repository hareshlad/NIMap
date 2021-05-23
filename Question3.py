import math
 

def sumofFactors(n) :
    list_factors=[]
    sum =0
    for i in range(1, n + 1):
       if n % i == 0 and i%2==0:
           list_factors.append(i)
           sum = sum + i
     
    list_factors.sort(reverse=True)
    print(list_factors)
    print(sum)
    
    
 

n = int(input("Enter a number :"))
sumofFactors(n)
