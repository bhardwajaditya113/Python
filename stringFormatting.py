user_input = input("Enter your name:")
#String formatting with 2.7 or less
message = "Hello %s!" % user_input
#String formatting with 3.6 or above
message = f"Hello! {user_input}"
print(message)
