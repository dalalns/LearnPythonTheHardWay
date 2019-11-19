def print_one(arg1):
	return (f"single argument {arg1}")

def print_two(arg1,arg2):
	return (f"The two arguments are {arg1} and {arg2}")
	
def print_none():
	return ("The single argument is None")
	
def print_two_again(*args):
	arg1,arg2 = args
	return (f" The two arguments are {arg1} and {arg2}")
print(print_none())
print(print_one("abcd"))
print(print_two("navin",'monika'))
print(print_two_again("anju",'nikhil'))
	
	