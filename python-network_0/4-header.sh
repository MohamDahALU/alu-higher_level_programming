#!/bin/bash
# Sends request with an added custom header
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
