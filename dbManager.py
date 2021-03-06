# connectos to MySql Database 
# creates Database and Table if already not there 
# adds records to table in news_hash and news_link fields
# return hash_list 
# get all data  

# import pymysql as mysql
# import MySQLdb as mysql
import mysql.connector as mysql
import re 

class MyDB :
    _db = ''
    _cursor = ''
    _db_name     =  ''
    _table  =  ''
    _user   =  ''
    _pass   =  ''
    _host   =  '' 
    def __init__(self,config,host="localhost"):
        self._db_name = config['db']
        self._table   = config['table']
        self._user    = config['user']
        self._pass    = config['password']
        self._host    = host
        self._db      = mysql.connect(
            host      = self._host,
            user      = self._user,
            passwd    = self._pass,
            # database  = self._db_name, 
        )
        self._cursor = self._db.cursor()

        # crate DB if not exists 
        self._cursor.execute("CREATE DATABASE IF NOT EXISTS " + self._db_name)
        self._cursor.execute("use " + self._db_name)
        # create table if not exist 
        self._cursor.execute("CREATE TABLE IF NOT EXISTS " + self._table + 
                             " (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,news_hash VARCHAR(255), news_link VARCHAR(50000), category VARCHAR(300))")

        # pass 

    def get_hash_list(self):
        query = "SELECT news_hash FROM " + self._table
        self._cursor.execute(query)
        records = self._cursor.fetchall()
        ret = []
        for v in records:
            ret.append( list(v)[0] )
        return ret
        # pass


    def get_all(self):
        query = "SELECT news_hash , news_link FROM " + self._table 
        self._cursor.execute(query)
        records = self._cursor.fetchall()
        ret = {} 
        for v in records :
            ret[v[0]] = v[1]
        return ret     

    def get_category(self,link):
        r = re.findall("[/][a-zA-Z]{1,20}[/]",link)
        if len(r) > 0 :
            r = r[0]
            r = r[1:]
            r = r[:-1]
            return r 
        return ""


    def insert_news(self,news_dict={}):
        keys = list(news_dict.keys())
        records = []
        for key in keys :
            category = self.get_category(news_dict[key])
            t = (key,news_dict[key],category)
            records.append(t)
        query = "INSERT INTO " + self._table + " (news_hash, news_link, category) VALUES (%s, %s, %s)"   
        self._cursor.executemany(query, records) 
        self._db.commit()
        # pass

    # def insert_single_news(self,news_dict={})