class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        md=2
        c=1 
        j=0
        while seats[j]!=1:
            j+=1
        for i in range(j,len(seats)):
            if seats[i]==0:
                c+=1 
            else:
                md=max(md,c)
                c=1 
        if seats[-1]==0:
            return max(md//2,c-1,j)
        return max(md//2,j)