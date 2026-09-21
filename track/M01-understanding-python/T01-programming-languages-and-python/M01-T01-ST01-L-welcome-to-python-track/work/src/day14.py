# 1. Input

# rows = int(input())
# User enters:

# 4
# So:

# rows = 4
# Upper Half

# for i in range(1, rows + 1):
# Since rows = 4:

# range(1, 5)
# So i takes:

# i = 1
# i = 2
# i = 3
# i = 4
# 🔹 First Row: i = 1

# Step 1: Print spaces

# for j in range(rows - i):
# Substitute values:

# range(4 - 1)
# range(3)
# So j becomes:

# j = 0
# j = 1
# j = 2
# Three spaces are printed:

# ___
# where _ represents a space.

# Step 2: Print star/space

# for j in range(2 * i - 1):
# Substitute:

# range(2 * 1 - 1)
# range(1)
# So:

# j = 0
# Condition:

# if j == 0 or j == 2 * i - 2:
# becomes:

# if 0 == 0 or 0 == 0:
# True, so * is printed.

# Result:

#    *
# 🔹 Second Row: i = 2

# Step 1: Spaces

# range(4 - 2)
# range(2)
# j:

# 0, 1
# So 2 spaces:

# __
# Step 2: Star/space

# range(2 * 2 - 1)
# range(3)
# j:

# 0, 1, 2
# Now check each position:

# jConditionPrint

# 0

# j == 0 → True

# *

# 1

# False

# space

# 2

# j == 2 → True

# *

# Result:

#   * *
# 🔹 Third Row: i = 3

# Step 1: Spaces

# range(4 - 3)
# range(1)
# One space:

# _
# Step 2: Star/space

# range(2 * 3 - 1)
# range(5)
# j:

# 0, 1, 2, 3, 4
# jConditionPrint

# 0

# True

# *

# 1

# False

# space

# 2

# False

# space

# 3

# False

# space

# 4

# True

# *

# Result:

#  *   *
# profile photo
# Shakthi
# Instructor
# 10:53 AM
# 🔹 Fourth Row: i = 4

# Step 1: Spaces

# range(4 - 4)
# range(0)
# No spaces.

# Step 2: Star/space

# range(2 * 4 - 1)
# range(7)
# j:

# 0, 1, 2, 3, 4, 5, 6
# jConditionPrint

# 0

# True

# *

# 1

# False

# space

# 2

# False

# space

# 3

# False

# space

# 4

# False

# space

# 5

# False

# space

# 6

# True

# *

# Result:

# *     *
# So the upper half is:

#    *
#   * *
#  *   *
# *     *
# profile photo
# Shakthi
# Instructor
# 10:53 AM
# Lower Half

# Now this loop starts:

# for i in range(rows, 0, -1):
# With rows = 4:

# range(4, 0, -1)
# Therefore:

# i = 4
# i = 3
# i = 2
# i = 1
# It is going backwards.

# 🔹 Fifth Row: i = 4

# Spaces:

# range(4 - 4)
# range(0)
# → No spaces.

# Star loop:

# range(2 * 4 - 1)
# range(7)
# Stars at:

# j = 0
# j = 6
# Spaces between them.

# Result:

# *     *
# 🔹 Sixth Row: i = 3

# Spaces:

# range(4 - 3)
# range(1)
# → 1 space.

# Star loop:

# range(5)
# Stars at:

# j = 0
# j = 4
# Result:

#  *   *
# 🔹 Seventh Row: i = 2

# Spaces:

# range(4 - 2)
# range(2)
# → 2 spaces.

# Star loop:

# range(3)
# Stars at:

# j = 0
# j = 2
# Result:

#   * *
# 🔹 Eighth Row: i = 1

# Spaces:

# range(4 - 1)
# range(3)
# → 3 spaces.

# Star loop:

# range(1)
# Only j = 0.

# Result:

#    *
# Complete Trace

# RowiSpacesStar-loop rangePattern

# 1

# 1

# 3

# range(1)

# *

# 2

# 2

# 2

# range(3)

# * *

# 3

# 3

# 1

# range(5)

# * *

# 4

# 4

# 0

# range(7)

# * *

# 5

# 4

# 0

# range(7)

# * *

# 6

# 3

# 1

# range(5)

# * *

# 7

# 2

# 2

# range(3)

# * *

# 8

# 1

# 3

# range(1)


# # Final Output

# #    *
# #   * *
# #  *   *
# # *     *
# # *     *
# #  *   *
# #   * *
# #    *


# ==============================
# 10 Pattern Programs in Python
# ==============================

# 1. Right Triangle Star Pattern
print("1. Right Triangle Star Pattern")
n = 5
for i in range(1, n+1):
    print("*" * i)
print()

# 2. Inverted Right Triangle
print("2. Inverted Right Triangle")
n = 5
for i in range(n, 0, -1):
    print("*" * i)
print()

# 3. Pyramid Pattern
print("3. Pyramid Pattern")
n = 5
for i in range(1, n+1):
    print(" " * (n - i) + "*" * (2 * i - 1))
print()

# 4. Inverted Pyramid
print("4. Inverted Pyramid")
n = 5
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
print()

# 5. Number Triangle
print("5. Number Triangle")
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
print()

# 6. Continuous Number Pyramid
print("6. Continuous Number Pyramid")
n = 5
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
print()

# 7. Diamond Pattern
print("7. Diamond Pattern")
n = 5
# Upper half
for i in range(1, n+1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# Lower half
for i in range(n-1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
print()

# 8. Hollow Square
print("8. Hollow Square")
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()

# 9. Floyd’s Triangle
print("9. Floyd’s Triangle")
n = 5
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
print()

# 10. Pascal’s Triangle
print("10. Pascal’s Triangle")
n = 5
for i in range(n):
    print(" " * (n - i), end="")
    coef = 1
    for j in range(i + 1):
        print(coef, end=" ")
        coef = coef * (i - j) // (j + 1)
    print()