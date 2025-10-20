class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed 
        
    def bark(self):
        print("Whoof whooof")

    def intro(self):
        print(f"{self.name} is a {self.breed}")



black_dog = Dog("Sparky", "Poodle")
black_dog.intro()
black_dog.bark()

white_dog = Dog("Jack", "Shapard")
white_dog.intro()
white_dog.bark()