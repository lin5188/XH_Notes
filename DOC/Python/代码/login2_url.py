import requests

url = "http://www.renren.com/361753555/profile"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

cookie = "anonymid=k0cekkqv1ns2kz; depovince=SD; _r01_=1; JSESSIONID=abcBCgNH9Gp6yfeqIew0w; radius=10.148.132.42; ick_login=cafcf2ae-129a-4f01-a786-5ef1da9451af; uudid=cmsebe7272d-83e1-6273-427b-f397e50050f5; badu=idu; ick=ceb59552-70fe-4762-82ae-65a5efdb7912; __utma=151146938.1447282961.1568033483.1568033483.1568033483.1; __utmc=151146938; __utmz=151146938.1568033483.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; _de=713DFE3E24674F911AEC91B82326F40E34DF20B0B3AA6FF7; first_login_flag=1; ln_uact=userlixuhui@163.com; ln_hurl=http://head.xiaonei.com/photos/0/0/women_main.gif; id=361753555; jebecookies=972e3244-3c02-42e6-8809-e5b164285e25|||||; p=ff2d7788597f78d4a5d4a2359407a3a15; t=ad6819b5a195ea57e59368a3af05e49e5; societyguester=ad6819b5a195ea57e59368a3af05e49e5; xnsid=e9e731ea; __utmb=151146938.10.10.1568033483; jebe_key=e9a60bdf-fdb2-4eda-947d-8ef96b2e0588%7Cac28337071be67407b88c59f384e9770%7C1568033869884%7C1%7C1568033872154; jebe_key=e9a60bdf-fdb2-4eda-947d-8ef96b2e0588%7Cac28337071be67407b88c59f384e9770%7C1568033869884%7C1%7C1568033872157; wp_fold=0; ver=7.0; loginfrom=null"

cookie_dick = {i.split("=")[0]:i.split("=")[-1] for i in cookie.split("; ")} # 把cookie字符串分离成键子对。

# print(cookie_dick)

response = requests.get(url,headers=headers,cookies=cookie_dick)

with open("renren2.html",'w',encoding="utf-8") as f:
    f.write(response.content.decode())
