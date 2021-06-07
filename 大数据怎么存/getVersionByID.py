from connection import s3,BUCKET

def getVersionID(bucket,key):
	object=s3.Object(bucket,key)
	return object.version_id