class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for index in range(len(self.table[key_hash])):
                if self.table[key_hash][index][0] == key:
                    self.table[key_hash].pop(index)
                    print(f'Чи був видалений елемент "{key}":')
                    return True
        print(f'Чи був видалений елемент "{key}":')
        return False


# Тестуємо нашу хеш-таблицю:
H = HashTable(3)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)
H.insert("kiwi", 40)
H.insert("mango", 50)
H.insert("malon", 60)

print(H.table)
print(H.get("apple"))   
print(H.get("orange"))  
print(H.get("banana")) 

print(H.delete("mango")) 
print(H.delete("malon")) 
print(H.delete("watermalon"))

print(H.table)