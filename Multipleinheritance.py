class Father():
    location = "Pokhara"
    def fname(self):
        print("satya Joshi")

class Mother():
    location = "Kathmadnu"
    def mname(self):
        print("Tilya Joshi")

class Child(Father, Mother):
    def cname(self):
        print("Aditya Joshi") 


obj = Child()
obj.fname()
obj.mname()
obj.cname()
print(obj.location)

