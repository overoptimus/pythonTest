#coding:utf-8

import re
import requests
import urllib
# import urllib2
import bs4
from bs4 import BeautifulSoup

key=input("please input top domain: ")

print("查询马上开始...")
title=[]
domainlist=[]
for n in range(1,66):
    if n!=1:
        n*=10
    url="https://cn.bing.com/search?q=domain:"+key+"&first=%s" % n
    try:
        # req=urllib2.Request(url)
        # resp=urllib2.urlopen(req).read()
        resp = requests.get(url)
        #BeautifulSoup匹配标题
        bsObj = BeautifulSoup(resp.text,"lxml")
        getList = bsObj.find_all("h2",{"class":""})
        for t in getList:
            title.append(t.get_text())
        #正则匹配子域名
        regex=re.compile('<cite>(.*?)</cite>').findall(resp)
        for i in regex:
            domainlist.append(i.strip('https://').strip('http://').split('/')[0])
        #同步输出查询到的标题和子域名
        for (i,j) in zip(title,domainlist):
            print("%50s%30s" % (i,j))
    except Exception as e:
        print(e)
print("查询已全部完成...")
#去掉重复的子域名
domainlists=list(set(domainlist))
#保存子域名
for line in domainlists:
    with open('subdomain.txt','a') as fw:
        fw.write(line+'\n')
