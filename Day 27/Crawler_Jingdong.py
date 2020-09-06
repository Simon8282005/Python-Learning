import requests as re  # 加载 requests 库
url = 'https://item.jd.com/2967929.html'  # 创建网站地址

# 通用代码框架
try:
    kv = {'user-agent':'Mozilla/5.0'}  # 创建一个浏览器的头部信息，将我们的爬虫伪装成一个浏览器，要不然会报错
    r = re.get(url,headers=kv)  # 使用假的头部信息覆盖掉默认的头部信息
    r.raise_for_status  # 检查是否有错误，如有就直接执行 except （status_code 方法有点像，但这个是报错的话就直接执行except，status_code只是输出状态码，并不会报错）
    r.encoding = r.apparent_encoding  # 没有错误的话，更改编码
    print(r.headers)  # 输出内容
except:
    print('Error')  # 输出 ‘Error’
