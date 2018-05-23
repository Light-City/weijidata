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