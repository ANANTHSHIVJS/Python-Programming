
class hospital():
    def __init__(self,admin,doc,sis,dep,name,age):
        self.admin=admin
        self.doc=doc
        self.sis=sis
        self.dep=dep
        self.name=name
        self.age=age

    def enter(self):
        self.admin1=input("Enter admin name : ")
        self.doc1=input("Enter doctor name : ")
        self.sis1=input("Enter sister name : ")
        self.dep1=input("Enter department name : ")

class department(hospital):
    def show(self):
        print("The admin is :",self.admin1)
        print("The doctor is :", self.doc1)
        print("The sister is :", self.sis1)
        print("The department is :", self.dep1)

class patientward(department):
        def penter(self):
        self.name1=input("Enter the name of Patient : ")
        self.age1 = input("Enter the age of Patient : ")
    def pshow(self):

        print("The patient is :", self.name1)
        print("The patient's age is :", self.age1)

object=patientward('','','','','','')
object.enter()
object.show()
object.penter()
object.pshow()