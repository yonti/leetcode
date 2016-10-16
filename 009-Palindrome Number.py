# encoding=utf-8

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            tempx = x
            bits = 1
            while(tempx /10 >0):
                tempx /= 10
                bits += 1

            for i in range(bits/2):
                left = (x / (10**(bits-1-i)))%10
                right = (x /(10**(i)))%10
                if left != right:
                    return False
            return True
s = Solution()
print s.isPalindrome(123465321)