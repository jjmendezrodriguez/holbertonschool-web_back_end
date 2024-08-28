#!/usr/bin/env python3
"""Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """list all documents"""

    lst_all = mongo_collection.find()

    return list(lst_all)