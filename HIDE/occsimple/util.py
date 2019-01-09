def difference(*args):
	base = args[0]
	for i in range(1, len(args)):
		base = base - args[i]
	return base

def union(*args):
	base = args[0]
	for i in range(1, len(args)):
		base = base + args[i]
	return base

def intersection(*args):
	base = args[0]
	for i in range(1, len(args)):
		base = base ^ args[i]
	return base