class Solution:
    def getSum(self, a: int, b: int):

        while b!=0:
            c=a&b
            a=a^b
            b=c<<1
        return a
        
s=Solution()
print(s.getSum(a = 5, b = 4))

