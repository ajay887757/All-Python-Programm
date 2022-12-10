mail=input("Enter your Mail Id")
try:
    mail.index('@')
    print('your mail id cantain @ symbool')
except ValueError:
    print('your mail id dont cantain @symbol')
