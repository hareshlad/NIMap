import math
 

def sumofFactors(n) :
    list_factors=[]
    prime_flag=True
    sum =0
    for i in range(1, n + 1):
       if n % i == 0 and i%2==0:
           prime_flag=False
           list_factors.append(i)
           sum = sum + i
    if prime_flag:
        print("Enter a different number")
    else:
        list_factors.sort(reverse=True)
        print(list_factors)
        print(sum)
    
    
 

n = int(input("Enter a number :"))
if(n<10):
    print('Invalid Input')
else:
    sumofFactors(n)
