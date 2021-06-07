import os
from connection import PATH
listName=[]
def fileList(file_dir=PATH):
	fileList=os.listdir(file_dir)
	for file in fileList:
		if(os.path.isdir(file)):
			fileList(file_dir+'\\'+file)
		else:
			listName.append(file_dir+'\\'+file)
	return listName