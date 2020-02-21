import mysql.connector as mysql

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
                             " (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,news_hash VARCHAR(255), news_link VARCHAR(255))")

        # pass 

    def get_hash_list(self):
        pass
    def insert_news(self):
        pass
