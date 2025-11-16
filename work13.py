item = input("Enter the name of new item:")
f = open("items.txt","a")
f.write(item +"\n")
f.close()

print("\nList of items:")
f = open("items.txt","r")
print(f.read())
f.close()