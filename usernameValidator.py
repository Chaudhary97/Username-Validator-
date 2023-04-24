import string

def validator_arg_1(name):
	if len(name) <= 25 and len(name) >= 4:
		return True
	else:
		print('Please Enter A Username with More than 4 and Less than 25 chracters.')
		return False
		
def validator_arg_2(name):
	name = [i for i in name]
	if name[0] in string.ascii_letters:
		return True
	else:
		return False

def validator_arg_3(name):
	lst = [i for i in string.ascii_letters]
	lst += [i for i in str(string.digits)]
	lst += '_'
	list1 = []
	name = [i for i in name]
	for i in name:
		if i in lst:
			list1.append(i)
		else:
			return False
	if len(list1) == len(name):
			return True
	else:
			return False
			
def validator_arg_4(name):
	name = [i for i in name]
	if name[-1] == '_':
		return False
	else:
		return True

x = input("Enter Your Username :")

def validator(x):
	for i in range(2):
		if validator_arg_1(x) == True:
				if validator_arg_2(x) == True:
					if validator_arg_3(x) == True:
						if validator_arg_4(x) == True:
							return True
						else:
							return False
					else:
						return False
				else:
					return False
		else:
			return False
	
print(validator(x))