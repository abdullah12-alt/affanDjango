class overload:
    def __init__(self):
        print("this class is for overloading")
    def display(self):
        print('line 2')

    def display(self,name):
        self.name=name
        print('line 1 ',name)
class overload2(overload):
    def __init__(self):
        print("this class is for overloading2")
    def display(self,name):
        self.name=name
        print('line 1 ',name)
o1=overload()
o1.display('affan')
# o1.display()


def area(l, b):
  c = l*b
  return c
def area(size):
  c = size*size
  return c
print(area(4))
area(5,6)
