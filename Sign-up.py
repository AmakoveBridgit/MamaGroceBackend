class Customer:
    def __init__(self, name, create_password, confirm_password, email):
        self.name = name
        self.email = email
        self.create_password = create_password
        self.confirm_password = confirm_password

    def sign_up(self):
        if self.create_password == self.confirm_password:
            signup = {
                "name": self.name,
                "email": self.email,
                "password": self.confirm_password,
            }
            return signup
        else:
            return "Password and Confirm Password do not match"

name = input("Enter your name: ")
email = input("Enter your email: ")
create_password = input("Enter your password: ")
confirm_password = input("Confirm your password: ")

new_customer = Customer(name, create_password, confirm_password, email)
result = new_customer.sign_up()
print(result)

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
