# HashTable that uses chaining
class HashTable:
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

     # Inserts a new item into the hash table.
    def insert(self, key, item): #  does both insert and update 
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
 
        # update key if it is already in the bucket
        for kv in bucket_list:
          #print (key_value)
          if kv[0] == key:
            kv[1] = item
            return True
        
        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True
 
    # The search function is used to lookup items from the hash table
    def search(self, search_key):
        # Determine the bucket index where the search_key would be located.
        bucket_index = hash(search_key) % len(self.table)
        bucket_list = self.table[bucket_index]

        # Search for the search_key in the bucket list.
        for key_value_pair in bucket_list:
            if key_value_pair[0] == search_key:
                return key_value_pair[1]  # Return the corresponding value
        return None

    # Removes an item with a matching key from the hash table.
    def remove(self, key_to_remove):
        # Determine the bucket index where the item with key_to_remove will be removed from.
        bucket_index = hash(key_to_remove) % len(self.table)
        bucket_list = self.table[bucket_index]

        # Remove the item from the bucket list if it is present.
        for key_value_pair in bucket_list:
            if key_value_pair[0] == key_to_remove:
                bucket_list.remove([key_value_pair[0], key_value_pair[1]])
