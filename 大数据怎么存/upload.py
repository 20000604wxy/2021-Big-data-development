import boto3
from connection import s3,PATH,BUCKET

def upload(bucket_name, file_pathname ,obj_name):
	with open(file_pathname, 'rb') as f:
		f_stream = f.read()
		try:
			s3.Object(bucket_name,obj_name).upload_file(file_pathname)
			print("{} upload done".format(obj_name))
		except Exception as e:
			print("upload {} error:{}".format(obj_name, e))

def getBlock(file,blockSize):
	offset=0
	result = [];
	with open(file,'rb') as f:
		size=os.stat(file).st_size
		try:
			while offset<=size:
				result.append(f.read([blockSize]))
				offset+=blockSize
				f.seek(offset)
		except Exception as e:
			print(e)

	return result	
	
def multiUpload(bucket_name, file_pathname ,obj_name):
	uploadList=getBlock(file_pathname,5000000)
	for part in uploadList:
		try:
			response = s3.MultipartUploadPart(bucket_name,obj_name,str(uploadList.index(part)),str(uploadList.index(part))).upload(Body=part)
		except Exception as e:
			print("upload {} error:{}".format(obj_name, e))

from getdir import fileList
import os

def dirCatalogue(path=PATH):
	dir=path
	return(fileList(dir))

list=dirCatalogue(PATH)
source_size = []
for file in list:
	size=os.stat(file).st_size
	source_size.append(size)
limitsize=10000000


newList=[]
for str in list:
	s0=str.replace('\\','/')
	s1=s0.replace(PATH.replace('\\','/')+'/','')
	newList.append(s1)


for path in list:
	print(list.index(path))
	if source_size[list.index(path)]<limitsize:
		upload(BUCKET,path,newList[list.index(path)])
	else:
		multiUpload(BUCKET,path,newList[list.index(path)])
	
