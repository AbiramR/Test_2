def consecutive_1s(arr):

	count=0
	mx=0
	
	for i in range(len(arr)):
	
		if arr[i]=='1':
		
			count+=1

			if count>mx:
				mx=count
				
		else:
			count=0
	return mx
		
		

binnum=input('enter the binary number:')
binarr=list(str(binnum))

print('Binary Array:',binarr)

print(consecutive_1s(binarr))



