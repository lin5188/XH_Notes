# 利用SQL分析电商平台在线零售业务

背景
--


数据来源
--
该数据来源  [kaggle](https://www.kaggle.com/carrie1/ecommerce-data)

数据信息
--
本段数据集为：4198746 * 8列

InvoiceNo：发票号，每笔交易产生一个6位编码，退货订单的编码以C开头的7位编码

StockCode：产品代码，每个产品都有自己的编码

Description：产品描述

Quantity：数量，每次交易产品的数量

InvoiceDate：发票日期，每笔交易产生的时间

UnitPrice：商品单价，单位英镑

CustomerID：消费者编码，每个客户都为5位编码

Country：国家名字，消费者所在国家/地区的名字

提出问题
---
* 一共有多少客户，客户分别来自哪些国家，哪个国家客户最多

* 一共有多少订单，订单分别来自哪些国家，哪个国家订单最多

* 哪个国家的销售额最高

* 最畅销的商品是哪些，以及销售最高的是哪个商品

* 哪个月的销售额最高

* 退货率最高的商品

* 哪个国家的退货率最高

清洗数据
---
### 原始数据

![1](https://github.com/lin5188/XH_Notes/blob/master/DOC/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/%E6%A1%88%E4%BE%8B%E5%88%86%E6%9E%90/%E9%9B%B6%E5%94%AE/SQL/1.png)

