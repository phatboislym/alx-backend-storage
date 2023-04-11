#!/usr/bin/env python3

"""
module for function `list_all`
takes a pymongo collection object `mongo_collection`
returns a list of all documents in a collection
        or an empty list if there is no document in the collection
"""


def list_all(mongo_collection):
    """
    args: mongo_collection: pymongo.collection.Collection object
    return: collection: list
    """
    collection = []
    for mongo in mongo_collection.find():
        collection.append(mongo)
    return (collection)
