#!/bin/bash
# print all allowed methods
curl -i -sL -X OPTIONS "0.0.0.0:5000/route_4" | grep "Allow" | cut -f2 -d":" | tail -c+2
