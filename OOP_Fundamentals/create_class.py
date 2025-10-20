class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner 
        
    def bark(self):
        print("Whoof whooof")

    def intro(self):
        print(f"{self.name} is a {self.breed}")

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number


black_dog_owner = Owner("Mike", "Easy Str", "2-33-23")
black_dog = Dog("Sparky", "Poodle", black_dog_owner)
black_dog.intro()
black_dog.bark()
print('Black Dog\'s owner is ', black_dog.owner.name)

white_dog_owner = Owner("Miley", "Green Str", "3-09-89")
white_dog = Dog("Jack", "Shapard", white_dog_owner)
white_dog.intro()
white_dog.bark()
print('White Dog\'s owner is ', white_dog.owner.name)
