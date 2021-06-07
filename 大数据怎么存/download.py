from connection import s3,BUCKET
import botocore
def getFileByKey(bucket,key):
	try:
		s3.Object(bucket, key).download_file(key)

	except botocore.exceptions.ClientError as e:
		if e.response['Error']['Code'] == "404":
			print("The object does not exist.")
		else:
			raise
			
import getObject
Objectlist=getObject.objectList(BUCKET)
for obj in Objectlist:
	getFileByKey(BUCKET,obj)
	
