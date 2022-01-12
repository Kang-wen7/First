class MyClass (object):
	pass

my_instance = MyClass()
MyClass.class_attribute = 'hello'
my_instance.instance_attributes = 'world'
dir(my_instance)
['__class__', ... , 'class_attribute', 'instance_attribute']
print(my_instance.__class__)
#<class '>>main__.MyClass'>
type(my_instance)
#<class '>>main__.MyClass'>
print(my_instance.instance_attribute)
print(my_instance.class_attribute)
#print(MyClass.instance_attribute)
