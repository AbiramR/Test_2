 #Ask a user their name
# If their first name starts with A or B 
# tell them they go to room AB
# IF their first name starts with C
# tell them to go to room CD
# If their first name starts with another letter, ask for their last name
# IF their last name starts with Z, tell them to go to room Z
# if their last name starts with any other letter, tell them to go to room OTHER
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z


f_name=str(input('Enter your first name:'))

print(f_name[0].lower())

if f_name[0].lower() in ('a','b'):
	print('Goto Room : AB')
	
elif f_name[0].lower()== 'c':
	print('Goto Room : CD')
	
else:
	l_name=str(input('Enter your last name:'))
	
	if l_name[0].lower()== 'z':
		print('Goto Room : Z')
	else:
		print('Goto the \"OTHER\" Room')
	
		
