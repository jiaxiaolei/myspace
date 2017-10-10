# -*- coding: utf-8 -*-

class Person(object):
    """Silly Person"""
 
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def __str__(self):
        return '<Person: %s(%s)>' % (self.name, self.age)
 
if __name__ == '__main__':
    piglei = Person('piglei', 24)
    print piglei
