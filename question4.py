name = (input("Enter the name: \n"))
print(len(name))

if len(name) < 3:
    print("Name must be atleast 3 characters.")

elif len(name) > 50:
    print("Name must be atleast 50 characters long.")
    
else:
    print("Name looks good.") 
