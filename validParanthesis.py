class Solution:
    def isValid(self, s: str) -> bool:
        k='([{'
        stk=[]
        for i in s:
            if( i in k ):
                stk.append(i)
            else:
                if( not stk):
                    return False
                if(i == ')' and stk[-1] == '('):
                    stk.pop()
                elif (i=='}' and stk[-1] == '{'):
                    stk.pop()
                elif (i== ']' and stk[-1] == '['):
                    stk.pop()
                else:
                    return False
        return (not stk)
    