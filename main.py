from dbManager import MyDB 

config = {
    'db': 'tes2',
    'table': 'test',
    'user' : 'root',
    'password' : '',
}

db = MyDB(config)
# db.insert_news({'hash1':'news_link1','hash2':'news_link2'})
# print(db.get_hash_list())
print(db.get_all())