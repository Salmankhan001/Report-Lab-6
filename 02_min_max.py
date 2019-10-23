
list1=[]

while(1):
  a=int(input("Enter the element into the list but -1 for break="))
  if(a==-1):
    break
  else:
    list1.append(a)

print("Your list is {0}".format(list1))

print("The maximum element of list is {0}".format(max(list1)))
print("The minimum element of list is {0}".format(min(list1)))
  
