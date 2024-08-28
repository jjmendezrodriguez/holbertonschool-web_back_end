#!/usr/bin/env python3
"""Python function that changes all topics
of a school document based on the name"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Update all topics of a school document based on the name.

    Args:
    mongo_collection (pymongo.collection.Collection):
    The pymongo collection object.
    name (str): The school name to update.
    topics (list):
    The list of topics to set in the school document.

    Returns:
    None
    """

    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
