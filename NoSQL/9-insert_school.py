#!/usr/bin/env python3
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
    # Insert the document and get the insert result
    result = mongo_collection.insert_one(kwargs)
    # Return the _id of the inserted document
    return result.inserted_id
