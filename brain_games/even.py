import random
import prompt


# функция привествия!
def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def question():
    n = random.randint(1, 100)
    return n


# функция ответа
def answer_user():
    answer = input('Your answer: ')
    return answer


# функция проверки
def chek_answer(x):
    if x % 2 == 0:
        return 'yes'
    elif x % 2 != 0:
        return 'no'


def game():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 1

    while count <= 3:
        ques = question()
        print(f'Question: {ques}')
        answ = answer_user()
        chek = chek_answer(ques)
        if answ == chek:
            print('Correct!')
            count = count + 1
        else:
            print(f"{answ} is wrong answer ;(. Correct answer was {chek}.")
            return print(f"Let's try again, {name}!")
    return print(f'Congratulations, {name}!')
