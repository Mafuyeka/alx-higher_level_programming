#!/bin/bash
# This script takes a URL, sends a request, and displays size of body
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
