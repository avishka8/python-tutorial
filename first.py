#LECTURE1 - Variables and Data Types
print("hello world")
name="Khushu"
a=1+2
print(a)
print("My name is Avishka Srivastava", "My age is 20.")
b=9
c=23.2
total=a*b*c
print(total)
a=10
total=a*b*c
age=20
old=False
x=None
print(total)
print(type(a))
print(type(total))
print(type(name))
print(type(x))
print(type(old))
print(type(age)) 
y=2
z=4
sum=y+z
print(sum)

#operators 
#arithmetic(+,-,*,/)
p=5
q=2
print(p+q)
print(p-q)
print(p*q)
print(p/q)
print(p%q) #remainder
print(p**q) #exponent

#relational(==,>,<,!=)
print(p==q)
print(p!=q)
print(p>q)
print(p<q)
print(p<=q)
print(p>=q)

#assignment operator
num=10
num+=2
num-=2

#logical operators
print(not False) #gives opposite value, here it will print true.
#AND operator gives true only if all conditions are true and same for other cases.
#OR operator gives true if any condition is valid.a

#type conversion
a= 2
b= 4.25

#type casting
a=int("2")
b=4.25
print(a+b)

#input
name=input("enter your name ")
print("welcome", name)
age=int(input("enter your age "))
print("you are ", age, " years old.")