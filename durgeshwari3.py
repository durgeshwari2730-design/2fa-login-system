import random

# Stored user (demo purpose)
stored_username = "admin"
stored_password = "durgeshwari1234"

def generate_otp():
    return random.randint(1000, 9999)

print("===== TWO FACTOR AUTHENTICATION DEMO =====")

# Step 1: Username & Password
username = input("Enter username: ")
password = input("Enter password: ")

if username == stored_username and password == stored_password:
    print("Password correct!")

    # Step 2: Generate OTP
    otp = generate_otp()
    print("\n Your OTP is:", otp)   # (In real system, it goes to phone/email)

    user_otp = input("Enter OTP: ")

    if int(user_otp) == otp:
        print(" Login Successful! Access Granted.")
    else:
        print(" Wrong OTP! Access Denied.")

else:
    print(" Invalid username or password!")
