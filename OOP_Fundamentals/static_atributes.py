# static attribute

class User:
    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1

    def display_user(self): 
        print(f"username: {self.username}, email: {self.email}")

user1 = User("Bob", "bob@b.com")
print(user1.user_count)

user2 = User("Babs", "babs@b.com")
print(user2.user_count)

print("From 1 ", user1.user_count)

user3 = User("Ben", "ben@b.com")
print(user3.user_count)
print("From 1", user1.user_count)
print("From 2", user2.user_count)

print("Total users :", User.user_count )