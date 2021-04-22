s = "Hello World"
ret = s.upper()
print(ret) # HELLO WORLD

ret = s.lower()
print(ret) # hello world

b1 = s.startswith("World")
print(b1) # False

b2 = s.endswith("World")
print(b2) # True

s2 = "123yuan"
b3 = s2.isdigit()
print(b3) # False
b4 = s2.isalpha()
print(b4)
b5 = s2.isalnum()
print(b5) # True

s3 = "  yuan   is  a teacher! "
ret = s3.strip()
print(ret)

s4 = "yuan|alvin|eric"
ret = s4.split("|") #
print(ret) # ['yuan', 'alvin', 'eric']

s5 = ['yuan', 'alvin', 'eric',"alex"]
ret ="|".join(s5)
print(ret) # "yuan,alvin,eric,alex89

s6 = "Hello World"
ret = s6.find("World")
print(ret) # 6

s6.count("l") # 3
print(len(s6)) # 11