user_db = "admin"
pass_db = "1234"
otp_secret = "5566"

user = input("User: ")
pw = input("Pass: ")

if user == user_db and pw == pass_db:
    otp = input("Enter OTP: ")
    if otp == otp_secret:
        print("Success")
    else:
        print("Wrong OTP")
else:
    print("Fail")