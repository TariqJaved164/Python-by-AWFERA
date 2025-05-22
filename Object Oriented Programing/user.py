class User:
    """A class to represent a user profile."""
    
    def __init__(self, first_name, last_name, age, email, location):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        
    
    def describe_user(self):
        """Print a summary of the user's information."""
        print("\nUser Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
        
    
    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"\nHello, {self.first_name} {self.last_name}! Welcome back to our platform.")
    
    

# Create several instances representing different users
user1 = User("John", "Doe", 28, "john.doe@example.com", "New York")
user2 = User("Alice", "Smith", 32, "alice.smith@example.com", "London")
user3 = User("Mohammed", "Khan", 24, "m.khan@example.com", "Dubai")

# Call methods for each user
# User 1
user1.describe_user()
user1.greet_user()

# User 2
user2.describe_user()
user2.greet_user()

# User 3
user3.describe_user()
user3.greet_user()