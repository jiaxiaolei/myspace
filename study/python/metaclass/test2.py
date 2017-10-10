# -*- coding: utf-8 -*-

class ObjectCreator(object): 
    pass

my_object = ObjectCreator()
print my_object

'''
output:
<__main__.ObjectCreator object at 0x7f83caaa8050>
'''

print ObjectCreator     # 你可以打印一个类，因为它其实也是一个对象
"""
<class '__main__.ObjectCreator'>
"""

def echo(o):
    print o

echo(ObjectCreator)                 # 你可以将类做为参数传给函数
"""
<class '__main__.ObjectCreator'>
"""

print hasattr(ObjectCreator, 'new_attribute')
"""
Fasle
"""
ObjectCreator.new_attribute = 'foo' #  你可以为类增加属性
print hasattr(ObjectCreator, 'new_attribute')
"""
True
"""
print ObjectCreator.new_attribute
"""
foo
"""
ObjectCreatorMirror = ObjectCreator # 你可以将类赋值给一个变量
print ObjectCreatorMirror()
"""
<__main__.ObjectCreator object at 0x7fec238920d0>
"""
