class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        p='''!()-[]{};:'`"\,<>./?@#$%&*_~^ '''
        
        for i in p:

            s = s.replace(i,"")
        # print(s)
        if(s==s[::-1]):
            return True
        else:
            return False