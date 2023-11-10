#python Decorator
#Nested Function
'''def outer(x):
	def inner(y):
		return x+y
	return inner
	
add_five=outer(5)
result=add_five(6)
print(result)'''

#Higher order function

#Pass Function as Argument

def add(x,y):
	return x+y 
def cal(func,x,y):
	return func(4,6)
result=cal(add,4,6)
print(result)		


