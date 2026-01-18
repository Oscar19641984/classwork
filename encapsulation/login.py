class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, valid_users):
        if (self.username, self.password) in valid_users:
            return True
        else:
            return False

def main():
    valid_users = [
        ('0164', 'password'),
        ('oscar', 'betterpassword'),
        ('noonan', 'password123')
    ]

    username = input("Enter username: ")
    password = input("Enter password: ")

    login = Login(username, password)

    if login.authenticate(valid_users):
        print("Login successful!")
    else:
        print("Invalid username or password.")

main()