# OOPS ==> object oriented programming SystemError
#  Inheritance => It is an oops concept where child class can be derived from the parent class.
# Inheritance Types
# 1. single
# 2. Multiple
# 3. Multilevel

class school():
    schoolName = "Dursikshya"
    Course = "web Development"
    def reveiw(self):
        print("It is a nice school")

class Ten(school):
    def reveiw(self):
        print('It is a bad school')
    def details(self):
        print('yayy we are class 10 and we are graduating')


obj = Ten()
print(obj.schoolName)
obj.reveiw()  # firstly the reveiw is coming from class ten which is overriding the reveiw of class school
obj.details()


#  Polymorphism 
#  Encapsulation
#  Abstractions
