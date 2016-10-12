# encoding=utf-8

class Solution(object):
    # time limit exceed
    # 动态规划解决
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """

        max_idx = 0
        max_len = 0

        strlen = len(s)
        if strlen == 0:
            return s

        table = [[False for i in range(strlen)] for i in range(strlen)]
        # print table
        for i in range(strlen):
            table[i][i] = True
            max_len = 1
            max_idx = i
        for i in range(strlen-1):
            if s[i] == s[i+1]:
                table[i][i+1] = True
                max_len = 2
                max_idx = i
        for nowlen in range(3, strlen+1):
            for i in range(strlen-nowlen+1):
                if s[i] == s[i+nowlen-1] and table[i+1][i+nowlen-2] == True:
                    max_len = nowlen
                    table[i][i+nowlen-1] = True
                    max_idx = i
        res = s[max_idx:max_idx + max_len]
        return res
    def expandstr(self, s, left, right):
        strlen = len(s)
        l = left
        r = right
        while(l > -1 and r < strlen and s[l]==s[r]):
            l-=1
            r+=1
        l += 1
        r -= 1
        return s[l:r+1]

    # 以每个为中心,每个分别找最长的长度
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        strlen = len(s)
        if strlen == 0:
            return s
        res = s[0]
        for i in range(strlen):
            p1 = self.expandstr(s, i, i)
            if len(p1) > len(res):
                res = p1
            p2 = self.expandstr(s, i , i+1)
            if len(p2) > len(res):
                res = p2
        return res

s = Solution()
print  s.longestPalindrome("lphbehiapswjudnbcossedgioawodnwdruaaxhbkwrxyzaxygmnjgwysafuqbmtzwdkihbwkrjefrsgjbrycembzzlwhxneiijgzidhngbmxwkhphoctpilgooitqbpjxhwrekiqupmlcvawaiposqttsdgzcsjqrmlgyvkkipfigttahljdhtksrozehkzgshekeaxezrswvtinyouomqybqsrtegwwqhqivgnyehpzrhgzckpnnpvajqevbzeksvbezoqygjtdouecnhpjibmsgmcqcgxwzlzztdneahixxhwwuehfsiqghgeunpxgvavqbqrelnvhnnyqnjqfysfltclzeoaletjfzskzvcdwhlbmwbdkxnyqappjzwlowslwcbbmcxoiqkjaqqwvkybimebapkorhfdzntodhpbhgmsspgkbetmgkqlolsltpulgsmyapgjeswazvhxedqsypejwuzlvegtusjcsoenrcmypexkjxyduohlvkhwbrtzjnarusbouwamazzejhnetfqbidalfomecehfmzqkhndpkxinzkpxvhwargbwvaeqbzdhxzmmeeozxxtzpylohvdwoqocvutcelgdsnmubyeeeufdaoznxpvdiwnkjliqtgcmvhilndcdelpnilszzerdcuokyhcxjuedjielvngarsgxkemvhlzuprywlypxeezaxoqfges")
