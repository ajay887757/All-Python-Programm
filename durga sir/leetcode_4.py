class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l1=[]
        l2=[]
        for i in nums:
            if i !=0:
                print(i)
                l1.append(i)
            else:
                print(i)
                l2.append(i)
            l=l1+l2
        return l

s=Solution()
print(s.moveZeroes([0,1,0,3,12]))
