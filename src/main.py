import time
import datetime as dt

class Account:
    
    def __init__(self):
        self.username = None
        self.password = None
        self.confirm_password = None
        
    def get_data(self): 
        username = input("Enter Username :")
        password = input("Enter Password:")
        return username , password
       
    def create(self):
        print("== Creating Account ==")
        self.username , self.password =  self.get_data()
        self.confirm_password = input("Confirm Password: ")

        if self.username.strip() == "" or self.password.strip() == "":
            print("You must enter valid info")
        else:
            if self.password == self.confirm_password:
                print(f"The account has been created successfully!! Your user is: {self.username}")
                time.sleep(1)
            else:
                print("Password does not match")

    def login(self):
        print("== Login Account ==")
        if self.username is None or self.password is None:
            print("Your account is not found")
            time.sleep(1)
        else:  
          attempts = 4
          while attempts > 0: 
            username_login, password_login = self.get_data()
            if username_login == self.username and password_login == self.password:
                current_time = dt.datetime.now().strftime("%d-%m-%Y %I:%M %p")
                print(f"Welcome back {self.username}!\nLogin successful at {current_time}")
                time.sleep(2)
                break
            else:
                attempts -=1
                print(f"Incorrect username or password. attempts left : {attempts}")
          else:
              print("You have exceeded the allowed attempts.\nReturning to main menu...")
              time.sleep(1)       

    def delete(self):
        confirm = input("Are you sure you want to delete your account? (yes/no): ").strip().lower()
        if confirm.strip() == "yes":
            self.username = None
            self.password = None
            print("Account deleted successfully")
            time.sleep(1)
        else:
            print("Account deletion canceled")
            
            
    def reset_passowrd(self):
        print("Reset Password....")
        attempts = 4
        while attempts > 0: 
           username, password = self.get_data()
           if username == self.username and password == self.password:
              self.password = input("Enter new password :")
              print("Password changed successfully")
              time.sleep(1)
              break
           else:
            attempts -= 1
            print(f"Incorrect username or password. Attempts left: {attempts}")
        else:
          print("You have exceeded the allowed attempts.\nReturning to main menu..")
    
    def forget(self):
        print("Forget password")
        attmpts = 4
        while attmpts >0:
            username = input("Enter your username to return your account :")
            if username == self.username:
                self.password = input("New password :")
                self.confirm_password = input("Confirm password :")
                if self.password == self.confirm_password:
                    print("password changed successfully...")
                    time.sleep(1)
                    break
                else:
                    attmpts -=1
                    print(f"Password and confirm password do not match.. Attmpts left : {attmpts}")
            else:
                attmpts -=1
                print(f"couldn’t find username. try again! attmpts left : {attmpts}")
                time.sleep(1)
        else:
            print("You have exceeded the allowed attempts.\nReturning to main menu..")                    
                    
                
                    
            
                



def main():
    print("=== Welcome to Account Manager! ===")
    user = Account()

    while True:
        print("\n1. Create Account")
        print("2. Login Account")
        print("3. Delete Account")
        print("4. Reset password")
        print("5.Forget password")
        print("6.Exit")
        user_choice = input("Enter the number: ")

        if user_choice == "1":
            user.create()
        elif user_choice == "2":
            user.login()
        elif user_choice == "3":
            user.delete()
        elif user_choice == "4":
            user.reset_passowrd()
        elif user_choice == "5":
           user.forget()  
        elif user_choice == "6":
            print("Thank you for being with us.\nall the best!")
            break    
        else:
            print("Invalid option. Try again")


if __name__ == "__main__":
    main()
