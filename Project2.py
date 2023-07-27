class SingletonMeta(type):
    _instances = {}

    def __new__(cls, name, bases, attrs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__new__(cls, name, bases, attrs)
        return cls._instances[cls]

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Bool(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return f"This is {self.__class__.__name__} class which metaclass is SingletonMeta"


class Hundred(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return f"This is {self.__class__.__name__} class which metaclass is SingletonMeta"


b1 = Bool(True)
b2 = Bool([])
print(b1 is b2)

s1 = Hundred(1555)
s2 = Hundred(958)
print(s1 is s2)
