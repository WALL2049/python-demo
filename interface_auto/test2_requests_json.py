# coding = utf-8
# API 响应的消息体格式，通常以json居多。
# 为了 方便处理 响应消息中json 格式的数据 ，我们通常应该把 json 格式的字符串 转化为 python 中的数据对象。
# 怎么转化？ 前面我们学习过 json库，可以直接使用 json库里面的 loads 函数， 把 json 格式的字符串 转化为 数据对象

import requests,json
response = requests.post("http://httpbin.org/post", data={1:1,2:2})

# obj = json.loads(response.text)   # 字符串text（文本）等同于字节串content（内容）再编码
obj = json.loads(response.content.decode('utf8'))
print(obj)
print(obj['form']['1'])

# requests库为我们提供了更方便的方法，可以使用 Response对象的 json方法，
# 如下：
print('\n\n--------response对象的json方法-------')
response = requests.post("http://httpbin.org/post", data={1:1,2:2})
obj = response.json()
print(obj)
print(obj['form']['1'])