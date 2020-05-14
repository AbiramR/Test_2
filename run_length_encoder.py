def rl_encoder(inp=''):
	
	count=0
	encoded_str=''
	prev=''
	for current in inp:
	
		if prev=='':
			prev=current
			letter=current
			count=1
		else:
			if current==prev:
				count+=1
				
			else:
				encoded_str += str(count) + prev
				prev=current
				count=1
				
	encoded_str += str(count) + prev	
	print(encoded_str)
		
	
string='AAAABBBCCDAA'
string1='AABBBAAA'
rl_encoder(string)
#rl_encoder(string1)
