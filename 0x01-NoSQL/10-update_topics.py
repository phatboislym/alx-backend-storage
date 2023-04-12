"""
module for a Python function `update_topics` 
changes all topics of a school document based on the name
takes:  a pymongo collection object `mongo_collection`
        `name`: str will be the school name to update
        `topics`: list[str] will be the list of topics approached in the school
return: None
"""


def update_topics(mongo_collection, name, topics):
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
