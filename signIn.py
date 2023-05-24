class Signin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def sign_in(self):
        if self.username == email and self.password == create_password:
            return "Successful"
        else:
            return "Invalid username or password"

username = input("Enter your username (email): ")
password = input("Enter your password: ")

user = Signin(username, password)
result = user.sign_in()
print(result)
