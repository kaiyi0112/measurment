import MySQLdb
# conn = MySQLdb.connect(host="163.18.69.14", user="root", passwd="rsa+0414018", db="pdal-measure")
# cursor = conn.cursor()
# cursor.execute("SELECT VERSION()")
# print("Database version : %s " % cursor.fetchone())
# cursor.execute("create table mainsite_students(id int ,name varchar(20),class varchar(30),age varchar(10))") #建立資料表名稱 : mainsite_students
# SQL=("SELECT * FROM mainsite_project")
# cursor.execute(SQL)
# print(list(cursor.fetchone()))
# print(list(cursor.fetchone()))
# # print(list(cursor.fetchall()))
# a = list(cursor.fetchall())
# print(list(list(cursor.fetchall())[0]))
# cursor.fetchall()
def sql_test(table_name):
    conn = MySQLdb.connect(host="163.18.69.14", user="root", passwd="rsa+0414018", db="pdal-measure", charset="utf8") #新增 charset="utf8"才會顯示中文
    cursor = conn.cursor()
    SQL = ("SELECT * FROM  %s"%table_name)
    cursor.execute(SQL)
    return list(cursor.fetchall())

# a=sql_test("mainsite_project")
# print(a)
# b=sql_test("mainsite_measurement")
# print(b)
conn = MySQLdb.connect(host="163.18.69.14", user="root", passwd="rsa+0414018", db="pdal-measure",charset="utf8")  # 新增 charset="utf8"才會顯示中文
cursor = conn.cursor()
SQL =("INSERT INTO mainsite_project(id,name,create_time) VALUES ('5','159','20200731')")
cursor.execute(SQL)
conn.commit()