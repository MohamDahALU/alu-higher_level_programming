#!/bin/bash
# Sends request with an added custom header
curl -sL -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
