from pymongo import MongoClient
import gridfs

def mongo_conn():
    try:
        conn=MongoClient(host="127.0.0.1",port=27017)

        print("mongo connected")
        return conn
        #return conn.paradisehope
    except Exception as e:
        print("Error in mongo connection:",e)


conn=mongo_conn()
db=conn.paradisehope
#db=mongo_conn()

name="youtube.mp4"
filedata=open(name,"rb")
data=filedata.read()


fs=gridfs.GridFS(db)
fs.put(data,filename=name)
print("upload complete")
