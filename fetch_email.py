#created by Pranay Wajjala
#greenscizor

import email
import imaplib
import sys
import command_execute

host = 'imap.gmail.com'
username = 'your-mail-id'
password = "your-password"

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
sys.stdout = open(r"path-to-output-text-file", "w")
print(my_inbox)
exec(open('command_execute.py').read())
