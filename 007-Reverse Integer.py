# encoding=utf-8

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = ""
        if x == 0 :
            return 0
        elif x > 0:
            strx = str(x)
            strlen = len(strx)
            for i in range(len(strx)):
                res += strx[strlen - 1 -i]
            if int(res) > 2147483647:
                return 0
            return int(res)
        elif x < 0:
            strx = str(x)[1:]
            strlen = len(strx)
            for i in range(len(strx)):
                res += strx[strlen - 1 - i]
            if int(res) > 2147483648:
                return 0
            return -int(res)


s = Solution()
print s.reverse(1534236469)