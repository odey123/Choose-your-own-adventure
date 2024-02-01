import os
os.system ('cls')

answer = input("you are on an untared road, it has come to an end. You can go left or right. where do you want to go: ").lower()

if answer == "left":
    answer = input("You have reached a brick wall. press climb to climb it or press around to go around  it: ").lower()

    if answer == "climb":
        quit(print("Birds pushed you down and you died"))
    elif answer == "around":
        answer = input("you have reached a river. press swim to swim or press ride to ride a boat across: ").lower()

        if answer == "swim":
            quit(print("crocodiles ate you"))
        elif answer == "ride":
            answer = input("you reached the other side. Do you want to trek or steal a car (trek/steal): ").lower()

            if answer == "steal":
                quit(print("The police caught you"))
            elif answer == "trek":
                answer = input("You got home but your feet were sore. do you want to go to the spa or use cheap cosmetics(spa/cosmetics): ").lower()

                if answer == "cosmetics":
                    quit(print("Because they were cheap they gave you skin irritation"))
                elif answer == "spa":
                    answer = input("you do not have any money to pay. Do you want to borrow or steal (borrow/steal): ").lower()

                    if answer == "steal":
                        answer = input("you able to steal but police caught you. Do you want to be imprisoned🔐 or escape 🏃‍♂️ (imprisonment/escape): ").lower()

                        if answer == "imprisonment":
                            quit(print("you still tried to escape and they flogged you to death for trying to escape😵"))
                        elif answer == "escape":
                            quit(print("you were not able to escape and they flogged you to death for trying to escape😵"))
                        else:
                            quit(print(" Not a valid option. You lose."))

                    elif answer == "borrow":
                        print("people were too stingy to give you money so the spa ask you to wash the plate of the next restaurant so that the restaurant will pay the money for you: ").lower()
                        print("you won!!!🏆")
                        
                    else:
                        quit(print(" Not a valid option. You lose."))
                    

            else:
                quit(print(" Not a valid option. You lose."))
            
        else:
            quit(print(" Not a valid option. You lose."))
    else:
        quit(print(" Not a valid option. You lose."))

elif answer == "right":
    quit(print("you lost, you entered a dead end."))
else:
    quit(print(" Not a valid option. You lose."))