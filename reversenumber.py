class Solution:
    def reverse(self, x: int) -> int:
        c=1
        if(x<0):
            c=-1
            # sym=-1
            x=x*-1
        s=str(x)
        s=s[::-1]
        s=int(s)
        s*=c
        if(s>2147483647):
            return 0
        elif(s<-2147483648):
            return 0
        return(s)



