#!/bin/bash
#size of content-length
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
