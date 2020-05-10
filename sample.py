def evensq(num):

	new_num=[]
	for i,f in enumerate(num):
		if i%2==0:
			f=f**2
		new_num.append(f)	
		#print(f)
	return new_num
		
			
num=[12,21,28,14,56,41,33,5,30,76,19,26,38]

print(evensq(num))	
		
	
	
	
	
#	if len(num)==0:
#		print('The list is EMPTY!')
#	
#		else:
#			for i in range(len(num)):
#				if i%2==0:
#					num[i]=num[i]**2
				
#			return num
