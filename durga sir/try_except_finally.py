try:
    print("try")
    print(10/0)

except ZeroDivisionError as msg:
    print(msg)
    print(ZeroDivisionError.__name__)

else:
    print('else block')

finally:
    print("finally")
