#_*_ coding:utf-8 _*_
import logging
from traceback import format_exc
from bs4 import BeautifulSoup
import requests
from config import headers,per_requests_time
from lxml import etree
import time,os


###html5lib 解析需要传入的字符串编码为：Unicode


##如果网页无法用html以及lxml解析，可以利用BeautifulSoup以html5lib为解析器进行putty之后，就好解析了


if __name__ =='__main__':
    
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        # filename=log_file,
                        # filemode='w'

                        ) 

class Root(object):

    def __init__(self,url,local=None):

        self.url=url
        self.local=local
        self.host=self.url.rsplit('/',1)[0]
        self.get_html()
        self.get_root()
        # self.get_soup()
        ##默认不开启soup
        


    def get_html(self,):

        if self.local:
            ##如果存在本地文件，就从本地文件读取html
            
            with open(self.local,'r')as f:
                self.html=f.read()

            self.url=self.local
          
            log=u'load html from localation=%s'%(self.local)
            logging.info(log)

        else:

            log=u'start requests to %s,then will sleep %s second!'%(self.url,per_requests_time)
            logging.info(log)
            self.html=requests.get(url=self.url,headers=headers,timeout=30).content
            time.sleep(per_requests_time)


    def get_root(self,):

        self.root=etree.HTML(self.html)



    def get_soup(self,):

        if not isinstance(self.html,unicode):
            html=self.html.decode('utf-8','ignore')
        else:
            html=self.html

        self.soup = BeautifulSoup(html, "lxml")
        return self.soup


        

    def tostring(self,element):
        ##解析的html最好为unicode编码，否则会乱码

        return etree.tostring(element)




