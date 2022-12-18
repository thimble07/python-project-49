import random
import prompt


# функция привествия!
def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


# функция вопроса
def question():
    n = random.randint(1, 100)
    return n


# функция ответа
def answer_user():
    answer = input('Your answer: ')
    return answer


# функция проверки
def chek_answer(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return 'no'
    return 'yes'


def game():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0

    while count < 3:
        ques = question()
        print(f'Question: {ques}')
        answ = answer_user()
        chek = chek_answer(ques)
        if answ == chek:
            print('Correct!')
            count = count + 1
        else:
            return print(f"{answ} is wrong answer ;(. Correct answer was {chek}.\nLet's try again, {name}!")
    return print(f'Congratulations, {name}!')
