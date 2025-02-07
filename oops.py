class Student:
    college="University"

    #default constructor
    def __init__(self):
        pass


    #parameterized constructor
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def welcome(self):
        print("welcome student")

s1=Student("arjun",98)
print(s1.name, s1.marks)
print(Student.college)

s2=Student("ankoor", 100)
print(s2.name, s2.marks)

print(Student.college)
s1.welcome()
s2.welcome()

#attributes: appearance like color,type 1. Class.attr 2. obj.attr 
# preference: obj attr > class attr
#methods: functioning








#class Car:
#    color="Red"
#    brand="mercedes"

#car1=Car()
#print(car1.color)   
#print(car1.brand) 
