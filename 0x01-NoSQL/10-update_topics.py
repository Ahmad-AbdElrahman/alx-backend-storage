#!/usr/bin/env python3
'''
Change school topics 
'''


def update_topics(mongo_collection, name, topics):
    '''
    changes all topics of a school document based on the name
    '''
    result = mongo_collection.update_many(
        { "name": name },       # Filter to find the document by name
        { "$set": { "topics": topics } }  # Update operation to set the topics field
    )
    return result.modified_count
