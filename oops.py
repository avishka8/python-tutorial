class Student:
    college="University"

    #staticmethod
    @staticmethod
    def hello():
        print("hello")

    #default constructor
    def __init__(self):
        pass

    #parameterized constructor
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def average(self):
        sum=0
        for a in self.marks:
            sum += a
        print("average marks", sum/3)    
                

    def welcome(self):
        print("welcome student")

s1=Student("arjun",[98,88,90])
print(s1.name, s1.marks)
print(Student.college)
s1.welcome()
s1.average()

s2=Student("ankoor", [100,99,93])
print(s2.name, s2.marks)
print(Student.college)
s2.welcome()
s2.average()


#attributes: appearance like color,type 1. Class.attr 2. obj.attr 
# preference: obj attr > class attr
#methods: functioning








#class Car:
#    color="Red"
#    brand="mercedes"

#car1=Car()
#print(car1.color)   
#print(car1.brand) 
