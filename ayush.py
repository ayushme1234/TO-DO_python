start=int(input("Enter the starting number: "))
end=int(input("Enter the ending number: "))
skip=int(input("Enter the number to skip: "))
for i in range(start, end+1):
    if i%skip==0:
        continue
    print(i ,end=' ')