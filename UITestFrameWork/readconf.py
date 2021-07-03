# _*_coding:utf-8 _*_

import os
import codecs
import configparser

prodir=os.path.dirname(os.path.abspath(__file__))
conf_prodir=os.path.join(prodir, 'conf.ini')

'''
https://blog.csdn.net/songlh1234/article/details/83316468 
'''


class ReadConf:
    cf =configparser.ConfigParser()

    def readcf(self):
        with open(conf_prodir) as fd:
            data=fd.read()
            # 清空文件信息
            if data[:3] == codecs.BOM_UTF8:
                data=data[3:]
                file=codecs.open(conf_prodir, 'w')
                file.write(data)
                file.close()
        self.cf.read(conf_prodir)

    @classmethod
    def get_browser(cls, name):
        cls().readcf()
        return cls.cf.get("browser", name)

    @classmethod
    def get_db(cls, name):
        cls().readcf()
        return cls.cf.get("mysqldb", name)

    @classmethod
    def get_report(cls, name):
        cls().readcf()
        return cls.cf.get("report", name)

    @classmethod
    def get_url(cls, name):
        cls().readcf()
        return cls.cf.get("url", name)


if __name__ == '__main__':
    print(ReadConf.get_browser('name'))
    print(ReadConf.get_db('db'))
    print(ReadConf.get_report('report_title'))
    print(ReadConf.get_url('lian_jia_url'))
