# # # import math

# # # print(help(math.sin(4)))


# # # def hello(n=3):
# # #     print(n)
    
# # # hello(5)



# # def cube(x):
# #     return x*x*x
# # l=[1,2,3,4,5]
# # new_list=list(map(cube,l))

# # print(new_list)

# my_list = [1, 2]
 
# for v in range(2):
#     print(v)
#     my_list.insert(-1, my_list[v])
 
# print(my_list)

# def function_1(a):
#   return None


# def function_2(a):
#   return function_1(a) * function_1(a)


# # print(function_2(2))

# print(1//2)

# def func(a,b):
#   return b ** a


# print(func(2,2))

# z = 0
# y = 10
# x = y < z and z > y or y < z and z < y

# print(x)

# # for=3
# # print(print)

# my_list =  [x * x for x in range(5)]



# def fun(lst):
#    del lst[lst[2]]
#    return lst


# print(fun(my_list))


# x = 1
# y = 2
# x, y, z = x, x, y #1 1 2
# z, y, z = x, y, z # 1 1 2

# print(x, y, z)

# a = 1
# b = 0
# a = a ^ b 
# print(a)
# b = a ^ b 
# print(b)
# a = a ^ b 
# print(a)

# print(a, b)

# def fun(x):
#   if x % 2 == 0:
#        return 1
#   else:
#       return 2


# print(fun(fun(2)))


# x = int(input())
# y = int(input())
# x = x % y
# x = x % y
# y = y % x
# print(y)

# # print("a", "b", "c", sep="sep")
# # x = 1 // 5 + 1 / 5
# # print(x)

# # x = float(input())
# # y = float(input())
# # print(y ** (1 / x))
# dct = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dct['three']

# for k in range(len(dct)):
#    v = dct[v]

# print(v)

# lst = [i for i in range(-1, -2)]

# print(lst)


# def fun(a, b, c=0):
#  print(a)
 

# # fun(b=1)


# def fun(x, y):
#    if x == y:
#      return x
#    else:
#       return fun(x, y-1)


# print(fun(0, 3))


# i = 0
# while i < i + 2 :
#    i += 1
#    print("*")
# else:
#    print("*")
   
tup = (1, 2, 4, 8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)
dct = {}
dct['1'] = (1, 2)
# dct['2'] = (2, 1)

# for x in dct.keys():
#    print(dct[x][1], end="")

def fun(inp=2, out=3):
   return inp * out


print(fun(out=2))

print(Hello, World!)







dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="")







   









