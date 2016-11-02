
doors = [False] * 100

for i in range(100):    #100 passing by the hallway
    for j in range(i, 100, i+1):   #number of steps every time change +1
        doors[j] = not doors[j]   #if door is closed open it - if open closed it

print("The following doors are open: ", end="")  #'end' for  print in the same line
for index, value in enumerate(doors):
    if value == True:
        if index == len(doors) - 1:  #if index matches 99 print without ','
            print(index + 1)
        else:
            print(index + 1, end=", ")
