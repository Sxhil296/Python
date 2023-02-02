class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"HI, I am {self.name}.")


john = Person("Paterick")
john.talk()

bob = Person("Walter")
bob.talk()