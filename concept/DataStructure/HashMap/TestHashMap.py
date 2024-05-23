from concept.DataStructure.HashMap.HashMap import HashMap

if __name__=="__main__":
    hash_map=HashMap()
    hash_map.put("name","shoumik")
    hash_map.put("profession", "Software Engineer")
    hash_map.put("age","28")
    # hash_map.print()
    # print(hash_map.get("age"))
    hash_map.delete("profession")
    hash_map.print()

