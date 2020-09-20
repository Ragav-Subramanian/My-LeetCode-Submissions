class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        l=len(str(low))
        f=len(str(high))
        s=len(str(low)[0])
        a=[]
        for i in range(l,f+1):
            while True:
                t=''
                if i+s>10:
                    break
                for j in range(s,i+s):
                    t+=str(j)
                if int(t)>high:
                    break
                if int(t)<low:
                    s+=1
                    continue
                s+=1
                a.append(t)
            s=1
        return a