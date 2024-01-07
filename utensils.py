
#set=no duplicate values
utensils ={"ali","bba","com","com","cup"}
dishes = {"bol","plate",'cup'}


#utensils.add("hari")
utensils.remove('bba')
#dishes.update(utensils)
#dishes_table = utensils.union(dishes)

print(dishes.difference(utensils))
print((utensils.intersection(dishes)))

#for x in utensils:
 #   print(x)



