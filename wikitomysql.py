import pymysql.cursors
from urllib import request
#导入bs4模块
from bs4 import BeautifulSoup as sp
#引用re方法
import re
# 维基百科url
url = "https://en.wikipedia.org/wiki/Main_Page"
#在浏览器下获取他们的headers信息
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'
          ,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
}
req = request.Request(url, headers=header)
#打开并读取url内信息
html = request.urlopen(req).read()
#利用bs4库解析html
soup = sp(html,"html.parser")
listUrls=soup.findAll('a',href=re.compile(r'^/wiki/'))
for url in listUrls:
    # 过滤掉以.jpg|JPG结尾的词条地址
    if not re.search(r"(.jpg|JPG)",url['href']):
        # 输出词条名字与词条地址
        print(url.get_text(),"<-------->",'https://en.wikipedia.org'+url['href'])
    connection = pymysql.connect(host='localhost', user='root', password='xxxx', db='wikiurl', charset='utf8mb4')
    try:
        # 通过with实现把connection.cursor()返回得到cursor对象
        with connection.cursor() as cursor:
            # 创建sql语句
            sql="insert into `urls`(`urlname`,`urlhref`)values(%s,%s)"
            # 执行sql语句
            cursor.execute(sql,(url.get_text(),'https://en.wikipedia.org'+url['href']))
            connection.commit()
    finally:
        connection.close()