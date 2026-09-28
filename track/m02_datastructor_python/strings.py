strin = "slndskh\'namae\' \"jgfctfr\"  " # this print the output as it is given in the string 
print(strin)

# Inbuilt String Methods – Single Program
s = "  kodNest Technologies 123  "


print("Original String:", s) 


# Case conversion methods
print("upper():", s.upper()) # 
print("lower():", s.lower()) #   
print("capitalize():", s.capitalize()) #  
print("title():", s.title()) #  
print("swapcase():", s.swapcase()) #


# Searching & counting
print("find('Tech'):", s.find("Tech")) #  use to find the index of the substring
print("count('o'):", s.count("o")) #used to count the number of occurrences of a substring in a string


# Replace
print("replace('123', '2025'):", s.replace("123", "2025"))
#  


# Start & End check
print("startswith('  kod'):", s.startswith("  kod")) #
print("endswith('123  '):", s.endswith("123  ")) #


# Split & Join
words = s.split() #
print("split():", words)
print("join():", "-".join(words)) #  


# Strip spaces
print("strip():", s.strip()) #
print("lstrip():", s.lstrip())# 
print("rstrip():", s.rstrip())#  


# Checking methods
print("isalpha():", s.isalpha())#
print("isdigit():", s.isdigit())#
print("isalnum():", s.isalnum())#


# Length
print("Length of string:", len(s)) #