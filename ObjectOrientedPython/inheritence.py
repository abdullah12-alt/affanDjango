# class Parent:
#     def __init__(self,fname,lname):
#         self.fistName=fname
#         self.LastName=lname
#     def Display(self):
#         print(f'First name is : {self.fistName}\nLast Name is : {self.LastName}')
        
# class Child(Parent):
#     def __init__(self, fname, lname,hairColor):
#         super().__init__(fname, lname)
#         self.hairColor=hairColor
        
    
#     def Display(self):
#         print(super().Display())
#         print('child hairs color is : ',self.hairColor)

# c1=Child('Jhone','Khan','Brown')

# c1.Display()



class Vehical:
    def __init__(self):
        print('i am vehical')
        

class Car:
    def __init__(self,color,model):
        super().__init__()
        self.model=model
        self.color=color
    def display(self):
         print(f'{self.model}\n{self.color}')
         
class bike(Car,Vehical):
    def __init__(self, color, model,wheels):
        super().__init__(color, model)
        self.wheels= wheels
        
    def display(self):
        print(super().display())
        print(self.wheels)
        


        
    
    
        