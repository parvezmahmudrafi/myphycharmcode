class Mammal:
    def walk(self):
        print("Walk")

class dog(Mammal):
    def bark(self):
        print("bark")


class cat(Mammal):
    def Cutest(self):
        print("They are cutest")

dog1 = dog()
dog1.bark()

cats = cat()
cats.Cutest()