def con1(arr):

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
		
		
binarr=['1', '0', '1', '1', '0', '1', '1', '1', '0', '1', '1', '0', '1', '1', '1', '1', '1', '1', '0', '1']


#n=len(binarr)

print(con1(binarr))
