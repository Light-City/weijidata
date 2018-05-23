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