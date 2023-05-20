class Customer:
    def __init__(self, name, create_password, confirm_password, email):
        self.name = name
        self.email = email
        self.create_password = create_password
        self.confirm_password = confirm_password

    def sign_up(self, name, create_password, confirm_password, email):
        if (
            self.name == name
            and self.create_password == create_password
            and self.confirm_password == confirm_password
            and self.email == email
        ):
            return "You have successfully signed up"
        else:
            return "Password and Confirm Password do not match"


new_customer = Customer(
    "Emily Haile", "passwordI22j78", "passwordI22j78", "haileemily@gmail.com"
)

result = new_customer.sign_up(
    "Emily Haile", "passwordI22j78", "passwordI22j78", "haileemily@gmail.com"
)

print(result)

class Signin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def signin(self):
        if self.username == self.username and self.password == self.password:
            return "Successful"
        else:
            return "Invalid username or password"


user = Signin("cynthia", "ocean@eyes")
result = user.signin()
print(result)