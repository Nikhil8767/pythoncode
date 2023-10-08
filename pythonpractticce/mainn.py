print("hello world")
name="nikhil gupta"
print(name)
id=1234
#print(name+ id)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print("lets use for loop for name")
for character in name:
    print(character)


fruit="mango"
len1=len(fruit)
print("mango is a ",len1,"letter fruit")
print(fruit[0:4])
print(fruit[:4])
print(fruit[:])
print(fruit[-3])
print(fruit[-1:-2])


a="!!!!Nikhil!!!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Nikhil","coder"))
print(a.split())
blogheadinf="introdUVVction to js"
print(blogheadinf.capitalize())
str1="welcome to console!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Nikhil"))
print(str1.find("to"))
b=int(input("enter your age: "))
print("your age is ",b)
if(b>18):
    print("you are adult and you can vote")
else:
    print("you can not vote")