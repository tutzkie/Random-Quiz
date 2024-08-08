#---------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print('---------------------------')
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D) ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)

#---------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

#---------------------------
def display_score(correct_guesses, guesses):
    print('---------------------------')
    print("RESULTS")
    print('---------------------------')
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

#---------------------------
def play_again():

    response = input("do you want to play again? (Yes or No?): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
#---------------------------

questions = {
    "What is the top 1 University in the Philippines?: ": "B",
    "What is the capital of Malaysia?: ": "C",
    "Who discovered the theory of relativity": "A",
    "What shape is the Earth?: ": "A",
}

options = [["A. University of Santo Tomas","B. University of the Philippines","C. Ateneo De Manila University", "D. De La Salle University"],
           ["A. Bangkok","B. Tokyo","C. Kuala Lumpur","D. Beijing"],
           ["A. Albert Einstein", "B. Isaac Newton", "C. Marie Curie", "D. Nikola Tesla"],
           ["A. Obloid-Spheroid","B. Round","C. Flat","D. Heart"]]

new_game()

while play_again():
    new_game()
print("---------------------------")
print("Thank you for playing!")
