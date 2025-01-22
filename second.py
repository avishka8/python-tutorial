str1="this is a string.\nwe are creating it in python"
print(str1)

#concatenation
str2="hello "
str3="world"
print(str2+str3)

#length
print(len(str1), len(str2), len(str3), len(str2+str3))

#indexing
print(str1[0])
print(str1[4])
print(str1[19])
print(str1[45])

#slicing
print(str1[0:4], str1[:4])
print(str1[5:])
#negative slicing
print(str1[-5:-1])
print(str1[-10:])

#strfunctions
print(str1.endswith("on"))
print(str2.endswith("abs"))
print(str3.capitalize())
print(str1.replace("t","x"))
print(str1.find("is"))
print(str1.find("q"))
print(str1.count("t"))

#conditional statements
age=int(input("enter age"))
if(age>18):
    print("eligible for driving license")
elif(age==18):
    print("can get learner's license")    
else:
    print("not eligible")

#odd-even check
num=int(input("enter number "))
if num%2==0:
    print("Number is even") 
else:
    print("Number is odd")       

#q2
a=4
b=6
c=2
if (a>b and a>c):
    print(a,"is greatest")
elif (b>c and b>a):
    print(b,"is greatest")
else:
    print(c,"is greatest")

