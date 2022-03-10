#! /usr/bin/env python3

import os
import sys
import requests


REQUEST_URL  = 'http://<corpweb-external-IP>/feedback'
FEEDBACK_DIR = '/data/feedback'



def parse_file(filepath) -> dict:
    
    data_to_send = {}

    with open(filepath, 'r') as file_content:
        lines = file_content.readlines()

        data_to_send["title"]       = lines[0]
        data_to_send["name"]        = lines[1]
        data_to_send["date"]        = lines[2]
        data_to_send["feedback"]    = lines[3]

    file_content.close()
    return data_to_send

def send_request(data_to_send):

    # requests.post (url, data=p)
    response = requests.post (REQUEST_URL, json=data_to_send)

    # response status check
        # raise error if request's response aren't good | response.raise_for_status()
    response.raise_for_status()


def main():

    # Listing files in directory
    files = os.listdir (FEEDBACK_DIR)

    # For loop
    for file in files:
        filepath = os.path.join (FEEDBACK_DIR, file)

        if not filepath.endswith('.txt'):
            continue

        # Parse file into dictionary
        data_to_send = parse_file(filepath)
        # Send post_request
        send_request (data_to_send)


if __name__ == "__main__":
    sys.exit (main())