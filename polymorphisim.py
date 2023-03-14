#Polymerphism = it is an oops concept where poly means many and merphism forms so all togehter it is called many forms
class Bird():
    def intro (self):
        print("we are birds category")
    def fly(self):
        print("Birdss can fly as weill as cannot fly")

class Pegion(Bird):
    def name(self):
        print("I am pegion from Bird Class")
    def fly(self):
        print("I can fly") 

class Penguin(Bird):
    def name(Self):
        print("I am Penguin")
    def fly(self):
        print("I can not fly")



Bird1 = Bird()
Bird1.intro()
Bird1.fly()

Pegion1 = Pegion()
Pegion1.intro()
Pegion1.name()
Pegion1.fly()

Penguin1 = Penguin()
Penguin1.name()
Penguin1.fly()