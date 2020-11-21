import pymongo

# mongodb를 파이썬 코드를 통해 연결
MONGO_CONN = pymongo.MongoClient('mongodb://localhost') 

# mongodb가 얘기치 못하여 끊겼을 경우 다시 연결
def conn_mongodb() :
    try : 
        MONGO_CONN.admin.command('ismaster')
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    except :
        MONGO_CONN = pymongo.MongoClient('mongodb://localhost')
        blog_ab = MONGO_CONN.blog_session_db.blog_ab

    return blog_ab