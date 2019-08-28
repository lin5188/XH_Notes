#e24.1 CrawUnivRanking.py
'''
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(allUniv,html):
    soup = BeautifulSoup(html,"html.parser")  # 解析器中间有.
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            allUniv.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string]) # 添加列表，别忘了[]

def printUnivList(allUniv,num):
    tplt = "{1:^4}\t{2:{0}^10}\t{3:^10}\t{4:^10}"
    print(tplt.format(chr(12288),"排名","学校名称","省市","总分")) # 调取format前面是点.
    for i in range(num):  # for...in range()是固定搭配，别忘了range()
        u = allUniv[i]  # []表示
        print(tplt.format(chr(12288),u[0],u[1],u[2],u[3]))

def main():
    allUniv = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html"
    html = getHTMLText(url)
    fillUnivList(allUniv,html)
    printUnivList(allUniv,10)


main()
'''

# 爬取中国大学排名 （静态网页爬虫）
import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):  # 将url信息从网络中爬取下来，把内容返回给函数
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):  # 提取HTML关键的数据，填写到一个列表中
    soup = BeautifulSoup(html, "html.parser")  # 解析器中间有个点.
    for tr in soup.find('tbody').children:  # 在tbody的子节点中找到所以tr标签
        if isinstance(tr, bs4.element.Tag):  # 如果tr是bs4库中识别的标签类型
            tds = tr('td')  # 查找tr标签中的td标签，并存入tds中
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])  # 将找到的td信息存入列表中，添加列表，别忘了[]


def printUnivList(ulish, num):  # 打印大学排名列表，居中输出
    tplt = "{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}"  # 模板宽度设定(居中显示），其中{4}表示宽度不够时，使用format函数中对应第3的位置填充中文空格
    print(tplt.format("排名", "学校", "省份", "总分", chr(12288)))  # 格式化输出三列表格的表头信息，宽度不够时填充中文空格的变量位置，调取format前面是点.
    for i in range(num):  # 使用for循环来打印学校排名的其他信息，for...in range()是固定搭配，别忘了range()
        u = ulish[i]
        print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))


def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 30)  # 打印前20名大学


main()