list1=[]
list2=[]
for i in range(1,100):
    list1.append(i)
    if i%3==0:
        list2.append(i)

print(list2)


list3 = [i for i in range(1,100) if i%3==0]
print(list3)