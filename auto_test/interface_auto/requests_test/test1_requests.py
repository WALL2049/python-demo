
import requests


proxies = {
    'http':'http://127.0.0.1:8888',
    'https':'http://127.0.0.1:8888'
}
urlpara = {
    'wd':'上海疫情',
    'rsv_spt':'1'
}
url_baidu = 'https://www.baidu.com/s'
url1 = 'http://httpbin.org/get'
url2 = 'http://httpbin.org/post'
headers = {
    'user-agent': 'kevin-app/7.7.7',
    'auth-type': 'kevin-token',
    'cookies': '123'
}
payload_XML = '''
<?xml version="1.0" encoding="UTF-8"?>
<WorkReport>
    <Overall>良好</Overall>
    <Progress>30%</Progress>
    <Problems>暂无</Problems>
</WorkReport>
'''
payload_urlencoded = {
    'key1': 'value1',
    'key2': 'value2'
}
payload_JSON ={
    "Overall":"良好",
    "Progress":"30%",
    "Problems":[
        {
            "No" : 1,
            "desc": "问题1...."
        },
        {
            "No" : 2,
            "desc": "问题2...."
        }
    ]
}
# response = requests.get('https://www.baidu.com/s?wd=上海疫情&rsv_spt=1')
# response_get1 = requests.get(url_baidu, params=urlpara)
# response_get1 = requests.get(url1,
#                             params=urlpara,
#                             proxies=proxies,
#                             verify=False)
#
# response_get2 = requests.get(url1,
#                              params=urlpara,
#                              headers=headers,
#                              proxies=proxies,
#                              verify=False)

# response_post1 = requests.post(url2,
#                                 headers=headers,
#                                 data=payload_XML.encode('utf-8'),
#                                 proxies=proxies,
#                                 verify=False)
#
# response_post2 = requests.post(url2,
#                                 # headers=headers,         # 可以修改header
#                                 data=payload_urlencoded,  # dict格式数据表示是以urlencoded格式传入
#                                 proxies=proxies,
#                                 verify=False)

response_post3 = requests.post(url2,
                               json=payload_JSON,   # json表示是以json格式传入数据
                               proxies=proxies,
                               timeout=5,
                               verify=False)
# response_post3.encoding='utf8'        # 但是有时候，服务端并不一定会在消息头中指定编码格式，这时， requests的推测可能有误，需要我们指定编码格式。
print('\n--------消息体---默认编码格式-------')
print(response_post3.encoding)  # 默认编码格式
# print(response_get1.text.encode('utf-8'))
# print(response_get2.text)
print('\n-----------状态码----------')
print(response_post3.status_code)
print('\n-----------消息头----------')
print(response_post3.headers)
# print(response_post3.headers['Content-Type'])            # headers是dict的子类，可以通过键获取值，但不是dict，可以转化一下
print(dict(response_post3.headers)['Content-Type'])
print('\n--------消息体---文本-------')
print(response_post3.text)
# 那么，requests是 以什么编码格式 把HTTP响应消息体中的 字节串 解码 为 字符串的呢？
# requests 会根据响应消息头（比如 Content-Type）对编码格式做推测。
# 但是有时候，服务端并不一定会在消息头中指定编码格式，这时， requests的推测可能有误，需要我们指定编码格式。
# 可以通过这样的方式指定
# import requests
#
# response = requests.get('http://mirrors.sohu.com/')
# response.encoding='utf8'
# print(response.text)

#如果我们要直接获取消息体中的字节串内容，可以使用 content 属性，
# response是对象，字符串text（文本）等同于字节串content（内容）再编码
print('\n------消息体----字节串----"b"开头（byte)----')
print(response_post3.content)
print('\n--------消息体---字节串decode为字符串-------')
print(response_post3.content.decode('utf-8'))






