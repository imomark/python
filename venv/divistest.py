lister = [x for x in range(2000,3201) if x % 7 == 0 and x % 5 != 0]
print(lister)

for i in range(2000,3201):
    if i%7 == 0 and i%5!=0:
        print(i,end=',')
print("\b")