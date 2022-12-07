class Dog:
    kind = "cerene"
    def __init__(self , name):
        self.name= name
        print(self.name)

d = Dog("fido")
e = Dog.kind
print(d)
print(e)
