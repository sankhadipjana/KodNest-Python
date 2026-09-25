#swap 2 Number without third variable
a = 20
b = 30
a,b = b,a
print(a,b)

# #first 10 prime number\

count = 0
num = 2
while count < 10:
    if all(num % i != 0 for i in range(2, num)):
        print(num, end=" ")
        count += 1
    num += 1
print()
#find some of the first 10 even number

n=10
s =0
while (n>0) :
    if(n%2 ==0):
        s= s+n
    n-=1
print(s)  


#factorial

fact = 5
fin = 1

for i in range(1,fact+1):
    fin =fin * i
print(fin)


# revarce anumber

numb= 12345
rev=0
while numb > 0:
    last = numb%10
    rev = rev*10+last
    numb = numb//10
print(rev)


#palindrom

num= 12321
rev=0
while num > 0:
    last = num%10
    rev = rev*10+last
    num = num//10

if num == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")

#sum of all degit until a single degit

deg = 12345
while deg > 9:
    sum = 0
    while deg > 0:
        sum += deg % 10
        deg //= 10
    deg = sum
print(deg)  




num = int(input("Enter a number: "))

while num >= 10:
    total = 0
    while num > 0:
        digit = num % 10

        total += digit

        num //= 10



    num = total



print(num)






 
