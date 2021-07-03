#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis


class RedisOperate:
    '''
        redis执行器
    '''
    def __init__(self, host, port, db, pwd):
        self.host = host
        self.port = port
        self.db = db
        self.pwd = pwd

        self.redis = redis.Redis(
            host=self.host, port=self.port, db=db, password=self.pwd)

    def get(self, key):
        '''
        获取redis的key值
        :param key:
        :return:
        '''
        return str(self.redis.get(key), encoding="utf-8")

    def set(self, key, value, ex=None, px=None, nx=None, xx=None):
        '''
        设置redis的key值,可设置过期时间
        :param key:
        :param value:
        :param ex:
        :param px:
        :param nx:
        :param xx:
        :return:
        '''
        self.redis.set(key, value, ex, px, nx, xx)


if __name__ == '__main__':
    print(RedisOperate(0).get("name"))
    RedisOperate(1).set("name", "baba")
