from pymongo import MongoClient
import gridfs
def mongo_conn():
    try:
        conn=MongoClient(host="127.0.0.1",port=27017)
        print("mongo connected")
        return conn.paradisehope
    except Exception as e:
        print("Error in mongo connection:",e)
db=mongo_conn()

fs=gridfs.GridFS(db)

name="youtube.mp4"

data=db.fs.files.find_one({"filename":name})
print(data)
myid=data['_id']

outputdata=fs.get(myid).read()

output=open("mongodb_video.mp4","wb")
output.write(outputdata)

output.close()
print("download complete")

