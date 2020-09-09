#!/bin/bash
cp  -r server.py www/runningserver.py
echo "Starting server \n"
python3 www/runningserver.py --directory www/
echo "Server running \n"