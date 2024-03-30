#!/bin/bash
# This script sends a JSON POST request to a URL with contents of a file in the body
# It then displays the body of the response
file_content=$(cat "$2" 2>/dev/null)
if [[ $? -ne 0 ]]; then
    echo "Not a valid JSON"
    exit 1
fi

curl -sX POST -H "Content-Type: application/json" -d "$file_content" "$1"
