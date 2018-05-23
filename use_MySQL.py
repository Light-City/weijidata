# 引入开发包
import pymysql.cursors
# 获取数据库链接
connection=pymysql.connect(host='localhost',user='root',password='xxxx',db='xxx',charset='utf8mb4')
# 获取会话指针
new_cursor=connection.cursor()
# 执行SQL语句
sql=""
new_cursor.execute(sql,('参数1','参数n'))
# 提交
connection.commit()
# 关闭
connection.close()
# 读取mysql数据
# 得到总纪录数
new_cursor.execute()
# 查询下一行
new_cursor.fetchone()
# 得到指定大小
new_cursor.fetchmany(size=None)
# 得到全部
new_cursor.fetchall()
# 关闭
connection.close()