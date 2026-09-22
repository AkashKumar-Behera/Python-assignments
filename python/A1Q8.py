def check_password(password):
    if len(password) < 8:
        return "False \nPassword must be at least 8 characters long."
    elif not any(char.isdigit() for char in password): #
        return "False \nPassword must contain at least one digit."
    elif not any(char.isupper() for char in password):
        return "False  \nPassword must contain at least one uppercase letter."
    elif not any(char.islower() for char in password):
        return "False \nPassword must contain at least one lowercase letter."
    else:
        return "True \nPassword is valid."


password=input("Enter your password: ")
print(check_password(password))