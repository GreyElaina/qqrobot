import requests
from mymain import *
URL = r'https://mc.meitangdehulu.com/message/mod_domain'

@myMain
def main(g,q,m):
    if not m:
        return '不能为空'
    params = {
        'domain': m,
        're':1
    }
    response = requests.get(url=URL,params=params).json()
    if response['status'] != 'ok':
        return '返回超时'
    if response['data'] == 'null':
        return '未找到该mod信息'
    names = getList(response['data']['detail']['language_files'], 'name')
    languages = getSupportLanguages(getList(response['data']['detail']['language_files'], 'language'))
    return 'mod名字:%s\nmod简介:%s\nmod版本:%s\nmod主页:%s\n语言文件夹名:%s\n支持语言:%s'%(
        response['data']['name'],
        response['data']['description'],
        response['version'],
        response['data']['href'],
        ' '.join(names),
        ' '.join(languages)
    )

def getSupportLanguages(items):
    L = []
    for item in items:
        if item.get('en_us',None):
            L.append('英文')
        if item.get('zh_cn',None):
            L.append('中文')
    return L

def getList(items,key):
    return [k[key] for k in items]