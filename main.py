from dbManager import MyDB 
from newsManager import MyNews
config = {
    'db': 'tes2',
    'table': 'prothom_alo',
    'user' : 'root',
    'password' : '',
}

db = MyDB(config)
base_url  ="http://www.prothomalo.com"
hash_list = db.get_hash_list() 


news = MyNews(base_url      =base_url,
              hash_list     =hash_list,
              must_contain  ="www.prothomalo.com",
              target_class  ="link_overlay")

news.fetch_news(base_url) # hear base url is the enry point 

db.insert_news(news.get_news_dict())
# db.insert_news({'hash1':'news_link1','hash2':'news_link2'})
# print(db.get_hash_list())
# print(db.get_all())

