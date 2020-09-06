import requests as re

keyword='Python'
try:
    kv = {'q':keyword}
    r = re.get("http://www.so.com/s", params = kv)
    print('URL: ',r.url)
    print(len(r.text))
except:
    print('Error')
