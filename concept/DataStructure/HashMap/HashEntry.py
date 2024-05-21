class HashEntry:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.nxt=None
    def __str__(self):
        return str(self.key)+" "+self.value