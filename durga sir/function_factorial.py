def factoral(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result

num=int(input("Enter Number"))
r=factoral(num)
print("The Factoral of {} is {}".format(num,r))
