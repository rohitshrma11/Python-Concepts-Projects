from collections import OrderedDict
class LRUCache:
    def __init__(self,capacity):
        self.capcity= capacity
        self.cache=OrderedDict()

    def get(self,url):
        if url not in self.cache:
            return "Page Not Found"
        self.cache.move_to_end(url)
        return self.cache[url]

    def put(self,url, page_data):
        if url in self.cache:
            self.cache.move_to_end(url)
        self.cache[url]=page_data
        if len(self.cache)>self.capcity:
            removed =self.cache.popitem(last=False)
            print(f"Removed Oldest page: {removed[0]}")

    def show_history(self):
        print("\n Print the recent history")
        for url,data in reversed(self.cache.items()):
            print(f"{url}-> {data}")

    def search_history(self, keyword):
        print("\n Searching Browser History")
        found =True
        for url in self.cache:
            if keyword.lower() in url.lower():
                print(url)
                found =True
        if not found:
            print('No Matching found history')
            