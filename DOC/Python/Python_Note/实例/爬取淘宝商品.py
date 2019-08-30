# 目标：获取淘宝搜索页面的信息，提取其中的商品名称和价格
# 理解：淘宝的搜索接口、翻页的处理
# 技术路线：requests、re
# 爬虫可行性报告：https://www.taobao.com/robots.txt 限制所有爬虫

# 程序的结构设计
# 1、提交商品搜索请求，循环获取页面
# 2、对于每个页面，提取商品名称和价格信息
# 3、将信息输出到屏幕上 （扩展：键接和产品图片，价格，名称存在文件里）



import requests
import re

def getHTMLText(url):


def parsePage(list,html):

def printparsePage(list):

def main():
    infolist = []
    goods = '瑜伽袜子'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infolist,html)
        except:
            continue
        printparsePage(infolist)

main()



