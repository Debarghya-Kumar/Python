'''class MyClass:    
    def _init_(self,value):
        self.value=value
        
    def print_value(self):
        print(self.value)    
obj1=MyClass(10)
obj1.print_value()'''
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass with value: {self.value}"

    def __add__(self, other):
        return MyClass(self.value + other.value)

obj1 = MyClass(10)
obj2 = MyClass(20)
result = obj1 + obj2  # This invokes the __add__ method
print(result)  



