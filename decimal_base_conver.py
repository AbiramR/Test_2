def decimal_to_anybase(val,b):
	
	new_val=''
	while val>0:
		rem=val%b
		if rem<10:
			new_val +=str(rem)
		else:
			new_val+=chr(ord('A')+rem-10)
		val=val//b
	new_val=new_val[::-1]
	return new_val		

num=int(input('Enter the value:'))
new_base=int(input('enter the base to be converted into:'))

print(num,' in base ',new_base,':',decimal_to_anybase(num,new_base))	
