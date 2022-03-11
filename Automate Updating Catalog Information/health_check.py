#!/usr/bin/env python3

import psutil
import socket
import emails
import sys

sender = 'automation@example.com'
recipient = 'username@example.com'



def manageCheck(send_email: bool, subject: str):

    if send_email:
        email_msg = emails.generate_email(
            sender=sender,
            recipient=recipient,
            subject=subject,
            body='Please check your system and resolve the issue as soon as possible.'
        )
        emails.send_email (email_msg)


def CheckHealth():

    cpu_check = psutil.cpu_percent() > 80
    manageCheck(cpu_check, 'Error - CPU usage is over 80%')

    disk_check = (100 - psutil.disk_usage('/').percent) < 20
    manageCheck(disk_check, 'Error - Available disk space is less than 20%')

    mem_check = (psutil.virtual_memory().available / 1048576) < 500
    manageCheck(mem_check, 'Error - Available memory is less than 500MB')

    host_check = socket.gethostbyname('localhost') != '127.0.0.1'
    manageCheck(host_check, 'Error - localhost cannot be resolved to 127.0.0.1')


def main():
    CheckHealth()


if __name__ == "__main__":
    sys.exit(main())





