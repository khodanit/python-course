class Person(object):
    def __init__(self, name, age):
        self.fname, self.sname = name.split(" ")
        self.age = age

    def get_name(self):
        return self.fname + " " + self.sname

    def set_name(self, name):
        self.fname, self.sname = name.split(" ")

    name = property(get_name, set_name)

    def talk(self):
        return "My name is %s" % self.name

    def walk(self):
        if self.age < 1:
            return "crawl"
        elif self.age > 75:
            return "hobble"
        else:
            return "walk"


fred = Person(name="Fred James", age=0.9)
harry = Person("Harry Fields", 90)
sally = Person("Sally Anderson", 20)

for p in (fred, harry, sally):
    print(p.talk(), p.walk())
