# name1 = input("Enter your name of person1 : ")
# age1 = int(input("Enter your age : ")) #string 
# name2 = input("Enter your name of person2: ")
# age2 = int(input("Enter your age : ")) #string 
# if age1>age2:
#     print(name1)
# else: 
#     print(name2)
# a = """Lorem ipsum dolor sit amet consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)
# a='hello' single line
# a='hello' 
# print(a[4])
# z = 2
# y = 2
# print(y%z)

# m = int(input("Enter a Digit"))
# print(type(m))
# b = "my name is affan"
# print(b[-1:])

# a = "    hello world!    "
# a.strip()
# print(a)


# name= input('Enter your name : ')
# age= int(input("enter your age : "))

# print(f'Hello {name}! You age is {age} ')  #string interpulation


# age = 36
# name = 'ali'
# print("My name is {}, and I am {}".format(name,age))


# a = "hello world!"
# print(a.find('o'))



# print(2**10)

# print(5//3)

# age = int(input('Enter your age :'))
# if age>=18:
#     inter = input('have you done  intermediate?\n1:yes\n2:no\n')
#     if inter =='yes':
#         print('you are eligible to get admission in university')
#     else:
#         print('Sorry,you are  not eligible to get admission in university')
        
# else:
#     print('Sorry,you are  not eligible to get admission in university')
    
    

# age = int(input("Enter your age = "))
# if age>=18 or age<=26:
#     print('You can join this uni')
# else:
#     print("you cannot join this uni")
# a=0
# b=100
# while(a!=b):
#     print(a+=1)


# # a='hello'
# # for i in range(len(a)): #ending point allways excluded
# #     print(a[i])


# number = int(input('Enter the number : '))
# for x in range(1,101):
#   print(f"{number} x {x} = {number*x}")


# name = input('enter your name :')
# for char in name:
#     print(char)



# year = int(input('enter the year'))
# if year % 4==0:
#    if year %100!=0: 
#       if year % 400 ==0:
#          print("leap year")
# else :
#    print("not leap year")

# import math
# a=[2,4] #x1,y1
# b=[5,7] #x2,y2

# eculiduen = math.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)
# print(eculiduen)

angle1 = int(input("enter : "))
angle2 = int(input("enter : "))
angle3 = int(input("enter : "))

if angle1+angle2+angle3 == 180 & angle1 !=0 or angle2!=0 or angle3 !=0:
    print("triangle")
else:
    print("not a triangle")
