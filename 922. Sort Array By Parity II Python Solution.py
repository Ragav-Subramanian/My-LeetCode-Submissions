class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        e=[]
        o=[]
        for i in A:
            if i%2==0:
                e.append(i)
            else:
                o.append(i)
        a=0
        b=0
        for i in range(len(A)):
            if i%2==0:
                A[i]=e[a]
                a+=1
            else:
                A[i]=o[b]
                b+=1
        return A