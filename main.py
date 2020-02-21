from dbManager import MyDB 

config = {
    'db': 'tes2',
    'table': 'test',
    'user' : 'root',
    'password' : '',
}

db = MyDB(config)
print(config)