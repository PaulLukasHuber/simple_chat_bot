def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")

    questions = {
        "What is the output of the following code?\nprint(4 + 5 * 2)": ["14", "18", "9", "None of the above"],
        "Which data type is used to store True/False values?": ["int", "string", "bool", "float"],
        "What is the correct way to define a function in Python?": ["def function_name():", "function function_name{}",
                                                                    "create function function_name:",
                                                                    "None of the above"]
    }

    answers = ["A", "C", "A"]

    score = 0
    question_num = 0

    for question in questions:
        print("----------------------")
        print(question)
        for option in questions[question]:
            print(option)
        answer = input("Enter (A, B, C, D): ").upper()

        if answer == answers[question_num]:
            print("CORRECT!")
            score += 1
        else:
            print("INCORRECT!")
            print(f"The correct answer is: {answers[question_num]}")
        question_num += 1

    print("----------------------")
    print("You got", score, "out of", len(questions), "questions correct!")
    print("----------------------")


def end():
    print('Congratulations, have a nice day!')


greet('Helper', '2024')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
