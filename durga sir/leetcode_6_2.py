class Solution:
    def romanToInt(self, s: str) -> int:

        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        count=0
        a=0
        b=1
        l=len(s)
        j=0
        for i in range(l):
            try:
                if d[s[a]]<d[s[b]]:
                    r=d[s[b]]-d[s[a]]
                    count=count+r
                else:
                    count=count+d[s[i]]
           
            except:
                if d[s[i]]<d[s[i+1]]:
                    r=d[s[i+1]]-d[s[i]]
                    count=count+r
                else:
                    count=count+d[s[i]]
            
        return count
s1=Solution()
print(s1.romanToInt("III"))   #3
print(s1.romanToInt("LVIII"))  #58
print(s1.romanToInt("MCMXCIV")) #1994
