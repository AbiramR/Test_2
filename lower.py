def ToLowerCase(lm ):
	if len(lm)==0:
		print('Empty String!!')
	else:
		new_lm=lm.lower()
		return new_lm
	
c=str(input('Enter the string:'))
print(ToLowerCase(c))
