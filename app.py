print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay!, Let's play\n")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!")

thread = input("What does GPU stand for? ")
if thread.lower() == "graphics processing unit":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!")

spinster = input("What does RAM stand for? ")
if spinster.lower() == "random access memory":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!")

coolant = input("What does PSU stand for? ")
if coolant.lower() == "power supply":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!")

print("you got " + str(score) + " questions of 4 correct. ")
print("you got " + str(score / 4 * 100) + "%.")
