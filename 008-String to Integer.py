# encoding=utf-8

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        strlen = len(str)
        if strlen == 0:
            return 0
        sign = 1
        if str[0] == '+':
            str = str[1:]
        elif str[0] == '-':
            sign = -1
            str = str[1:]

        res = 0
        strlen = len(str)
        for i in range(strlen):
            if str[i] < '0' or str[i] > '9':
                break
            else:
                res = res * 10 + int(str[i])
                if sign * res > 2 ** 31 - 1:
                    return 2 ** 31 - 1
                elif sign * res < -(2 ** 31):
                    return -(2 ** 31)
        return sign * res


s = Solution()
print s.myAtoi("")