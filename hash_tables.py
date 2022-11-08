class HashTable:
    def __init__(self,size=7):
        self.data_map=[None] * size

    def __hash(self,key):
        my_hash=0
        for item in key:
            my_hash = (my_hash + ord(item)*23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, item in enumerate(self.data_map):
            print(i, ": ", item)

    def set_item(self,key,value):
        i=self.__hash(key)
        if self.data_map[i] is None:
            self.data_map[i] = []
        self.data_map[i].append ([key,value])

    def get_item(self,key):
        i=self.__hash(key)
        if self.data_map[i]:
            for item in self.data_map[i]:
                if item[0] == key: return item[1]
        return None

    def keys(self):
        result=[]
        for item in self.data_map:
            if item:
                for i in item:
                    result.append(i[0])
        return result




my_ht=HashTable()
my_ht.set_item("bolts",7)
my_ht.set_item("washers", 10)
my_ht.set_item("nails", 20)
my_ht.set_item("hammers", 30)
my_ht.set_item("lumber", 40)
my_ht.print_table()
print(my_ht.keys())