boysname = input("Enter the boy's name: ").lower()
girlsname = input("Enter the girl's name: ").lower()
flames = ['Friendship', 'Love', 'Affair', 'Marriage', 'Enemy', 'Sister']
boysnamelst = [char for char in boysname if char != ' '] #List Comprehension
girlsnamelst = [char for char in girlsname if char != ' ']
for i in boysnamelst:
    for j in girlsnamelst:
        if i==j:
            boysnamelst.remove(i)
            girlsnamelst.remove(i)
length = len(boysnamelst + girlsnamelst)
lengthofflames = len(flames)
for i in range(1, 6):
    cutnumber = length % lengthofflames
    del flames[cutnumber]
    lengthofflames -= 1
print(flames)