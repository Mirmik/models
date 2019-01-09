def union(*args):
	ret = args[0]
	for i in range(1,len(args)):
		ret = ret + args[i]
	return ret

def difference(*args):
	ret = args[0]
	for i in range(1,len(args)):
		ret = ret - args[i]
	return ret