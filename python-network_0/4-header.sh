#!/bin/bash
# Sends request with an added custom header
curl -sH "X-School-User-Id: 98" "$1"
