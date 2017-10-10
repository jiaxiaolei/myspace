
class B(object):

    def __init__(self, name='', age=20):
       self.name = name 
       self.age = age 

    def get_name(self):
        pass
        #return self.name

class A(object):

    def addnewattributesfromotherclass(self,class_name):
            func_names = dir(class_name)
            for func_name in func_names:
                if  not func_name.startswith('_'):
                    new_func = getattr(class_name,func_name)
                    self.__setattr__(func_name,new_func)
                    #self.__setattr__(func_name,new_func())


a = A()

print dir(a)
b = B()
print dir(b)

a.addnewattributesfromotherclass(b)
print dir(a)

"""
output:

['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'addnewattributesfromotherclass']
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'get_name', 'name']
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'addnewattributesfromotherclass', 'age', 'get_name', 'name']
"""

