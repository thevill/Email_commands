#created by Pranay Wajjala
#blackberryMonk#bhavitavya
#this program creates a new folder
#you can edit and make your pc run custom commands through email

import email
import imaplib
import sys
import os
import subprocess
from pathlib import Path

host = 'imap.gmail.com'
username = 'your_username'
password = "your_password"

def get_inbox():
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    _, search_data = mail.search(None, 'UNSEEN')
    my_message = ""
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                email_data= body.decode()
        my_message = email_data
        
    return my_message


my_inbox = get_inbox()
output_file = open(r"path_to_file", "w+")
output_file.write(my_inbox)
output_file.close()
output_file = open(r"path_to_file","r")
txt = output_file.readline()
txt = txt.replace('\n', '')
if txt == "create folder":
    path = 'path_to_folder'
    os.chdir(path)
    Newfolder = 'task_1'
    os.makedirs(Newfolder)
    print("A new folder with the name, task_1 has been created at ",path)
