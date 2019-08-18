#!/usr/bin/env python3.4
# coding=utf-8

import urllib
import requests
import os
from bs4 import BeautifulSoup
    
class eBooks(object):
    """
        爬取电子书相关的变量和函数
    """

    def  __init__(self,name):

        self.chapterurls    = []
        search_url = 'https://www.biquguo.com/modules/article/search.php?searchkey=' + urllib.request.quote(name,encoding = 'gbk')
        #print(search_url)
        try:
            source = requests.get(url = search_url)
            html =  source.text.encode(source.encoding).decode(encoding='gbk',errors='ignore')
            bs   =  BeautifulSoup(html,"lxml")
            novelist = bs.select("#main > div.novelslistss > li > span.s2 > a")
            #print(novelist)
            for link in novelist:
                if name == link.text:
                   self.url = link.get("href")
                   print('find novle name : %s url: %s \n' %(name,self.url))
        except:
            print('error!!!!')
 
    
    
    def geturls(self):
        url  =  requests.get(url=self.url)
        html =  url.text.encode(url.encoding).decode(encoding='gbk',errors='ignore')
        #print(html)
        bs  =  BeautifulSoup(html,"lxml")
        a   =  bs.select("#list > dl > dd > a")
        for link  in a:
            self.chapterurls.append(link.get("href"))


    def downloaddata(self):
        count = 0;
        for url   in self.chapterurls:
            chapterurl =  self.url + url
            chapter = requests.get(url=chapterurl)
            html = chapter.text.encode(chapter.encoding).decode(encoding='gbk',errors='ignore')
            bs  =  BeautifulSoup(html,"lxml")
            name  = bs.select("#wrapper > div.content_read > div > div.bookname > h1")[0].text
            contents = bs.select("#content")
            count += 1
            print("当前下载章节名称:%s 下载进度: %0.2f %% 共 %d 章" % (name ,count/len(self.chapterurls)*100,len(self.chapterurls)))
            try:
                with open(name+'.txt',mode = "w") as f:
                    for content  in contents:
                        f.write(content.text+'\r\n')
            except:
                pass
    
def ebooktest():  
    book_name = input('请输入小说名字:\n')
    ebook   = eBooks(book_name)
    ebook.geturls()
    ebook.downloaddata()

if __name__ == '__main__':
    ebooktest()
    

