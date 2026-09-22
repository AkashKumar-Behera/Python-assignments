def forCheckPass(password):
    for char in password:
        if len(password) < 8:
            print("False \nPassword must be at least 8 characters long.")
            password = input("Enter your password: ")
            
        elif not any(char.isdigit() for char in password):
            print("False \nPassword must contain at least one digit.")
            password = input("Enter your password: ")
            
        elif not any(char.isupper() for char in password):
            print("False  \nPassword must contain at least one uppercase letter.")
            password = input("Enter your password: ")
            
        elif not any(char.islower() for char in password):
            print("False \nPassword must contain at least one lowercase letter.")
            password = input("Enter your password: ")
            
        elif not any(not char.isalnum() for char in password):
            print("False \nPassword must contain at least one special character.")
            password = input("Enter your password: ")
            
        else:
            print("True \nPassword is valid.")
            break

password = input("Enter your password: ")
forCheckPass(password)