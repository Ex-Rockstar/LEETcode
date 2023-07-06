class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n=len(s)
        rep =''

        for i in range(n//2):
            rep +=s[i]
            if (rep * (n//(i+1))) == s:
                return True
        else:
            return False



        