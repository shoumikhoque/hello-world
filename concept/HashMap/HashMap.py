from concept.HashMap.HashEntry import HashEntry


class HashMap:
    def __init__(self):
        # total slots or size of the actual hashtable
        self.slots=10
        #current entries in the table
        #needed for resizing the table when threshold has exceeded
        self.size=0
        self.bucket=[None]*self.slots
        self.threshold=0.6

    def get_size(self):
        return self.size
    def is_empty(self):
        return self.size == 0
    def get_index(self,key):
        return hash(key)%self.slots
    def change_threshold(self,new_threshold_value):
        self.threshold=new_threshold_value
    def resize(self):
        #resize the bucket and copy the existing values in new bucket
        self.slots=self.slots*2
        new_bucket=[None]*self.slots
        for item in self.bucket:
            head=item
            while head is not None:
                new_index=self.get(head.key)
                if new_bucket[new_index] is None:
                    new_bucket[new_index]=HashEntry(head.key,head.value)
                else:
                    node=new_bucket[new_index]
                    while node is not None:
                        if node.key == head.key:
                            node.value=head.value
                            node=None
                        elif node.nxt is None:
                            node.nxt
    def put(self,key,value):
        #insert a key,value pair
        key_index=self.get_index(key)
        if self.bucket[key_index] is None:
            #insert new head for key_index
            self.bucket[key_index]=HashEntry(key,value)
            self.size+=1
        else:
            # insert new key value at the end of the linkedList
            head=self.bucket[key_index]
            while head is not None:
                if head.key is key:
                    head.value=value
                    break
                elif head.nxt is None:
                    head.nxt=HashEntry(key,value)
                    self.size+=1
                    break
                head=head.nxt
        if float(self.size)/(self.slots)>= self.threshold:
            self.resize()

    def get(self,key):
        #return a key,value pair for a key
        key_index=self.get_index(key)
        head=self.bucket[key_index]
        while head is not None:
            if head.key==key:
                return head.value
            head=head.nxt
        return None
    def delete(self,key):
        # delete a key
        key_index=self.get_index(key)
        head=self.bucket[key_index]
        # if key exists at first slot
        if head.key is key:
            self.bucket[key_index]=head.next
            self.size-=1
            return self
        # if key exists in inner slot
        prev=head
        head=head.nxt
        while head is not None:
            #if key exists
            if head.key is key:
                prev.nxt=head.nxt
                self.size-=1
                return
            prev = head
            head=head.nxt


        #if key doesn't exist
        print("key not found")
    def print(self):
        if self.is_empty():
            print("hashmap is empty")
        for index in range(self.slots):
            if self.bucket[index] is not None:
                print(index)
                head=self.bucket[index]
                while head is not None:
                    print(head.key,"->"+head.value)
                    head=head.nxt

