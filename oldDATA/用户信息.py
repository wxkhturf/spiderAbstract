#https://blog.csdn.net/wp7xtj98/article/details/112711465
import requests
from bs4 import BeautifulSoup
import re
import json

# 请求头
gheaders = {
    'Referer': 'https://ieeexplore.ieee.org/search/searchresult.jsp? \
    newsearch=true&queryText=support',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:27.0) \
    Gecko/20100101 Firefox/27.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9, \
    image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive'
}
# 请求链接
url = 'https://ieeexplore.ieee.org/document/4537113'
IEEE_response = requests.get(url=url, headers=gheaders)     # GET请求
soup = BeautifulSoup(IEEE_response.text, 'lxml')            # 解析
# 正则表达式 创建模式对象
pattern = re.compile(r'xplGlobal.document.metadata=(.*?);', re.MULTILINE | re.DOTALL)
script = soup.find("script", text=pattern)                  # 根据模式对象进行搜索
res_dic = pattern.search(script.string).group(1)            # 配合search找到字典
#print(res_dic)
json_data = json.loads(res_dic)                             # 将json格式数据转换为字典
print(json_data['userInfo'])                                # 测试一下。。











