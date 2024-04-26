#!/bin/bash
#size of content-length
curl -sX PUT -L -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
