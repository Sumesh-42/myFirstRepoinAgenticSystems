# Interactive Profile Builder

# Get user input
user_name = input("What is your name? ")
user_age = int(input("What is your age? "))
is_active_input = input("Are you an active user? (True/False) ")
is_active_user = is_active_input == "True"

# Print formatted summary using f-string
print(f"User {user_name} is {user_age} years old. Active status: {is_active_user}")