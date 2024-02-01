import os
os.system ('cls')
print("Welcome to the riddle quiz")

while True:
    answer = input('Do you want to play (yes/no): ').lower()

    if answer == 'yes':
        print("Okay! Let's play")
        break
    elif answer == 'no':
        quit(print('Bye!'))
    else:
        print('Not a valid option try again')
        continue

score = 0
1
answer = input("1. What do you call animals with scales: ")
if answer.lower() == "reptiles":
    print("correct!")
    score += 1
else:
    print("incorrect. The correct answer is reptiles.")
2
answer = input("2. What do you call animals that do not lay eggs: ")
if answer.lower() == "mammals":
    print("correct")
    score += 1
else:
    print("incorrect. The correct answer is mammals.")

3
answer = input("3. What do you call animals that lay eggs but do not have scales: ")
if answer.lower() == "amphibians":
    print("correct!")
    score += 1
else:
    print("incorrect. The correct answer is amphibians.")
4
answer = input("4. What do you call things that do not have life in them: ")
if answer.lower() == "non living things":
    print("correct!")
    score += 1
else:
    print("incorrect. The correct answer is non living things.")
5
answer = input("5. What do you call things that have life in them: ")
if answer.lower() == "living things":
    print("correct!")   
    score += 1
else: 
    print("incorrect. The correct answer is living things.")
6
answer = input("6. If something does not use wire to be connected what do you call it: ")
if answer.lower() == "wireless":
    print("correct!")
    score += 1
else: 
    print("incorrect. The correct answer is wireless.")
7
answer = input("7. If something uses wire to be connected what do you call it:  ")
if answer.lower() == "wired":
    print("correct!")
    score += 1
else: 
    print("incorrect. The correct answer is wired.")
8
answer = input("8. what do you call what you sit on: ")
if answer.lower() == "a chair":
    print("correct!")
    score += 1
else: 
    print("incorrect. The correct answer is a chair.")
9
answer = input("9. As sly as a : ")
if answer.lower() == "fox":
    print("correct!")
    score += 1
else: 
    print("incorrect. The correct answer is fox.")
10
answer = input("10. what is full meaning of NTA: ")
if answer.upper() == "NIGERIA TELEVISION AUTHORITY":
    print("correct!")
    score += 1
else: 
    print("incorrect. The correct answer is Nigeria Television Authority.")

print("you got " + str((score / 10) * 100) + "%.")


    


