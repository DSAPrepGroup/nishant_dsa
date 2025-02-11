# implementation of equals and hash function in python

# 1. __eq__

'''This method determines when two objects are considered equal. Use relevant attributes for comparison.'''

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        if isinstance(other, MyClass):
            return self.a == other.a and self.b == other.b
        return False

# 2. __hash__

'''This method computes the hash value of the object. Use the same attributes as in __eq__.'''

    def __hash__(self):
        return hash((self.a, self.b))

'''
Objects that are equal (__eq__) must have the same hash (__hash__) value.
Avoid using mutable attributes in __hash__, as changing them would make the object unusable in hash-based collections like dictionaries or sets245.
If you override __eq__, always override __hash__ for compatibility.
'''

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        if isinstance(other, MyClass):
            return self.a == other.a and self.b == other.b
        return False

    def __hash__(self):
        return hash((self.a, self.b))

# Usage
obj1 = MyClass(1, 2)
obj2 = MyClass(1, 2)
print(obj1 == obj2)  # True
print(hash(obj1) == hash(obj2))  # True
