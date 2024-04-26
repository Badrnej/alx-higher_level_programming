#!/bin/bash
#size of content-length
curl -s -o /dev/null -w "%{http_code}" "$1"
