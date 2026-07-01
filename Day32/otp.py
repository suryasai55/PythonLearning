import random
import smtplib

OTP = ""

for i in range(6):
    OTP += str(random.randint(0, 9))

msg = f"Subject: OTP Verification\n\nYour OTP is: {OTP}"

s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()

s.login("suryasaiofficial@gmail.com", "ormq nxfd zcsp hnkv")

sender = "suryasaiofficial@gmail.com"
receiver = input("Enter email: ")

s.sendmail(sender, receiver, msg)

print("OTP sent successfully!")

while True:
    a = input("Enter OTP: ")

    if a == OTP:
        print("OTP is correct")
        break
    else:
        print("OTP is incorrect")
