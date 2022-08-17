class Solution:
    def commonprefix(self, ListofStrs):
        res = ''
        for i in range(len(ListofStrs[0])):
            for s in ListofStrs:
                if i == len(s) or s[i] != ListofStrs[0][i]:
                    return res
            
            res += ListofStrs[0][i]
        return res

cls = Solution()
av = cls.commonprefix(ListofStrs = ["SonalAkash","Sonal"])
print(av)