class Solution:
    def nextGreaterElement(self, n: int) -> int:
        number = list(map(int,str(n)))
        t=n
        n=len(str(n))
        i=n-1
        while i>0: 
            if number[i] > number[i-1]: 
                break
            i-=1
        if i == 1 and number[i] <= number[i-1]: 
            return -1
        x = number[i-1] 
        smallest = i 
        for j in range(i+1,n): 
            if number[j] > x and number[j] < number[smallest]: 
                smallest = j 
        number[smallest],number[i-1] = number[i-1], number[smallest] 
        x = 0
        for j in range(i): 
            x = x * 10 + number[j] 
        number = sorted(number[i:]) 
        for j in range(n-i): 
            x = x * 10 + number[j] 
        return x if x>t and x<2**31 else -1