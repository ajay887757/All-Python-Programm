class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i in range(len(columnTitle)):
            result =result* 26
            print("result",result)
            print(ord(columnTitle[i]),"ctitle")
            result = result+ ord(columnTitle[i]) - ord('A') + 1
        return result
                
            


s=Solution()
print(s.titleToNumber("AAB"))  #1

#print(s.titleToNumber("AB"))  #28

#print(s.titleToNumber("ZY"))   #701




