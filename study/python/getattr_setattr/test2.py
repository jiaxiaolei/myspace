# -*- coding: utf-8 -*-

"""

http://www.cnblogs.com/skytraveler/p/3855645.html
"""

__author__ = 'lucas'

class attrtest(object):

    def __init__(self):
        pass

    def trygetattr0(self):
        self.name = 'lucas'
        print self.name
        #equals to self.name
        print getattr(self,'name')

    def attribute1(self,para1):
        print 'attribute1 called and '+ para1+' is passed in as a parameter'

    def trygetattr(self):
        fun = getattr(self,'attribute1')
        print type(fun)
        fun('crown')


if __name__=='__main__':
    test = attrtest()
    print 'getattr(self,\'name\') equals to self.name '
    test.trygetattr0()
    print 'attribute1 is indirectly called by fun()'
    test.trygetattr()
    print 'attrribute1 is directly called'
    test.attribute1('tomato')
