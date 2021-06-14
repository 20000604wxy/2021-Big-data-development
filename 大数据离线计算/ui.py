from tkinter import *
from impala_conn_exec import impala_conn_exec
from element_show import get_database,get_table,get_rows
import pandas as pd


#元素区
def display(root):
	root.title("元素区")
	root.geometry('150x500')
	sb = Scrollbar(root)  
	sb.pack(side = RIGHT, fill = Y)   
	mylist = Listbox(root, yscrollcommand = sb.set,height=25)  
	mylist.insert(END, '数据库'+get_database())
	for table in get_table(get_database()):
		mylist.insert(END, '表->'+table)
		if(table!=''):
			for rows in get_rows(table):
				mylist.insert(END, '字段-->'+rows)
	  
	mylist.pack( side = LEFT )  
	sb.config( command = mylist.yview )  

#结果区
def show_result(root,input):
	if(input!=''):
		try:
			result=impala_conn_exec(input)
		except Exception as e:
			result=e
	else:
		result=''
		
	root.title("结果区")
	sb = Scrollbar(root)  
	sb.pack(side = RIGHT, fill = Y)
	sb2 = Scrollbar(root)  
	sb2.pack(side=BOTTOM,fill=X)
	text = Text(root)
	text.pack()
	text.insert("insert", result)

#工作区
def workspace(root):
	root.title("工作区")
	root.geometry('600x480')
	v = StringVar()
	e = Entry(root,textvariable=v,width=300)
	e.pack()

	def submit():
		input = e.get()
		root3=Tk()
		show_result(root3,input)
		root3.mainloop()
		
	b = Button(root,text="查询",width=15,height=2,command=submit)
	b.pack()
