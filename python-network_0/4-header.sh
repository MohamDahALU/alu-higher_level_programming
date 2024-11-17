#!/bin/bash
# Sends request with an added custom header
curl -s --header "X-HolbertonSchool-User-Id: 98" "$1"
