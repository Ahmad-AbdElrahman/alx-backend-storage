#!/usr/bin/env python3
'''
Where can I learn Python? 
'''


def schools_by_topic(mongo_collection, topic):
    '''
    returns the list of school having a specific topic
    '''
    result = mongo_collection.find({ "topics": topic })
    return list(result)
