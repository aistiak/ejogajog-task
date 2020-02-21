# provide a dict of news_hashes and news_links
# if gives a hash_list will avoid links with with those hashes 
import requests 
import validators
from bs4 import BeautifulSoup

class MyNews :
    _main_dict = {} #dict
    _main_hash = []
    _dir_list   =  [ ] 
    _URL = "http://www.prothomalo.com"
    def __init__(self,url):
        pass 

    def get_news(url,depth):
    print("recursion depth",depth)
    # check if url is valid and contains  prthom alos url if not return 
    if validators.url(url) == True and "www.prothomalo.com" in url :
        pass 
    elif  validators.url(URL+url) == True:
        url = URL+url
        pass  
    else :
        print("abort dir url...")
        return 
    
    # cheack url alreay exista in hash_list 
    if url in main_hash :
        return 
    else :
        h = str(hash(url))
        main_hash.append(h)
    try :
        response = requests.get(url = url) 
    except :
        return 
    data = BeautifulSoup(response.text)
    anchors = data.findAll('a',href=True)
    for anchor in anchors :
        if "class" in anchor.attrs:
            if "link_overlay" in anchor["class"]:
                t_url = URL + anchor.attrs["href"] 
                h = str(hash(t_url))
                main_dict[h] = t_url
                if h not in main_hash:
                    main_hash.append(h) 
        else :
            # if dir url recursive call 
            h = str(hash(anchor["href"]))
            if h in main_hash:
                pass
            else :
                main_hash.append(h)
                print(anchor["href"])
                get_news(anchor["href"],depth+1)
            
    return "" 