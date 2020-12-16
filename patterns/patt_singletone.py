class DataBase:
    pass


# import MySQLdb as mysql
import pymysql.cursors
import pymysql
import sys
from configparser import ConfigParser


class DB:
    link = False

    @classmethod
    def setConnection(cls):
        config = ConfigParser()
        config.read("python/configs/config.ini")

        cls.link = pymysql.connect(
            host=config.get('DB', 'host'), user=config.get('DB', 'user'),
            password=config.get('DB', 'pass'), db=config.get('DB', 'name'),
            use_unicode=True, charset="utf8", cursorclass=pymysql.cursors.DictCursor
        )
        cls.cursor = cls.link.cursor()

    @classmethod
    def reconnect(cls):
        if cls.link == False:
            cls.setConnection()
            return
        cls.link.close()
        cls.link = False
        cls.setConnection()

    @classmethod
    def getByStatus(cls, table, limit=None, offset=0, status=None):
        if cls.link == False:
            cls.setConnection()
        cls.link.rollback()
        if status is None:
            status = "=0"
        else:
            status = "=" + str(status)
        if limit is None:
            cls.cursor.execute("""SELECT * FROM {table} WHERE parse_status {status}""".format(table=table, status=status), {
                'status': status
            })
        else:
            cls.cursor.execute("""
            SELECT * FROM {table} WHERE parse_status {status}
            LIMIT {o}, {l}
            """.format(table=table, l=limit, o=offset, status=status))
        return cls.cursor.fetchall()

    @staticmethod
    def something():
        DB.update_link_status()

    @classmethod
    def someclsmethod(cls):
        cls.update_link_status()

    @classmethod
    def update_link_status(cls, table, item):
        if cls.link == False:
            cls.setConnection()
        cls.cursor.execute("""
            UPDATE {table} SET parse_status=%(parse_status)s
            WHERE id=%(id)s
        """.format(table=table), {
            "parse_status": item.get("parse_status"),
            "id": item.get("id")
        })
        cls.link.commit()


DB.setConnection()


from typing import List


class Singletone:
    _table: List[list] = None
    _size: int = 0

    @classmethod
    def set_size(cls, size):
        cls._size = size

    @classmethod
    def generate_table(cls):
        # use somehow cls._size
        cls._table = [[]]

    @classmethod
    def get_table(cls):
        if not cls._table:
            cls.generate_table()

        return cls._table

    @classmethod
    def insert_value(cls, value, pos_x, pos_y):
        ...
        return cls._table


class A:
    def __init__(self, size):
        Singletone.set_size(size)
        Singletone.generate_table()

    def m1(self):
        Singletone.insert_value(1, 2, 3)


class B:
    def m2(self):
        return Singletone.get_table()


a = A(size=5)

b = B()
print(b.m2())
