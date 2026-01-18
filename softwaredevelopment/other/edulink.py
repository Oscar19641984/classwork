#classes
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validate(self, user_list):
        for user in user_list:
            if self.username == user['username'] and self.password == user['password']:
                return True
        return False

    def change_password(self, new_password):
        self.password = new_password
        print(f"Password for {self.username} has been changed.")

# Sample user data
users = [
    {'username': 'user1', 'password': 'pass1'},
    {'username': 'user2', 'password': 'pass2'},
]

# Example usage
def main():
    username = input("Enter username: ")
    password = input("Enter password: ")

    user = User(username, password)

    if user.validate(users):
        print("Login successful!")
        change = input("Do you want to change your password? (yes/no): ")
        if change.lower() == 'yes':
            new_password = input("Enter new password: ")
            user.change_password(new_password)
        else:
            function = input("What do you want to access, timetable, grades, homework: ")
            if function.lower() == 'timetable':
                print("P1, computer science : C72\nP2, computer science : C72")
    else:
        print("Invalid username or password.")

main()