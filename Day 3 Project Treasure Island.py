print("Text Adventure game dude!!")

ch=input("Find the treaser you can go left or right\n")
ch=ch.lower()

if(ch=="right"):
    print("Game Over")

elif(ch=="left"):
    ch=input("It's a boat!! do you want to swim or wait for the next one?\n")
    ch=ch.lower()
    
    if(ch=="wait"):
        print("Game Over")
    
    elif(ch=="swim"):
        ch=input("In the boat you find three boxes: red, blue, yellow which one you pick?\n")

        ch=ch.lower()
        if(ch=="yellow"):
            print("You win!!")

        else:
            print("Curse you")
            
    else:
        print("Game Over, wrong input")
    

else:
    print("Game Over, wrong input")

