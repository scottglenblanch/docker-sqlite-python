#!/bin/sh

apt-get update

# get python and sqlite
apt-get install -y sqlite3 python3

# delete folders so can use in container
rm -rf /app/db
rm -rf /app/src
