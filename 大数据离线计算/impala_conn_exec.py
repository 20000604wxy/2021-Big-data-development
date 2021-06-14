from impala.dbapi import connect
from impala.util import as_pandas
#连接设置
host='bigdata118.depts.bingosoft.net'
port=22118
user='user28'
password='pass@bingo28'
database='user28_db'

def impala_conn_exec(sql):
	conn = connect(
            host=host, 
            port=port, 
            auth_mechanism='PLAIN',
            user=user,password=password,
            database=database)
	cursor = conn.cursor()
	cursor.execute(sql)
	data_list=cursor.fetchall()
	return data_list