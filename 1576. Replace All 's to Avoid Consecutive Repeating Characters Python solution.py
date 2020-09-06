class Solution:
    def modifyString(self, l: str) -> str:  
        if l[0]=="?": 
            if len(l)==1: 
                return "a" 
            if len(l)==2: 
                if l[1]=="?": 
                    return "ab" 
                elif l[1]=="z": 
                    return "az" 
                else: 
                    return chr(ord(l[1])+1)+l[1]   
        l=list(l)
        if l[0]=="?": 
            if l[1]=="?": 
                if l[2]=="?": 
                    l=["a","b"]+l[2:]
                else: 
                    l[0]="a" 
            else: 
                if l[1]=="z": 
                    l[0]="y" 
                else: 
                    l[0]=chr(ord(l[1])+1)
        for i in range(1,len(l)-1): 
            if l[i]=="?": 
                if l[i+1]=="?":
                    l[i]=chr(ord(l[i-1])+1) 
                else: 
                    if l[i-1]==l[i+1]:
                        if l[i]=="z":
                            l[i]="y"
                        else:
                            l[i]=chr(ord(l[i-1])+1) 
                    else: 
                        if ord(l[i-1])+1==ord(l[i+1]): 
                            if l[i-1]=="a":
                                l[i]="c"
                            else:
                                l[i]=chr(ord(l[i-1])-1) 
                        elif ord(l[i-1])==ord(l[i+1])+1: 
                            if l[i]=="z":
                                l[i]="x"
                            else:
                                l[i]=chr(ord(l[i+1])-1)
                        else:
                            if abs(ord(l[i-1])-ord(l[i+1]))==2:
                                if l[i-1]=="a":
                                    l[i]="d"
                                elif l[i+1]=="a":
                                    l[i]="d"
                                elif l[i-1]=="z" or l[i+1]=="z":
                                    l[i]="x"
                                elif l[i-1]=="b":
                                    l[i]="a"
                                else:
                                    l[i]=chr(ord(l[i-1])-3)
                            else:
                                l[i]=chr(ord(l[i-1])+1)

        if l[-1]=="?": 
            if l[-2]=="z": 
                l[-1]="y" 
            else: 
                l[-1]=chr(ord(l[-2])+1)
        return "".join(l)