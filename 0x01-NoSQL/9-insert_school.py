#!/usr/bin/env python3

"""
module for a function `insert_school`
takes a pymongo collection object `mongo_collection`
inserts a new document in a collection based on kwargs
returns the new _id
"""


def insert_school(mongo_collection, **kwargs):
    """
    args:   mongo_collection: pymongo.collection.Collection object
            **kwargs: name:str, address:str
    return: _id: str
    """
    document = mongo_collection.insert_one(kwargs)
    id = document.inserted_id
    return (id)
