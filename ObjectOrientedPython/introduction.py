# class Human:
#     eyes=2
#     def __init__(self,color,name):
#         self.color =color
#         self.name= name
#     # def __del__(self):
#     #     print("destroyed")
#     @staticmethod
#     def legs():
#         print("all humans have two legs")
#     # attributes
#     def walk(self,name):
#         print(f"{self.name} is walking")
    
#     def __add__(self,other):
#         return self.name + other
        
#     def __str__(self):
#         print(f'this is an object thats name is {self.name} and it is belong from human class')
        

# # instance  --> object
# ali= Human('brown','ali')
# affan=Human('light brown','affan')

# # print(ali)
# print(ali,'hello')
# print(f'my name is {ali.name}\ncolor is {ali.color}')
# print(f'my name is {affan.name}\ncolor is {affan.color}')

print(dir(str))



# print(isinstance(ali,(int,str,float)))