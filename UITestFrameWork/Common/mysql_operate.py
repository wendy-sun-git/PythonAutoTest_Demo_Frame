#!/usr/bin/python3
# -*- coding=utf-8 -*-


import mysql.connector as sql


class MysqlDb(object):
    """
        example:
        with MysqlDb() as db:
            rt = db.query(sql, params=())
    """

    def __init__(self, host, port, user, pwd, log):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.log = log

        self.conn = sql.connect(host=self.host, port=self.port,
                                user=self.user, passwd=self.pwd)
        self.cursor = self.conn.cursor(dictionary=True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()
        if exc_tb:
            self.log.error("error: ".format(str(exc_val)))

    def close(self):
        self.cursor.close()
        self.conn.close()

    def query(self, sqlcmd, params=()):
        rv = None
        cursor = self.cursor
        try:
            cursor.execute(sqlcmd, params)
            rv = cursor.fetchall()
        except Exception as err:
            self.log.error('query error: {}'.format(str(err)))
            print(str(err))
        return rv

    def operator(self, sqlcmd, log, params=()):
        rv = False
        cursor = self.cursor()
        try:
            cursor.execute(sqlcmd, params)
            self.conn.commit()
            rv = True
        except Exception as err:
            self.log.error('query error: {}'.format(str(err)))
            print(str(err))
        return rv

