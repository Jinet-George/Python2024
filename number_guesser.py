import random
# print(random.randrange(start,stop))
# print(random.randint(start,stop))
top_of_number= input("TYPE A NUMBER: ")
if top_of_number.isdigit():
    top_of_number = int(top_of_number)

    if top_of_number <= 0:
        print('please type a number larger than 0')
        quit()
else:
    print('please type a NUMBER')
    quit()

random_number = random.randint(0, top_of_number)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print('please type a NUMBER')
        continue
    if user_guess == random_number:
        print("You got it!!!!!!!!!!!!!!!!!")
        break
    else:
        print("You got it wrong!")
print("you got it in", guesses, "guesses")
    