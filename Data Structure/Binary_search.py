l=[4, 9, 10, 20, 45, 56]
s=56
low=0
high=len(l)-1
mid=(low+high)//2
while l[mid]!=s and low<=high:
    if s<l[mid]:
        high=mid-1
    else:
        low=mid+1
    mid=(low+high)//2
if l[mid]==s:
    print(mid)
else:
    print(0-1)
