#!/bin/bash
#size of content-length
curl -sI "$1" | grep -i Allow | cut -d ' ' -f2-
