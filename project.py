import hashlib
import random

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self.hash_password(password)
        self.is_logged_in = False

    def hash_password(self, password):
        # Use a strong hashing algorithm like SHA-256
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

class CybersecurityApp:
    def __init__(self):
        self.users = {}
        self.logged_in_user = None

    def register_user(self, username, password):
        if username in self.users:
            print("Username already exists. Please choose another one.")
        else:
            user = User(username, password)
            self.users[username] = user
            print("Registration successful.")

    def login(self, username, password):
        if username in self.users:
            user = self.users[username]
            if user.password == user.hash_password(password):
                user.is_logged_in = True
                self.logged_in_user = user
                print("Login successful.")
            else:
                print("Incorrect password. Please try again.")
        else:
            print("User not found. Please register.")

    def logout(self):
        if self.logged_in_user:
            self.logged_in_user.is_logged_in = False
            self.logged_in_user = None
            print("Logout successful.")
        else:
            print("No user is currently logged in.")

    def generate_random_password(self, length=12):
        # Generate a random password of the specified length
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?"
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

if __name__ == "__main__":
    app = CybersecurityApp()

    while True:
        print("\n1. Register\n2. Login\n3. Logout\n4. Generate Random Password\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            app.register_user(username, password)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            app.login(username, password)

        elif choice == "3":
            app.logout()

        elif choice == "4":
            length = int(input("Enter the length of the password: "))
            random_password = app.generate_random_password(length)
            print("Generated password:", random_password)

        elif choice == "5":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")
