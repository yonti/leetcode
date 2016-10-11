class Solution(object):
    def convert(self, s, numRows):
        res = ""
        if numRows == 1:
            return s
        strlen = len(s)
        interval = 2*numRows -2;
        col = 0;
        while True:
            if col * interval < strlen:
                res += s[col*interval]
                col += 1
            else:
                break
        for row in range(1, numRows-1):
            col = 0
            while True:
                if row + interval*col < strlen:
                    res += s[row + interval*col]
                    if row + interval * col + (numRows - 1 - row) * 2 < strlen:
                        res += s[row + interval * col + (numRows - 1 - row) * 2]
                    col += 1
                else:
                    break
        col = 0
        while True:
            if col * interval + numRows-1 < strlen:
                res += s[col * interval + numRows-1]
                col += 1
            else:
                break

        return res

s = Solution()
print s.convert("ABC", 2)