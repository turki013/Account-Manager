import json 
import time
import datetime as dt

class Account:
    
    def __init__(self):
        """Initialize account with empty username and password"""
        
        self.username = None
        self.password = None
        self.confirm_password = None
        
        
    def load_data (self):
        """Load user data from the accounts.json file"""
        
        with open("src/accounts.json" , 'r') as file:
            return json.load(file)
        
    def save_data(self, data):
        """Save user data to the accounts.json file"""
        
        with open("src/accounts.json" , 'w') as file:
            json.dump(data , file , indent=4)  
                  
    def get_data(self): 
        """Ask user to input username and password"""
        
        username = input("Enter Username :")
        password = input("Enter Password:")
        return username , password
       
    def create(self):
        """Create a new account and save it"""
        data = self.load_data()
        print("== Creating Account ==")
        
        self.username , self.password =  self.get_data()
        if self.username.strip() == "" or self.password.strip() == "":
            print("You must enter valid info")
                
        if self.username in data:
            print("Username was teken try another one")
            return
        self.confirm_password = input("Confirm Password: ")
        
        if self.password != self.confirm_password:
            print("Password does not match")
            return self.confirm_password()
            
        data[self.username] = {'password' : self.password}
        self.save_data(data)
        print("Thank you for registering. Your account has been successfully created. You may now log in and access your dashboard.")
        time.sleep(1)
  
    def login(self):
        """Login to an existing account"""
        data = self.load_data()
        print("== Login Account ==")
        
        attempts = 4
        while attempts > 0: 
            username_login, password_login = self.get_data()
            if username_login in data and data[username_login]['password'] == password_login:
              self.username = username_login
              self.password = password_login
              current_time = dt.datetime.now().strftime("%d-%m-%Y %I:%M %p")
              print(f"Welcome back {username_login}!\nLogin successful at {current_time}")
              time.sleep(2)
              break
            else:
               attempts -= 1
               print(f"Incorrect username or password. Attempts left: {attempts}")
        else:
         print("You have exceeded  the allowed attempts.\nReturning to main menu...")
         time.sleep(1)       

    def delete(self):
        """Delete the currently logged in user's account"""
        data = self.load_data()
        if not self.username:
            print("No user is currently logged in..")
             
        else:
         confirm = input("Are you sure you want to delete your account? (yes/no): ").strip().lower()
         if confirm == "yes":
            if self.username in data:
               del data[self.username]
               self.save_data(data)
               print("Account deleted successfully")
               time.sleep(1)
               self.username = None
               self.password = None
            else:
               print("Account not found.")
         else:
          print("Account deletion canceled")
            
            
    def reset_password(self):
        """Reset password after verifying current password"""
        data = self.load_data()
        print("Reset Password....")
        attempts = 4
        while attempts > 0: 
           username, password = self.get_data()
           if username in data and data[username]['password'] == password:
              new_password = input("Enter new password: ")
              data[username]['password'] = new_password
              self.save_data(data)
              self.password = new_password
              print("Password changed successfully")
              time.sleep(1)
              break
           else:
            attempts -= 1
            print(f"Incorrect username or password. Attempts left: {attempts}")
        else:
          print("You have exceeded the allowed attempts.\nReturning to main menu...")
 
    
    
    def forget(self):
        """Recover account by setting new password after confirming username"""
        print("Forget password")
        data = self.load_data()
        attempts = 4
        while attempts > 0:
          username = input("Enter your username to recover your account: ")
          if username in data:
              new_password = input("New password: ")
              confirm_password = input("Confirm password: ")
              if new_password == confirm_password:
                  data[username]['password'] = new_password
                  self.save_data(data)
                  self.password = new_password
                  print("Password changed successfully...")
                  time.sleep(1)
                  break
              else:
                attempts -= 1
                print(f"Password and confirm password do not match. Attempts left: {attempts}")
          else:
              attempts -= 1
              print(f"Couldn't find username. Try again! Attempts left: {attempts}")
              time.sleep(1)
        else:
          print("You have exceeded the allowed attempts.\nReturning to main menu...")                    
                    
                                    
def main():
    """Main menu"""
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
            user.reset_password()
        elif user_choice == "5":
           user.forget()  
        elif user_choice == "6":
            print("Thank you for being with us.\nall the best!")
            break    
        else:
            print("Invalid option. Try again")


if __name__ == "__main__":
    main()
