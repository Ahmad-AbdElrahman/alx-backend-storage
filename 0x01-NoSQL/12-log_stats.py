#!/usr/bin/env python3
"""
This project module contains a Python script that provides
some stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
myclient = MongoClient()
db = myclient["logs"]
nginx = db["nginx"]
print("{} logs".format(nginx.count_documents({})))
print("Methods:")

for method in methods:
    print(
        "\tmethod {}: {}".format(
            method, nginx.count_documents({"method": method}))
    )

print(
    "{} status check".format(
        nginx.count_documents({"method": "GET", "path": "/status"}))
)
