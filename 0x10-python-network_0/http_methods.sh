#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL="$1"

# Send a request to the URL and display the allowed methods
curl -sI "$URL" | grep -i Allow | awk '{print "Allowed HTTP Methods:", $2, $3, $4, $5, $6, $7, $8}'
