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

'''def add(x,y):
	return x+y 
def cal(func,x,y):
	return func(4,6)
result=cal(add,4,6)
print(result)		
'''

#return a function as a value

'''def greeting(name):
	def hello():
		return 'Hello, ' +name+'!'
	return hello

greet=greeting('Hebol')
print(greet())'''

'''def make_pretty(func):
	def inner():
		print('I got decorated')
		func()
	return inner
	

def ordinary():
	print('I am ordinary')


#decorate ordinary function
decorated_func=make_pretty(ordinary)
decorated_func()'''

'''def make_pretty(func):
	def inner():
		print('I got decorated')
		func()
	return inner
	

@make_pretty
def ordinary():
	print('I am ordinary')

ordinary()'''

def my_decorator(func):
	def wrap_func():
		print('************')
		func()
		print('*************')

	return wrap_func

@my_decorator
def hello():
	print('hellloooooooo')	

hello()			

