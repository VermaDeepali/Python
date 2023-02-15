#Function to find a continuous sub-array which adds up to a given number.
#Note:- Both the indexes in the array should be according to 1-based indexing.

def subArraySum( arr, n, s):
        if s == 0:
            return [-1]
        res=0
        j=0
        for i in range(n):
            res+=arr[i]
            if res==s:
                    return j+1, i+1  
            if res>s:
                while res>s:
                    res -=arr[j]
                    j+=1
                    if res==s:
                         return j+1, i+1
        return [-1]
        
print(subArraySum([1,2,3,7], 4, 10))

# Examples
# 1. Case 1: ([1,2,3,7,5], 5, 12) Output: (2, 4)
# 2. Case 2: ([1,2,3,4,5,6,7,8,9,10], 10, 15) Output: (1, 5)
# 3. Case 3: ([1,2,3,7], 4, 10) Output: (3, 4)
