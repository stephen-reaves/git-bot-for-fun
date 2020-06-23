#!/bin/bash

# bash generate random 32 character alphanumeric string (upper and lowercase) and 
NEW_UUID=$(cat /dev/urandom | env LC_CTYPE=C tr -cd 'a-f0-9' | head -c 32)

cd ~/workspace/kres/random-stuff/
rm test.yml
./status.py
git add .
git commit -m $NEW_UUID
git push

