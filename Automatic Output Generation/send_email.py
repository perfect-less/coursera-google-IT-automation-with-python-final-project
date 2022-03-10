#!/usr/bin/env python3
"""This is my own attempt on writing script to send email with attachments."""

import mimetypes
import smtplib
import getpass
import sys
import os

from email.message import EmailMessage

# Email contents and parameter
sender      = "sender.email@mail.com"
receiver    = "receiver.email@mail.com"

subject     = "This is the Email Subject"
email_body  = """Hi, There

And this is the body (contents) of the email."""

attachment_path = 'attachments/cool_picture.jpg'


def ProcessAttachment(attachment_path):
    
    filename = os.path.basename (attachment_path)

    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    return mime_type, mime_subtype, filename


def CreateEmailMessage():
    message = EmailMessage ()
    
    message["From"] = sender
    message["To"]   = receiver

    message["Subject"] = subject
    message.set_content(email_body)

    mime_type, mime_subtype, filename = ProcessAttachment(attachment_path)

    with open (attachment_path, 'rb') as att:
        message.add_attachment(
            att.read(),
            maintype=mime_type,
            subtype=mime_subtype,
            filename=filename
        )

    return message


def SendSMPTEmail(message):

    SMPT_SERVER = 'smtp.gmail.com'
    SMPT_DEBUGLEVEL = 0 # Set 1 for debuging

    mail_server = smtplib.SMTP_SSL(SMPT_SERVER)
    mail_server.set_debuglevel(SMPT_DEBUGLEVEL)

    try:
        mail_pass = getpass.getpass('\n Please Enter Your Password: ')
        mail_server.login(sender, mail_pass)

    except smtplib.SMTPAuthenticationError as e:
        print ('\n Failed to Login into your email')
        print (e)

        mail_server.quit()
        return 1

    
    mail_server.send_message(message)
    mail_server.quit()

    print ("Email Sent to {}".format (receiver))

    return 0
        



def main():
    
    # Create message object
    print ("Creating message Object")
    message = CreateEmailMessage()

    print ("..message object createt")

    # Send email
    print ("Sending Email")
    return SendSMPTEmail (message)


if __name__ == "__main__":
    sys.exit (main())