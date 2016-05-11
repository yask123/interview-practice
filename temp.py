import copy
class test:
    def __init__(self,value):
        self.test_value = value

a = test(2)
b = copy.copy(a)
a.test_value = 5

print b.test_value
