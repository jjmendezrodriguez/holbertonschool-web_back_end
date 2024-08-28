#!/usr/bin/env python3
"""Python function that inserts a new document in a collection based on kwargs"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in the collection based on kwargs.

    Args:
    mongo_collection (pymongo.collection.Collection):
    The pymongo collection object.
    kwargs:
    Key-value pairs representing the document fields and values.

    Returns:
    ObjectId: The _id of the inserted document.
    """

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
