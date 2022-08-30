class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x**(1/2))
c = Solution.mySqrt(90)
print(c)