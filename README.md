# Python爬虫之英文维基百科词条获取

------
## 一、Python 爬虫学习
### 1.get方式
>简单

```python
# 导入urllib库的request模块
from urllib import request
# 定义url
url='http://www.baidu.com'
# 请求url
resp=request.urlopen(url)
# 使用响应对象输出数据
# resp此时是http.client中HTTPResponse对象
print(resp)
# 以bytes输出client中HTTPResponse对象对象的内容
print(resp.read())
# 转为str类型(以utf-8编码输出)
print(resp.read().decode("utf-8"))
```

>携带User-Agent头

```python
# 导入urllib库的request模块
from urllib import request
# 定义url
url='http://www.baidu.com'
# 模拟真实浏览器
# 携带User-Agent头
req=request.Request(url)
# req.add_header(key,value)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36')
resp=request.urlopen(req)
print(resp.read().decode("utf-8"))
```
### 2.post方式
```Python
# 导入urllib库下面的parse
from urllib import parse
from urllib import request
# 定义url
url='http://www.thsrc.com.tw/tw/TimeTable/SearchResult'
# 携带User-Agent头
req=request.Request(url)
# 使用urlencode生成post数据
postData=parse.urlencode([
    ('StartStation','e6e26e66-7dc1-458f-b2f3-71ce65fdc95f'),
    ('EndStation','fbd828d8-b1da-4b06-a3bd-680cdca4d2cd'),
    ('SearchDate','2018/05/22'),
    ('SearchWay','2018/DepartureInMandarin/22')
]
)
req.add_header('Origin','[{"key":"Origin","value":"http://www.thsrc.com.tw","description":""}]')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36')
# 使用postData发送post请求,注意此处postData可以是bytes类型，可迭代bytes对象，或者文件对象，但不能是str类型，故需要通过postData.encode('utf-8'),str转bytes
resp=request.urlopen(req,data=postData.encode('utf-8'))
# 打印请求状态
print(resp.status)
# 打印服务器的类型
print(resp.reason)
# 转为str类型(以utf-8编码输出)
print(resp.read().decode("utf-8"))
```
### 3.谷歌应用商店安装Postman

![](http://p20tr36iw.bkt.clouddn.com/scrap.jpg)

### 4.BeautifulSoup快速学习
```Python
from bs4 import BeautifulSoup as bs
import re
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# 不加解析器就报错，提供四种解析器，参考：https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
soup=bs(html_doc,"html.parser")
print(soup.prettify())
# 打印出第一个title标签
print("------------")
print(soup.title)
# 打印出标签内容
print("------------")
print(soup.title.string)
# 打印出标签名字
print("------------")
print(soup.title.name)
# 打印出第一个p标签
print("------------")
print(soup.p)
# 打印出p标签class属性的值,并以列表存储
print("------------")
print(soup.p['class'])
# 打印出所有的a标签,并以列表存储
print("------------")
print(soup.find_all('a'))
# 打印出id="link3"的标签
print("------------")
print(soup.find(id="link3"))
# 打印出所有a标签的链接
print("------------")
for link in soup.find_all('a'):
    print(link.get('href'))
# 打印出文档中所有文字内容
print("------------")
print(soup.get_text())
# 打印出id="link3"的标签的内容
print("------------")
print(soup.find(id="link3").get_text())
# 打印出所有a标签的所有内容
print("------------")
# print(soup.findAll('a').get_text()) 报错！
# 正确方法如下
for content in soup.find_all('a'):
    print(content.string)

# 查找class对应的标签
# 在python中class为关键字，不能使用同id查找那样，正确方法如下
print("------------")
print(soup.find('p',{'class','story'}))
# 打印出上述内容
print(soup.find('p',{'class','story'}).get_text()) # None
'''
为什么上述为None,而print(soup.title.string)，内容不为None，而是可以直接打印：The Dormouse's story？
从<title>The Dormouse's story</title>中知道title没有内部嵌入标签，如果改为<title>The Dormouse's story<a>hello</a></title>
则报错。这也正式string为None的原因，此时可以用get_text()
'''
# 正则表达式
for tag in soup.find_all(re.compile('^b')):
    print(tag.name)   # body b

soup.find_all()
# 找出所有含有href的a标签
a=soup.findAll('a',href=re.compile(r'^http://example.com/'))
print(a)
```
#### [更多详细用法](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)
### 5.爬虫数据存储至MySql
```Python
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
```
## 二、实战维基百科数据获取
```Python
import pymysql
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
```

## 三、数据持久化之MySql
![](http://p20tr36iw.bkt.clouddn.com/wikidata.png)
```Python
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
```
## 四、源码

### [点击此处](https://github.com/Light-City/weijidata)
