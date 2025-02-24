mylist = [2,1,3,4,5,6,7]
for i in range(len(mylist)):
  flag = 0
  for j in range(i+1, len(mylist)):
    if mylist[i] > mylist[j]:
      mylist[i], mylist[j] = mylist[j], mylist[i]
      flag = 1
  print(mylist)
  if flag == 0:
    break
