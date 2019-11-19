from sys import argv
script, filename =argv
print("are you sure you want to delete the content")
print("Really sure")
input("?")
target=open(filename, 'w')# file is open in read only mode by default ,so need to open in write mode to delete content
print("truncating the file")
target.truncate()
print("filecontent are now deleted")

line1 = input("line 1")
line2 = input("line 2")
line3 = input("line 3")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
print("Finally we are closing it")

target.close()