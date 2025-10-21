class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self._email = email

    def clean_email(self):
        return self._email.lower().strip()
    
    def get_email(self):
        return self._email
    
    def set_email(self, new_email):
        self._email = new_email.lower().strip()


    def say_hi_to_user(self, user):
        print(f"Sending message to {user.username}: Hi {user.username}, it\'s {self.username}")

user1 = User("JongWick", "3473974", "  SkDdh@de.co")
user2 = User("Scooby", "338283", "  TyeDamms@de.co")
user3 = User("Boddy", "73737", "  SkDdh@de.co")

user1.say_hi_to_user(user2)
user2.say_hi_to_user(user1)

print(user3.clean_email())