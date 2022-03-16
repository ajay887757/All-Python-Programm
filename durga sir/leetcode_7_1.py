class Solution:
    def containsDuplicate(self, nums) -> bool:
        d={}
        for i in nums:
            if i in nums:
                d[i]=d.get(i,0)+1
        print(d)

        for k,v in d.items():

            if v>=2:
                return "true"
            else:
                return "false"
                
            

s1=Solution()
print(s1.containsDuplicate([1,2,3,1]))
print(s1.containsDuplicate([1,2,3,4]))




