from connection import s3,BUCKET,PATH
def deleteObject(bucket,key,versionID):
	if(versionID==None):
		versionID=''
	Bucket=s3.Bucket(bucket)
	try:
		response =Bucket.delete_objects(
			Delete={
				'Objects': [
					{
						'Key': key,
						'VersionId': versionID
					},
				],
				'Quiet': True|False
			},
		)
		print("{} delete done".format(key))
	except Exception as e:
		print("upload {} error:{}".format(key, e))

from getObject import objectList
from getdir import fileList



listpre=fileList()
newListLocal=[]
for str in listpre:
	s0=str.replace('\\','/')
	s1=s0.replace(PATH.replace('\\','/')+'/','')
	newListLocal.append(s1)
	
newListS3=[]
for objsum in getObject.objectList():
	newListS3.append(objsum.key)
	
listLocal=sorted(newListLocal)
listS3=sorted(newListS3)


from getVersionByID import getVersionID
if(listLocal!=listS3):
	listtodel=list(set(listS3).difference(set(listLocal)))
	ID=[]
	for obj in listtodel:
		ID.append(getVersionID(BUCKET,obj))
	for iter in listtodel:
		deleteObject(BUCKET,iter,id[listtodel.index(iter)])