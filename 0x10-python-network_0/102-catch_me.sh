#!/bin/bash
# This script makes a request that causes the server to respond with "You got me!"
curl -s -L -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
