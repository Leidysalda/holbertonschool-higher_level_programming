#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me
curl -sL -X PUT "$1" -d "user_id=98" -H "origin: HolbertonSchool"
