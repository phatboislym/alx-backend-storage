#!/usr/bin/env python3

"""
module for a Python function `schools_by_topic`
returns a list of school having a specific topic
takes:  a pymongo collection object `mongo_collection`
        `topic`: list[str] will be the list of topic searched
return: schools: list[str]
"""


def schools_by_topic(mongo_collection, topic):
    """
    args:   mongo_collection: pymongo.collection.Collection
            topic: list[str]
    return: schools: list[str]
    """
    schools = []
    for collection in mongo_collection.find({'topics': topic}):
        schools.append(collection)

    return schools
