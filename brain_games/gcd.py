import random
import prompt
import math


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


def game():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    count = 1

    while count <= 3:
        number_one = question()
        number_two = question()
        print(f'Question: {number_one} {number_two}')
        answ = answer_user()
        chek = math.gcd(number_one, number_two)
        if int(answ) == chek:
            print('Correct!')
            count = count + 1
        else:
            return print(f"{answ} is wrong answer ;(. Correct answer was {chek}.\nLet's try again, {name}!")
    return print(f'Congratulations, {name}!')
