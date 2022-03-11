#!/usr/bin/env python3

import os
import sys
import emails
import reports
import datetime

files_dir = 'supplier-data/descriptions'


def MakeContent(files_dir):

    content = ""
    files = os.listdir(files_dir)

    for filename in files:
        if not filename.endswith('.txt'):
            continue

        with open (os.path.join(files_dir, filename), 'r') as txt_file:
            content += txt_file.readline() + "\n"
            content += txt_file.readline() + "\n"
        txt_file.close()
        content += "\n"
    
    return content


def main():

    # Gather content
    content = MakeContent(files_dir)

    # Create report
    reports.generate_report(
        '/tmp/processed.pdf', 
        "Processed Update on {}".format(datetime.date.today()),
        content.replace('\n', '<br/>')
    )

    # Send report email
    email_msg = emails.generate_email(
        sender='automation@example.com',
        recipient='username@example.com',
        subject='Upload Completed - Online Fruit Store',
        body='All fruits are uploaded to our website successfully. A detailed list is attached to this email',
        attachment_path='/tmp/processed.pdf'
    )
    emails.send_email(email_msg)


if __name__ == "__main__":
    sys.exit(main())

