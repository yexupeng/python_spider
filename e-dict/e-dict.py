#!/usr/bin/env python3.4
# coding=utf-8

import  requests 

"""
    有道词典翻译
"""

class eDict(object):
    def __init__(self,url):
        """
            data数据以及url初始化
        """
        self.url    = url 
        self.data  = {
            'from':'AUTO',
            'to'  :'AUTO',
            'smartresult':'dict',
            'client':'fanyideskweb',
            'doctype':'json',
            'vesrion':'2.1',
            'keyfrom':'fanyi.web',
            'action':'FY_BY_CLICKBUTTON',
            'typoResult':'false'
        }



    def translate(self,content):
        """
            显示待翻译的句子,获取结果后,显示翻译结果
        """
        print('content: %s' %content)
        self.data['i'] = content
        rsp = requests.post(self.url,data=self.data)
        print('result: %s' %rsp.json()['translateResult'][0][0]['tgt'])



def eDict_test():
    url  = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule' 
    dict = eDict(url)
    while True:
        str = input('请输入要翻译的内容:\n')
        if str == 'q':
            print('再见,期待下一次相遇')
            break
        dict.translate(str)
    

if __name__ == '__main__':
    eDict_test();
