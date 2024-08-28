#!/usr/bin/env python3
"""Python script that provides some stats
about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def log_stats():
    """
    Provides statistics about Nginx logs stored in MongoDB.
    """
    # Conectar a la base de datos MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Contar el número total de logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Contar el número de logs por método HTTP
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Contar el número de logs con method=GET y path=/status
    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
        )
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
