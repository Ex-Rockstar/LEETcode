class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        k = int(num ** 0.5)*int(num ** 0.5)
        if(k == num):
            return True
        else:
            return False 