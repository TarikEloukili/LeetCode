class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        y = str(x)
        n = len(y)
        if n==1:
            return True
        i=0
        j=n-1
        for i in range(n):
            if y[i]!=y[n-i-1]:
                return False
        return True
                
        