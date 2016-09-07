# Create a program that prompts the user ten times for a test score between 60 and 100. Each time a score is generated, your program should display what is the grade of that score. Here is the grade table:

# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

def score():
    counter = 10
    while counter > 0:
        grade = input("What is your grade? ")
        counter -= 1
        if grade < 69:
            print("Score is {}; Your grade is D".format(grade))
        elif grade < 79:
            print("Score is {}; Your grade is C".format(grade))
        elif grade < 89:
            print("Score is {}; Your grade is B".format(grade))
        elif grade <= 100:
            print("Score is {}; Your grade is A".format(grade))
    else:
        print("End of the program. Bye!")

score()
