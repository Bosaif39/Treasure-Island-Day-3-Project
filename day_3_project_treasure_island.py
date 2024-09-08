print("Text Adventure game dude!!")

ch=input("Find the treasurer. You can go left or right.\n")
ch=ch.lower()

if(ch=="right"):
    print("Game Over")

elif(ch=="left"):
    ch=input("It's a boat!! Do you want to swim or wait for the next one?\n")
    ch=ch.lower()
    
    if(ch=="wait"):
        print("Game Over")
    
    elif(ch=="swim"):
        ch=input("On the boat you find three boxes: red, blue, yellow and which one do you pick?\n")

        ch=ch.lower()
        if(ch=="yellow"):
            print("You found the treasurer !!")

        else:
            print("Game Over")
            
    else:
        print("Game Over, wrong input")
    

else:
    print("Game Over, wrong input")
