from sys import argv
script, filename = argv

def print_all(f):
	print(f.read())

	
def rewind(f):
	print(f.seek(5))# go to the 6th byte in the file
	
def print_line(line_count,f):
		print(line_count, f.readline())
		
f = open(filename)

print("print all content of file")
print_all(f)
print("rewind all content of file")
rewind(f)
linenumber=1
print_line(linenumber, f)
linenumber=linenumber+1
print_line(linenumber, f)