def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()

    
class LRU():
    def __init__():
        self.hastable = {}
        self.cache = {}
        # sorted by frequencecy store tupes (item, time)
        self.lru = []

    def __touch(self, item, key):
        if item in self.hashtable:
            lru_node = hashtable[key]
            self.lru.remove(lru_node) # O( NLnN)
        lru_node = self.lru.insert(key, item)
        self.hashtable[key] = lru_node
        
    def __remove(self):
        if len(self.lru) < MAX_LEN:
            return       
        item, key = self.lru[len(self.lru)-1]
        del(self.hashtable, item)
        del(self.cache, key)
        self.lru = self.lru[:len(self.lru)-2]
        
    def put(self, key, item):
        self.touch(item, key)
        self.cache[key] = item
        self.__remove()

    def get(item):
        if key in self.cache:
            item = self.cache[key]
            self.touch(item, key)
            return item
        else:
            return None
    
    



# 
# Your previous Java content is preserved below:
# 
# /*
#  * Click `Run` to execute the snippet below!
#  */
# 
# import java.io.*;
# import java.util.*;
# 
# /*
#  * To execute Java, please define "static void main" on a class
#  * named Solution.
#  *
#  * If you need more classes, simply define them inline.
#  */
# /*
# 
#  LRU Cache
# 
#  Store up to n items
# 
#  String get(int id)
#  void put(int id, String name)
# 
# example n=3
# 
#  cache.put(1, "John")
#  cache.put(2, "Paul")
#  cache.put(3, "George")
#  cache.put(4, "Ringo")
#  When we insert (4, “Ringo”) the LRU is (1,”John”), and therefore it should be removed.
# 
#  cache.put(1, "John")
#  cache.put(2, "Paul")
#  cache.get(1)
#  cache.put(3, "George")
#  cache.put(4, "Ringo")
#  When we insert (4, “Ringo”) the LRU is (2,”Paul”), and therefore it should be removed.
# */
# 
# class Solution {
#   public static void main(String[] args) {
#     ArrayList<String> strings = new ArrayList<String>();
#     strings.add("Hello, World!");
#     strings.add("Welcome to CoderPad.");
#     strings.add("This pad is running Java " + Runtime.version().feature());
# 
#     for (String string : strings) {
#       System.out.println(string);
#     }
#   }
# }
# 
