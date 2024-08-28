#!/usr/bin/env python3
"""Python function that returns the
list of school having a specific topic"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    Return the list of schools having a specific topic.

    Args:
    mongo_collection (pymongo.collection.Collection):
    The pymongo collection object.
    topic (str):
    The topic to search for in the school's topics list.

    Returns:
    list: A list of documents (schools) that have the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))
