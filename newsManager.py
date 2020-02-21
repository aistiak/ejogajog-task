# provide a dict of news_hashes and news_links
# if gives a hash_list will avoid links with with those hashes
import requests
import validators
from bs4 import BeautifulSoup


class MyNews:
    _main_dict = {}  # dict
    _main_hash = []
    _target_class = '' #'link_overlay'
    # dir_list = []
    _URL = '' #"http://www.prothomalo.com"
    _must_contain = '' #"www.prothomalo.com"

    def __init__(self ,base_url,hash_list,must_contain,target_class):
        self._URL = base_url
        self._main_hash = hash_list
        self._must_contain = must_contain 
        self._target_class = target_class

        # pass


    def get_news_dict(self):
        return self._main_dict 
    
    def get_news_hash_list(self):
        return self._main_hash 

    # def set_news_hash_list(self,hash_list=[]):
    #     return self._main_hash = hash_list        


    def fetch_news(self, url, depth=0):
        print("recursion depth", depth)
        if depth > 2 :
            return 
        # check if url is valid and contains  prthom alos url if not return
        if validators.url(url) == True and self._must_contain in url:
            pass
        elif validators.url(self._URL+url) == True:
            url = self._URL+url
            pass
        else:
            print("abort dir url...")
            return

        # cheack url alreay exista in hash_list
        if url in self._main_hash:
            return
        else:
            h = str(hash(url))
            self._main_hash.append(h)
        
        try:
            response = requests.get(url=url)
        except:
            return
        
        data = BeautifulSoup(response.text)
        anchors = data.findAll('a', href=True)

        for anchor in anchors:
            if "class" in anchor.attrs:
                if  self._target_class in anchor["class"]:
                    t_url = self._URL + anchor.attrs["href"]
                    h = str(hash(t_url))
                    self._main_dict[h] = t_url
                    if h not in self._main_hash:
                        self._main_hash.append(h)
            else:
                # if dir url recursive call
                h = str(hash(anchor["href"]))
                if h in self._main_hash:
                    pass
                else:
                    self._main_hash.append(h)
                    print(anchor["href"])
                    self.fetch_news(anchor["href"], depth+1)

        return ""
