words_upto_19=['','ONE','TWO','THREE','FOUR','FIVE','SIX',
'SEVEN','EIGHT','NINE','TEN','ELEVEN','TWELVE','THIRTEEN','FOURTEEN','FIFTEEN','SIXTEEN','SEVENTEEN','EIGHTEEN','NINETEEN']

words_for_tens=['','','TWENTY','THIRTY','FOURTY','FIFTY','SIXTY','SEVENTY','EIGHTY','NINETY']
words_for_Hun="HUNDRED"
n=int(input('Enter a number from 0 to 999:'))
output=''
if n==0:
	output='ZERO'
elif n<=19:
	output=words_upto_19[n]
elif n<=99:
	output=words_for_tens[n//10]+" "+words_upto_19[n%10]
elif n<=999:
    output=words_upto_19[n//100]+" "+words_for_Hun+" "+words_for_tens[(n%100)//10]+" "+words_upto_19[(n%100)%10]
else:
	output='Please enter a value from 0 to 999 only'
print(output)
