print("Welcome to the quiz game")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Come on...Let's play")
score = 0

answer = input("What is the capital of Canada? ")
if answer.lower() == "ottawa":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is the capital of India? ")
if answer.lower() == "delhi":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is the capital of Germany? ")
if answer.lower() == "berlin":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is the capital of Italy? ")
if answer.lower() == "rome":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " answers correctly")
print("You got " + str((score/4) * 100) + "%")