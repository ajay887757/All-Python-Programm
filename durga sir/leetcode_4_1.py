class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=nums.count(0)
        for i in range(c):
            nums.remove(0)
            nums.append(0)
        return nums

s=Solution()
print(s.moveZeroes([0,1,0,3,12]))

