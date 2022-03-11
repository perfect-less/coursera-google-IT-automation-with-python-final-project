#!/usr/bin/env python3
import requests
import os

# Modified example_upload.py to upload .jpeg files
# inside files_dir

url = "http://localhost/upload/"
files_dir = 'supplier-data/images/'


def main():

    files = os.listdir(files_dir)

    for filename in files:

        if not filename.endswith('.jpeg'):
            continue

        with open(os.path.join(files_dir, filename), 'rb') as opened:
            r = requests.post(url, files={'file': opened})
            r.raise_for_status ()


if __name__ == "__main__":
    main()