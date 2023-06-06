#https://blog.csdn.net/int888888/article/details/107231549
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
 
import json
import time
#保存信息函数
def write_to_file(Abstract):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(Abstract, ensure_ascii=False) + '\n')
 
#任务：爬取2页或多页指定URL的文章摘要
def main(pageNumber):
    browser = webdriver.Chrome()
    browser.implicitly_wait(200)#这是延时等待。由于网速时快时慢，而get方法会在网页框架加载结束后停止执行，
    #这就会导致有些时候我们打算获取的内容还没被加载进来便结束了获取页面数据，最后报错，拿不到想要的数据。
    url = 'https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=kyber&highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&pageNumber='+str(pageNumber)
    browser.get(url)
    #遇到class name中的复合情况（即有多个class name中间是空格隔开的）
    #选取其中一个具有全局唯一性的class name即可准确定位所要查找的结点内容
    AbstractList = browser.find_elements(By.CLASS_NAME, 'stats-SearchResults_DocResult_ViewMore')
    for Abstract in AbstractList:
        #对于需要点击才显示出来的页面内容（隐藏内容）需要使用下面的方法获取文本信息
        result = browser.execute_script("return arguments[0].textContent", Abstract)
        print(result)
        write_to_file(result)#写入文本文件进行保存
 
if __name__ == "__main__":
    for i in range(2):
        j = i + 1
        main(pageNumber = j)
        #time.sleep(1)#有些网站有反爬虫机制，如果访问间隔时间很短则不会响应。