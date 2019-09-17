import requests
import json
from parse_URLText import parse_url


class DoubanSpider:

    def __init__(self):
        self.temp_url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288&_=0"

    def getURLList(self, html_str):  # 提取数据
        dict_data = json.loads(html_str)
        url_list = dict_data["subject_collection_items"]
        total = dict_data["total"]
        return url_list, total

    def saveURLList(self, url_list): # 保存数据
        with open("douban_em.txt", "a", encoding="utf-8") as f:
            for content in url_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
        print("保存成功")

    def run(self):  # 实现主要逻辑
        num = 0 #通过网页分析，初始为0，步进为18
        total = 45
        while num < total + 18:
            # 1.starte_url
            url = self.temp_url.format(num)
            print(url)
            # 2.发送请求，获取响应内容
            html_str = parse_url(url)

            # 3.提取数据
            url_list, total = self.getURLList(html_str)

            # 4.保存
            self.saveURLList(url_list)

            # 5.构造下一页的url地址，循环第2-5步
            num += 18


if __name__ == "__main__":
    douban = DoubanSpider()
    douban.run()