class Account:
    
    def __init__(self, username, password, confirm_password):
        self.username = username
        self.password = password
        self.confirm_password = confirm_password
        
    def create(self):
        print("== Creating Account ==")
        self.username = input("Enter Username: ")
        self.password = input("Enter Password: ")
        self.confirm_password = input("Confirm Password: ")

        if self.username.strip() == "" or self.password.strip() == "":
            print("You must enter valid info")
        else:
            if self.password == self.confirm_password:
                print(f"The account has been created successfully!! Your user is: {self.username}")
            else:
                print("Password does not match")

    def login(self):
        print("== Login Account ==")
        if self.username is None or self.password is None:
            print("Your account is not found")
        else:
            username_login = input("Enter Username: ")
            password_login = input("Enter Password: ")
            if username_login == self.username and password_login == self.password:
                print(f"Login successfully! \nWelcome back {self.username}!")
            else:
                print("Incorrect username or password")

    def delete(self):
        confirm = input("Are you sure you want to delete your account? (yes/no): ").lower()
        if confirm.strip() == "yes":
            self.username = None
            self.password = None
            print("Account deleted successfully")
        else:
            print("Account deletion canceled")




def main():
    print("=== Welcome to Account Manager! ===")
    user = Account(None, None, None)

    while True:
        print("\n1. Create Account")
        print("2. Login Account")
        print("3. Delete Account")
        print("4. Exit")
        chose = input("Enter the number: ")

        if chose == "1":
            user.create()
        elif chose == "2":
            user.login()
        elif chose == "3":
            user.delete()
        elif chose == "4":
            print("Exiting the app, goodbye!")
            break
        else:
            print("Invalid option. Try again")


if __name__ == "__main__":
    main()
