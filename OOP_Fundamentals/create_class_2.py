class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def say_hi_to_user(self, user):
        print(f"Sending message to {user.username}: Hi {user.username}, it\'s {self.username}")

user1 = User("JongWick", "3473974")
user2 = User("Scooby", "338283")

user1.say_hi_to_user(user2)
user2.say_hi_to_user(user1)