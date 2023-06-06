import requests
import re
def Web(url,headers):
    # 要爬取的url，注意：在开发者工具中，这个url指的是第一个url
    r = requests.get(url=url,headers=headers)
    print(r.status_code)
    #print(r.text)
    all_lines = r.text;
    all_lines = all_lines.split('\n', -1 );
    return all_lines

def GetAbstract(all_lines):
    line = ''
    for i in all_lines:
        ret = re.match('.*<meta property="twitter:description.*/>', str(i))
        if(ret):
            i = i.split('content="',1)
            i = i[1]
            i = i.split('" />',1)
            i = i[0]
            print(str(i))
            line = i
            break
    return line


if __name__ == "__main__":
    #url = "https://ieeexplore.ieee.org/document/9509281"
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    #all_lines = Web(url,headers)
    #line = GetAbstract(all_lines)
    #with open('gg.txt','w') as wf:
        #wf.write(line)
    url = 'https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=kyber'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    all = Web(url,headers)
    #all = GetAbstract(all)
    with open('gg.txt','w') as wf:
        for i in all:
            wf.write(i)
    wf.close()








