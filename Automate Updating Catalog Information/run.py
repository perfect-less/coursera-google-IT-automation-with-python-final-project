#! /usr/bin/env python3

import os
import sys
import requests


REQUEST_URL  = 'http://<corpweb-external-IP>/fruits/'
CONTENTS_DIR = 'supplier-data/descriptions/'



def parse_file(filepath) -> dict:
    """Read the given file and return its contents as dictionary"""
    data_to_send = {}

    with open(filepath, 'r') as file_content:
        lines = file_content.readlines()

        data_to_send["name"]        = lines[0].strip()
        data_to_send["weight"]      = int(lines[1].strip().removesuffix('lbs'))
        data_to_send["description"] = lines[2].strip()
        data_to_send["image_name"]  = os.path.basename(filepath)

    file_content.close()
    return data_to_send

def send_request(data_to_send):
    """Send POST request with data_to_send as data
    Raises Exceptions if the response is not ok."""
    # requests.post (url, data=p)
    response = requests.post (REQUEST_URL, data=data_to_send)

    # response status check    
    response.raise_for_status()


def main():
    """List files in the CONTENTS_DIR, parse each of
    them into dictionary and then send request to 
    the web API."""
    # Listing files in directory
    files = os.listdir (CONTENTS_DIR)

    for filename in files:
        filepath = os.path.join (CONTENTS_DIR, filename)

        # Only process txt files
        if not filepath.endswith('.txt'):
            continue

        # Parse file into dictionary and then send request
        data_to_send = parse_file(filepath)
        send_request (data_to_send)


if __name__ == "__main__":
    sys.exit (main())