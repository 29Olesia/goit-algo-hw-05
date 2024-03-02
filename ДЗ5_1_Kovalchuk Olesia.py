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
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    break
            else:
                self.table[key_hash].append(key_value)

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
            for i, pair in enumerate(self.table[key_hash]):
                if pair[0] == key:
                    del self.table[key_hash][i]
                    break


if __name__ == "__main__":
    H = HashTable(5)
    H.insert("яблуко", 10)
    H.insert("апельсин", 20)
    H.insert("банан", 30)

    print("Перед видаленням 'апельсин':")
    print(H.get("апельсин"))  # Вивід: 20

    H.delete("апельсин")  # Видаляємо ключ 

    print("\nПісля видалення 'апельсин':")
    print(H.get("апельсин"))  # Вивід: None, оскільки "апельсин" було видалено
