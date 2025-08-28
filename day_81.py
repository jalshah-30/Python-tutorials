'''Hybrid and Hierarchical Inheritance in Python'''

#Hybrid Inheritance
class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Base):
    pass

class Derived3(Derived1,Derived2):
    pass

#Hierarchiacal Inheritance

class BC1:
    pass

class D1(BC1):
    pass

class D2(BC1):
    pass

class D3(D1):
    pass
