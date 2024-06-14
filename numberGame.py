import random

print(" Welcome to the Number Guessing Game !\n ")

#Ask User For name 

user_name = input("please enter your name : ")
user_name = user_name.capitalize().strip()

#opt out quiting or starting 

question = input("Do want to continue Yes/No ? ")
question = question.lower().strip()

if question != "yes":
    quit()
else :
   print(f"Welcome {user_name}, lets get started :)")

#user inputs range 
range_of_guess = int(input("please enter a number that is above 0  :\n"))

if range_of_guess <= 0 :
    print("please enter a valid number")
    quit()
else:
    print("Thank you !! ")

number_guessed = int(input("please enter any number within your given range :\n "))

random_number = random.randrange(0 , range_of_guess)
if(random_number == number_guessed):
    print("you got it !")
elif number_guessed > random_number :
    print( "you have guessed a little over the number ")
else :
    print("your guess was way too low ")

    ### unfinished