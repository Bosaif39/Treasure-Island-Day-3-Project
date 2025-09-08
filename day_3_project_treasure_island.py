print("Text Adventure game dude!!")

choice=input("Find the treasurer. You can go left or right.\n")
choice=choice.lower()

if(choice=="right"):
    print("Game Over")

elif(choice=="left"):
    choice=input("It's a boat!! Do you want to swim or wait for the next one?\n")
    choice=choice.lower()
    
    if(choice=="wait"):
        print("Game Over")
    
    elif(choice=="swim"):
        choice=input("On the boat you find three boxes: red, blue, yellow and whichoice one do you pick?\n")

        choice=choice.lower()
        if(choice=="yellow"):
            print("You found the treasurer !!")

        else:
            print("Game Over")
            
    else:
        print("Game Over, wrong input")
    

else:
    print("Game Over, wrong input")

