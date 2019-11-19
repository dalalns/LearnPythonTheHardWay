types_of_people = 10
x = f"There are {types_of_people} types of people."
print(x)
binary = "binary"
hilarious=False
joke_evaluation = "Is'nt that joke so funny {} {} {}"
print(joke_evaluation.format(hilarious,x,"good"))
print('.'*10)
end1='C'
end2='h'
end3='e'
end4='e'
end5='s'
end6='e'
end7='B'
end8='u'
end9='r'
end10='g'
end11='e'
end12='r'

print(end1+end2+end3+end4+end5+end6,end=' ')#end is by default as newline and if ' ' than next print statement will be executed after the space
print(end7+end8+end9+end10+end11+end12)

formatter = '{} {} {} {}'

print(formatter.format(1,2,3,4)) # this will print 1,2,3,4

print(formatter.format('one','two','three','four'))

print(formatter.format(True,False,False,True))

print(formatter.format(
						"Try your",
						"own text here",
						"Maybe a poem",
						"or a song about fear"
					  ))

print(formatter.format(formatter,formatter,formatter,formatter)) # this will print the string '{} {} {} {}' four times