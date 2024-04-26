#!/bin/bash
#size of content-length
curl -s "$1" | wc -c
