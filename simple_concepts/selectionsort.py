mylist = [5,3,45,6,4,7,5,9,8,6,4,7]
sortedlist = []
for i in range(len(mylist)):
  lowestnum = mylist[0]
  for i in mylist:
    if i < lowestnum:
      lowestnum = i
  sortedlist.append(lowestnum)
  mylist.remove(lowestnum)
print(sortedlist)
