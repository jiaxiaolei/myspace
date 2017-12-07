# -*- coding: utf-8 -*-  

class AttrTest(object):
    def __init__(self):
        self.__info = "AttrTest:"
        self.field = "invalidField"

    @property
    def Info(self):
        return self.__info

    @Info.setter
    def Info(self, new_value):
        self.__info = new_value

    @Info.deleter
    def Info(self):
        del self.__info

    @staticmethod
    def JoinSM(a, b):
        return str(a) + str(b)

    def JoinX(a, b):
        """这个函数实际上属于staticmethod,这种定义不太好"""
        return "Join2:" + str(a) + str(b)

    def JoinNSM(self, a, b):
        return self.__info + str(a) + str(b)


if __name__ == "__main__":
    print("============")
    if hasattr(AttrTest, "JoinSM"):
        attr = getattr(AttrTest, "JoinSM")
        print(attr)
        print(attr('abcde', '12345'))
    print("============")
    #if hasattr(AttrTest, "JoinX"):
    #    attr = getattr(AttrTest, "JoinX")
    #    print(attr)
    #    print(attr('abcde', '12345'))
    print("============")
    at = AttrTest()
    if hasattr(at, "JoinNSM"):
        attr = getattr(at, "JoinNSM")
        print(attr)
        print(attr('abcde', '12345'))
    print("============")
    if hasattr(AttrTest, "JoinNSM"):
        attr = getattr(AttrTest, "JoinNSM")
        print(attr)
        print(attr(at, 'abcde', '12345'))
    print("============")
    if hasattr(at, "JoinSM"):
        attr = getattr(at, "JoinSM")
        print(attr)
        print(attr("abcde", "12345"))
    print("============")
    if hasattr(at, "Info"):
        print(getattr(at, "Info"))
        setattr(at, "Info", "at:")
        print(getattr(at, "Info"))
    print("============")
    if hasattr(at, "field"):
        print(getattr(at, "field"))
        setattr(at, "field", "validField")
        print(getattr(at, "field"))
    print("============")
    print("WILL EXIT...")
    exit(0)
