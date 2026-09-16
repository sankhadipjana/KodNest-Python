# 1. Positive number
n = int(input("Enter number: "))
if n > 0: print("Positive")

# 2. Blood donation eligibility
age = int(input("Enter age: "))
if age >= 18: print("Eligible to donate blood")

# 3. Hot day
temp = float(input("Enter temperature: "))
if temp > 30: print("Hot Day")

# 4. Attendance
attendance = float(input("Enter attendance %: "))
if attendance >= 75: print("Eligible")

# 5. Even or odd
n = int(input("Enter number: "))
if n % 2 == 0: print("Even")
else: print("Odd")

# 6. Driving license
age = int(input("Enter age: "))
if age >= 18: print("Eligible")
else: print("Not Eligible")

# 7. Leap year
year = int(input("Enter year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0): print("Leap Year")
else: print("Not Leap Year")

# 8. Greater number
a, b = map(int, input("Enter two numbers: ").split())
if a > b: print(a)
else: print(b)

# 9. Grade
m = int(input("Enter marks: "))
if 90 <= m <= 100: print("Grade A")
elif 80 <= m < 90: print("Grade B")
elif 70 <= m < 80: print("Grade C")
elif 60 <= m < 70: print("Grade D")
else: print("Fail")

# 10. Electricity usage
u = int(input("Enter units: "))
if u > 500: print("High")
elif u >= 301: print("Medium")
elif u >= 101: print("Low")
else: print("Very Low")

# 11. BMI
bmi = float(input("Enter BMI: "))
if bmi < 18.5: print("Underweight")
elif bmi < 25: print("Normal")
elif bmi < 30: print("Overweight")
else: print("Obese")

# 12. Ticket category
age = int(input("Enter age: "))
if age < 5: print("Free")
elif age <= 12: print("Child Ticket")
elif age <= 59: print("Adult Ticket")
else: print("Senior Citizen Ticket")



#PART 2 — NESTED IF, MATCH-CASE, FOR LOOP




# 13. Scholarship
marks = int(input("Marks: "))
income = int(input("Income: "))
if marks >= 85:
    if income < 300000: print("Eligible")
    else: print("Not Eligible")
else: print("Not Eligible")

# 14. Login
user = input("Username: ")
pwd = input("Password: ")
if user == "admin":
    if pwd == "1234": print("Login Successful")
    else: print("Wrong Password")
else: print("Wrong Username")

# 15. Club entry
age = int(input("Age: "))
id_valid = input("Valid ID (yes/no): ")
if age >= 21:
    if id_valid == "yes": print("Entry Allowed")
    else: print("Valid ID Required")
else: print("Not Allowed")

# 16. Employee bonus
exp = int(input("Experience: "))
rating = input("Rating: ")
if exp >= 5:
    if rating.lower() == "excellent": print("Bonus Eligible")
    else: print("No Bonus")
else: print("No Bonus")

# 17. Weekday
n = int(input("Day (1-7): "))
match n:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")
    case _: print("Invalid")

# 18. Month
n = int(input("Month (1-12): "))
months = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"]
if 1 <= n <= 12: print(months[n-1])
else: print("Invalid")

# 19. Season
m = int(input("Month: "))
if m in (12,1,2): print("Winter")
elif m in (3,4,5): print("Summer")
elif m in (6,7,8,9): print("Rainy")
elif m in (10,11): print("Autumn")
else: print("Invalid")

# 20. Traffic signal
signal = input("Signal: ").lower()
match signal:
    case "red": print("Stop")
    case "yellow": print("Wait")
    case "green": print("Go")
    case _: print("Invalid")

# 21. 1 to 20
for i in range(1, 21): print(i)

# 22. Multiplication table
n = int(input("Number: "))
for i in range(1, 11): print(n, "x", i, "=", n*i)

# 23. Odd numbers 1-50
for i in range(1, 51):
    if i % 2 != 0: print(i)

# 24. Squares 1-10
for i in range(1, 11): print(i*i)

# 25. Sum 1-100
total = 0
for i in range(1, 101): total += i
print(total)



#whilwe break continue 

# 26. 10 to 1
i = 10
while i >= 1:
    print(i); i -= 1

# 27. Factorial
n = int(input("Number: "))
fact = 1
while n > 0:
    fact *= n; n -= 1
print(fact)

# 28. Reverse number
n = int(input("Number: "))
rev = 0
while n:
    rev = rev*10 + n%10
    n //= 10
print(rev)

# 29. Count digits
n = abs(int(input("Number: ")))
count = 1 if n == 0 else 0
while n:
    count += 1; n //= 10
print(count)

# 30. Sum of digits
n = abs(int(input("Number: ")))
total = 0
while n:
    total += n % 10; n //= 10
print(total)

# 31. Stop at 15
for i in range(1, 21):
    if i == 16: break
    print(i)

# 32. Search using break
nums = [10,20,30,40,50]
target = int(input("Search: "))
for n in nums:
    if n == target:
        print("Found"); break
else: print("Not Found")

# 33. Input until 0
while True:
    n = int(input("Enter number: "))
    if n == 0: break
    print(n)

# 34. Skip multiples of 3
for i in range(1, 21):
    if i % 3 == 0: continue
    print(i)

# 35. Odd numbers
for i in range(1, 51):
    if i % 2 == 0: continue
    print(i)

# 36. Characters except vowels
text = input("Enter string: ")
for ch in text:
    if ch.lower() in "aeiou": continue
    print(ch)



#function 
# 
# 
# # 37. Cube
def cube(n): return n ** 3
print(cube(int(input("Number: "))))

# 38. Maximum of two
def maximum(a, b): return a if a > b else b
a, b = map(int, input("Two numbers: ").split())
print(maximum(a, b))

# 39. Rectangle area
def area(l, w): return l * w
l, w = map(float, input("Length Width: ").split())
print(area(l, w))

# 40. Prime number
def prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
n = int(input("Number: "))
print("Prime" if prime(n) else "Not Prime")

# 41. Simple Interest
def simple_interest(p, r, t):
    return (p*r*t)/100
p,r,t = map(float, input("P R T: ").split())
print(simple_interest(p,r,t))

# 42. Empty function
def display():
    pass

# 43. Empty class
class Student:
    pass

# 44. For loop using pass
for i in range(5):
    pass

# 45. If using pass
n = int(input("Number: "))
if n > 0:
    pass
else:
    print("Not positive")    