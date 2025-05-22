class User:
    """A class to represent a user profile."""
    
    def __init__(self, first_name, last_name, age, email, location):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0  # New attribute to track login attempts
    
    def describe_user(self):
        """Print a summary of the user's information."""
        print("\nUser Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
        print(f"Login attempts: {self.login_attempts}")
    
    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"\nHello, {self.first_name}! Welcome back to our platform.")
    
    def increment_login_attempts(self):
        """Increment the number of login attempts by 1."""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset the number of login attempts to 0."""
        self.login_attempts = 0

# Create an instance of User
user1 = User("Emma", "Johnson", 29, "emma.j@example.com", "Boston")

# Increment login attempts several times
print(f"Initial login attempts: {user1.login_attempts}")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"After 3 login attempts: {user1.login_attempts}")  # Should show 3

# Reset login attempts
user1.reset_login_attempts()
print(f"After reset: {user1.login_attempts}")  # Should show 0