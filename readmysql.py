import pymysql.cursors
connection = pymysql.connect(host='localhost', user='root', password='xxxx', db='wikiurl', charset='utf8mb4')
try:
    # 获取会话指针
    with connection.cursor() as cursor:
        # 查询语句
        sql="select `urlname`,`urlhref` from `urls` where id is not null"
        count=cursor.execute(sql)
        print(count)
        '''
        # 查询所有数据
        result=cursor.fetchall()
        print(result)
        print('---------------')
        '''
        # 查询三条数据
        result = cursor.fetchmany(size=3)
        print(result)
finally:
    connection.close()