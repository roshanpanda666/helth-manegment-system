print("welcome to my health management system ")
while True:
    lock=input("what do you want to lock exercise or food ?\n")
    if(lock=="exercise"):

        name=input("who do you want to lock for type the name\n")
        f=open("name.txt","a")
        f.write(name)
        print("you have success fully written the name \n")
        print("you have chosen "+name,"and you have locked "+lock)

        exe=input("\n now type the name of the exercise exercise ")
        f=open("exercise.txt","a")
        f.write(exe)
        print(" you have success fully written "+exe)

    if(lock=="food"):

        name=input("who do you want to lock for type the name\n")
        f=open("name.txt","w")
        f.write(name)
        print("you have success fully written the name \n")
        print("you have chosen "+name,"and you have locked "+lock)
        

        food=input("\n now type the name of the food he/she had eaten")
        f=open("food.txt","w")
        f.write(food)
        print(" you have success fully written "+food)
    else:
        print("enter properly exercise or food ? ")


