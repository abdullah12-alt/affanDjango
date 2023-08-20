class Person:
   def __init__(self):
       self.name=''
   def set(self,name):
      self.name=name
   def get(self):
      return f'name is {self.name}'

p1=Person()
p1.set('ali')
print(p1.get())

      
    
       