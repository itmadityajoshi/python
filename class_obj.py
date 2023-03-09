# A class is a blueprint or template of an object 
# A class doesnot hold memory
# A object is an instance of class
# A object is a real world entity
# A object holds memory.
# A object can have one class but class have many objects.


class Form():
    def getform(self):
        print(f"{self.name} {self.contact}")


#object1
bikalForm = Form()
bikalForm.name = "Bikal Shrestha"
bikalForm.contact = 986456465
bikalForm.getform()    #bikalForm.getform(bikalForm.name,bikalForm.contact)


#object2

person2 = Form()
person2.name = "Aditya Joshi"
person2.contact = 9860709627
person2.getform()


#obejct3

person3 = Form()
person3.name = "Vivek Rana"
person3.contact = 9841213908
person3.getform()
