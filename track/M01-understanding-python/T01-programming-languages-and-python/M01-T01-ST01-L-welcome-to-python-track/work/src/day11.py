# number = int(input())

# if number%2 == 0:
#     print("even")
# else:
#     print("odd")





# a = 20
# b = 50
# c = 49

# if a>b and a>c:
#     large = a
#     print("a is grater")

# elif b>a and b>c:
#     large = b
#     print("b is grater")
# else:
#     large = c
#     print("c is grater")
    
# print(large)

# res = a if a>b and a>c else (b if b>a and b>c else c)

# print(res)
    

# def addnum():
#     a,b = 20,34
#     c= a+b
#     print(c)

# addnum()


# Square of a number and 
def squar():
    num = 30
    squar = num *num
    print(squar)
squar()

# largest of 3 number
def largest():
    a=30
    b=3
    c=2
    res = a if a>b and a>c else (b if b>a and b>c else c)
    print("largest number is:",res)
largest()

#goodmornig with my name
#no argument no return
def message():
    name="sankha"
    print("goodmornig",name)
message()
#argument, no return
def sum1(a,b):
    print(a+b) 
sum1(1,2)  
#no argument, return value
def sum2( ):
    a = 2
    b =3
    return a+b
print(sum2())    
#argument, return value
def sum(a,b):
    return a+b 
print( sum(1,2))    





