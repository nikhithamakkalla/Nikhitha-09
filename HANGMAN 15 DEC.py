import time

name = input("what is youn name? ")

print ("Hello, " + name, "Time to play hangman Game!")

time.sleep(1)

print ("Start guessing...")
time.sleep(0.5)

word = ("python")

guesses = 'p'

turns = 4

while turns > 0:         

    
    failed = 0             

    
    for char in word:      

    
        if char in guesses:    
    
        
            print (char,end=""),    

        else:
    
        
            print ("_ ",end=""),     
       
        
            failed += 1    

    
    if failed == 0:        
        print (" You Guess the correct word")
    
        break            
    
    guess = input("guess a character:") 

    
    guesses += guess                    

    
    if guess not in word:  
 
     
        turns -= 1        
 
    
        print ("Wrong")  
 
    
        print ("You have", + turns, 'more guesses' )
 
    
        if turns == 0:           
    
        
            print(" You Lose")
