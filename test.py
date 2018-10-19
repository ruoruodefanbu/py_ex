from urllib import request, parse
import json

url = r'http://127.0.0.1:9090/act/model/list'
headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': r'http://127.0.0.1:9090',
    'Connection': 'keep-alive',
    'ticket': 'Qt5DKg783ogqIBXCWcGR5HMvOb2UVv+J0lAwT/CAHtIXB/Lyw5XFlbY3p2Da0I55PnU6c/yBIZBdabCJWhSVIx50IwZKVie5FVGJYzMo1/H5o/4x7ljJ233+pAAvFYpDv9ULhbbsbRndu0Jxm2a52KIAnw/wJr4+YZQAINFUzNA='
}
data = {
   'extendActBusinessId': 'dc2c625a139e4b05bd8ee33e1fe38a40',
   'page': 1,
   'pageSize': 10
}
data = parse.urlencode(data).encode('utf-8')
req = request.Request(url, headers=headers, data=data)
page = request.urlopen(req).read()
page = page.decode('utf-8')

hjson = json.loads(page)
lista=hjson["result"]["list"]
print(hjson["result"]["list"])

print(len(lista))

for i in lista:
    print(i["businessCategoryName"])


