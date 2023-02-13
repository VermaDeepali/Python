# You are given an array. 
# You have to replace all the values of the array with the nearest prime number. 
# If more than one prime number exists at an equal distance, choose the smallest one.

from math import sqrt
def isPrime(x):
    if x<2:
        return False
    if x==2 or x==3:
        return True
    if x%2==0 or x%3==0:
        return False
    for i in range(5,int(sqrt(x))+1,6):
        if (x%i==0) or (x%(i+2)==0):
            return False
    return True

def makePrime(x):
    if isPrime(x):
        return x
    if x == 1: return 2
    else:
        for i in range(1,x):
            if isPrime(x-i):
                return (x-i)
            elif isPrime(x+i):
                return (x+i)
    return x

def primeList(arr):
    primeArray = []
    for i in range(len(arr)):
        primeData = makePrime(arr[i])
        primeArray.append(primeData)
    return primeArray
        
print(primeList([2,4,5,8,15]))


# Examples
# 1. Case 1: [1, 3, 4] Output: [2, 3, 3]
# 2. Case 2: [2, 6, 10] Output: [2, 5, 11]
# 3. Case 3: [1, 15, 20] Output: [2, 13, 19]
# 4. Case 4: [2,4,5,8,15] Output: [2, 3, 5, 7, 13]
