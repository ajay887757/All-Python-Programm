class Solution:
    def majorityElement(self, nums) -> int:
        s=set(nums)
        d={}
        l=[]
        for i in s:
            c=nums.count(i)  # 2
            d[c]=i

        print(d)

        for k,v in d.items():
            l.append(k)
            
        m=max(l)
        #print(m)
        return d[m]

s1=Solution()

print(s1.majorityElement([3,3,4]))   #3

print(s1.majorityElement([3,2,3]))   #3

