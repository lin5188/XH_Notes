SQLZOO答案
===

## 一
***
> ![][1] __*SELECT  BASICS*__
---
1 . 
```Mysql
SELECT population FROM world
    WHERE name = 'Germany';
```

2 . 
```Mysql
SELECT name,population FROM world
    WHERE name in ('Sweden','Norway',Denmark');
```

3 .
```Mysal
SELECT name,area FROM world
    WHERE area BETWEEN 200000 AND 250000;
```
---
> ![][1] __*quiz*__  
---
1 .
```Mysaql
SELECT name,population FROM world
    WHERE population BETWEEN 1000000 AND 1250000;
```

2 .
Table-E

|Albania|3200000
|---|---
|Algeria|32900000

3 .
```Mysql
SELECT name FROM world
    WHERE name LIKE '%a' OR name LIKE '%l';
```
4 .

|name|length(name)
|:---:|---:
|Italy|5
|Malta|5
Spain|5

5 .

|Andorra|936
|---|---

6 .
```Mysql
SELECT name,area,population FROM world
    WHERE area > 50000 AND population < 10000000;
```

7 .
```Mysql
SELECT name,population/area FROM world
    WHERE name in ('China','Nigeria','France','Australia');
```

## 二
___
> ![][1] __*SELECT FROM WORLD*__
___

1 .








[1]:
https://github.com/lin5188/XH_Notes/blob/master/DOC/others/icons/%E6%B0%B4%E6%9E%9Cicon/%E8%8B%B9%E6%9E%9C.png