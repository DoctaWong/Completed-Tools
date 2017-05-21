import random

class Person(object):
    def __init__(self, name, age, major=None):
        self.name = name
        self.age = age
        self.friends = []
        self.major = major
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_friends(self):
        return self.friends
    def get_major(self):
        return self.major
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def remove_friend (self, fname):
        try:
            self.friends.remove(fname)
        except:
            raise(ValueError(str(fname) + " not found"))
    def change_major(self, major):
        self.major = major
    def __str__(self):
        return str(self.name) + ": " + str(self.age) + " years old. Friends: " + str(self.friends) + ". " + str(self.major)
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("Need sleep!!!")
        elif r < 0.5:
            print("So hungry.  Must eat!!!")
        elif r < 0.75:
            print("Europa!")
        else:
            print("Busy, homework")
            
mike = Person("Michael", 55)
mike.add_friend("Wilson")

print mike

chris = Person("Chris", 24)
chris.change_major("Political Science")
chris.add_friend("Wade")
chris.add_friend("Wilson")
chris.add_friend("Corbin")

print chris

chris.remove_friend("Corbin")

print chris.get_friends()
print chris
'''
chris.remove_friend("Corbin")
'''

chris.change_major("Computer Science")

print chris.get_major()
print chris
print chris.speak()
