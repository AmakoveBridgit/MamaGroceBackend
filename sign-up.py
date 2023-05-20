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

new_customer = Customer("Emily Haile", "passwordocean@yes", "passwordocean@yes", "haileemily@gmail.com")
result = new_customer.sign_up()
print(result)

class Signin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def sign_in(self):
        if self.username == "ehaile" and self.password == "ocean@eyes":
            return "Successful"
        else:
            return "Invalid username or password"

user = Signin("ehaile", "ocean@eyes")
result = user.sign_in()
print(result)