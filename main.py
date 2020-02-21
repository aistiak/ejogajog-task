from dbManager import MyDB 
from newsManager import MyNews
config = {
    'db': 'tes2',
    'table': 'test',
    'user' : 'root',
    'password' : '',
}

db = MyDB(config)
news = MyNews()
# db.insert_news({'hash1':'news_link1','hash2':'news_link2'})
# print(db.get_hash_list())
print(db.get_all())