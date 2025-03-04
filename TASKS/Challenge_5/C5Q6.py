#Print 20 to 25 without 22

i=20
while i<26:
    if i==22:
        i+=1
        continue
    else:
        print(i)
        i+=1
