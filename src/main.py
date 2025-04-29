import json 
import time
import datetime as dt

class Account:
    
    def __init__(self):
        self.username = None
        self.password = None
        self.confirm_password = None
        
    def load_data (self):
        with open("src/accounts.json" , 'r') as file:
            return json.load(file)
        
    def save_data(self, data):
        with open("src/accounts.json" , 'w') as file:
            json.dump(data , file , indent=4)  
                  
    def get_data(self): 
        username = input("Enter Username :")
        password = input("Enter Password:")
        return username , password
       
    def create(self):
        print("== Creating Account ==")
        account = Account()
        data = account.load_data()
        self.username , self.password =  self.get_data()
        if self.username.strip() == "" or self.password.strip() == "":
            print("You must enter valid info")
                
        if self.username in data:
            print("Username was teken try another one")
            return
        
        if self.password != self.confirm_password:
            print("Password does not match")
            return
    
        self.confirm_password = input("Confirm Password: ")
        data[self.username] = {'password' : self.password}
        account.save_data(data)
  
        

    def login(self):
        account = Account()
        data = account.load_data()

        print("== Login Account ==")
        
        attempts = 4
        while attempts > 0: 
            username_login, password_login = self.get_data()
            if username_login in data and data[username_login]['password'] == password_login:
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
        account = Account()
        data = account.load_data()
        confirm = input("Are you sure you want to delete your account? (yes/no): ").strip().lower()
        if confirm == "yes":
          if self.username in data:
            del data[self.username]
            account.save_data(data)
            print("Account deleted successfully")
            time.sleep(1)
            self.username = None
            self.password = None
          else:
            print("Account not found.")
        else:
         print("Account deletion canceled")
            
            
    def reset_passowrd(self):
        account = Account()
        data = account.load_data()
        print("Reset Password....")
        attempts = 4
        while attempts > 0: 
           username, password = self.get_data()
           if username == self.username and password == self.password:
              new_password = input("Enter new password: ")
              data[self.username]['password'] = new_password
              account.save_data(data)
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
        print("Forget password")
        account = Account()
        data = account.load_data()
        attempts = 4
        while attempts > 0:
          username = input("Enter your username to recover your account: ")
          if username == self.username:
              new_password = input("New password: ")
              confirm_password = input("Confirm password: ")
              if new_password == confirm_password:
                  data[self.username]['password'] = new_password
                  account.save_data(data)
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
