class person:
    age=20
    name="student"
    def __init__(self):
        print(self.name,self.age)
a=person()
print(a.name,a.age)
a.display()