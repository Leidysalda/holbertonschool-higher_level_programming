#!/bin/bash
# Bash script that sends a request to a URL passed as an argument
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
