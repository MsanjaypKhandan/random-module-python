import random
list1 = ["Today willl be a lucky day","You will meet someone new and interesting","Watch out for obstacles in your path"] 
ch=int(input("Enter the choice"))
if(ch==1):
   print(random.choice(list1))
elif(ch==2):
   print(random.choice(list1))
elif(ch==3):
   print(random.choice(list1))


else:
  exit()