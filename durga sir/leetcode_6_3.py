class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l=[]
        for i in s:
            if i in t:
                l.append(i)
            else:
                return "false"
        
        return len(l)==len(s)

s1=Solution()
print(s1.isAnagram("anagram","nagaram"))
print(s1.isAnagram("rat","car"))

