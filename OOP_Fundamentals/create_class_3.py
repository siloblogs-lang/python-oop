class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        print("email accessed")
        return self._email
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email


    
user1 = User("Boddy", "bod@dy.co", "lsdkj")
print(user1.email)

user1.email = "kjffff"
print(user1.email)

user1.email = "kjh@kjjjj"
print(user1.email)
