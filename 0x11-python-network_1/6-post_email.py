#!/usr/bin/python3
""" Script that takes in a URL and an email, sends a POST request
 And displays the body of the response
"""

import urllib.parse
import urllib.request
import sys

def send_post_request(url, email):
    # Encode email parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    
    # Send POST request
    with urllib.request.urlopen(url, data=data) as response:
        # Decode and display the body of the response
        body = response.read().decode('utf-8')
        print(body)

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    # Extract URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Send POST request
    send_post_request(url, email)
