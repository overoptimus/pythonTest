class Celsius:
    def __init__(self, value = 26.0):
        self.value = float(value)

    # def __init__(self, fget, fset, fdel):
    #     self.fget = fget
    #     self.fset = fset
    #     self.fdel = fdel
    #
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)

    # def __delete__(self, instance):
    #     del self.fdel(instance)

class Fahrenheit:
    def __get__(self,instance, owner):
        return instance.cel * 1.8 +32

    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8

class Temperature:
    # cel = None
    # fah = None
    def __init__(self):
        self.cel = Celsius()
        self.fah = Fahrenheit()
