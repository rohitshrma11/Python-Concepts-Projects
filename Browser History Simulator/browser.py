from LRU_cache import LRUCache

class Browser:
    def __init__(self,history_limit):
        self.histroy = LRUCache(history_limit)
    def visit_page(self,url,title):
        print(f"\n Visiting {url}")
        self.histroy.put(url,title)
    def open_page(self,url):
        result =self.histroy.get(url)
        print(f"\n Opening {result}")
    def show_recent_tabs(self):
        self.histroy.show_history()
    def search(self,keyword):
        self.histroy.search_history(keyword)