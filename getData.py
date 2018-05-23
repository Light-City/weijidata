# 导入urllib库的request模块
from urllib import request
# 定义url
url='http://www.baidu.com'
'''
    简单版
'''
# 请求url
resp=request.urlopen(url)
# 使用响应对象输出数据
# resp此时是http.client中HTTPResponse对象
print(resp)
# 以bytes输出client中HTTPResponse对象对象的内容
print(resp.read())
# 转为str类型(以utf-8编码输出)
print(resp.read().decode("utf-8"))

'''
    携带User-Agent头
'''
# 模拟真实浏览器
# 携带User-Agent头
req=request.Request(url)
# req.add_header(key,value)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36')
resp=request.urlopen(req)
print(resp.read().decode("utf-8"))
