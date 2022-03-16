class Solution:
    def myAtoi(self, s: str) -> int:
        r=""
        t=s.replace(" ","")
        for i in t:
            if ord(s[0])>=65 and ord(s[0])<=122:
                r=r+"0"
                break
            elif ord(i)>=65 and ord(i)<=122:
                    continue
            else:
                r=r+i
        result=int(r)
        print(r)
        if result in range(2147483648) or result in range(-2147483648,0) :
            return result
        elif r[0]=="+":
            return 2147483648
        elif r[0]=="-":
            return -2147483648
            
                
s=Solution()
print(s.myAtoi("4193 with words"))
                
        
