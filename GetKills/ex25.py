class Animal(object):
    def run(self):
        print('Animal class')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

def run_twice(animal):
    animal.run()
    animal.run() 
a = Dog()

run_twice(a)
