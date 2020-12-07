# hash function to hash a string
def hash(s, length):
    hash_key = 0
    for char in s:
        character_code = ord(char)
        hash_key += character_code
    return hash_key % length

# hash table class
class HashTable:
    def __init__(self):
        self.num_containers = 1
        self.containers = [[] for i in range(self.num_containers)]
        self.num_elements = 0

    def insert(self, key, value):
        hash_value = hash(key, self.num_containers)
        container = self.containers[hash_value]
        for pair in container:
            if pair[0] == key:
                return

        container.append([key, value])
        self.num_elements += 1
        load_factor = self.num_elements / self.num_containers

        if load_factor > 0.8:
            self.resize(self.num_containers * 2)

    def search(self, key):
        hash_value = hash(key, self.num_containers)
        bucket = self.containers[hash_value]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]

        return None

    def delete(self, key):
        hash_value = hash(key, self.num_containers)
        bucket = self.containers[hash_value]

        for pair in bucket:
            if pair[0] == key:
                bucket.remove(pair)
                return pair[1]

        return None

    def resize(self, new_size):
        new_containers = [[] for i in range(new_size)]
        for container in self.containers:
            if len(container) > 0:
                for pair in container:
                    new_hash_value = hash(pair[0], new_size)
                    new_containers[new_hash_value].append(pair)
        self.num_containers = new_size
        self.containers = new_containers


h = HashTable()
h.insert("name", "bob")
h.insert("age", 30)
h.insert("colour", "blue")
h.insert("height", "180cm")
h.insert("weight", "70kg")
h.insert("job", "software developer")
h.insert("salary", "400k")
h.insert("location", "toronto")
