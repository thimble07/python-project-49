import random
import prompt


# функция привествия!
def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


# функция ответа
def answer_user():
    answer = input('Your answer: ')
    return answer


def game():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What number is missing in the progression?')
    count = 1

    while count <= 3:
        step = random.randint(2, 10)
        start = random.randint(1, 10)
        n = list(range(start, 70, step))
        numb = random.randint(1, len(n) - 1)
        a = n[numb]
        n[numb] = '..'
        ques = ''.join(str(x) + ' ' for x in n)
        print('Question: ' + ques)
        answ = answer_user()
        chek = a
        if int(answ) == chek:
            print('Correct!')
            count = count + 1
        else:
            return print(f"{answ} is wrong answer ;(. Correct answer was {chek}.\nLet's try again, {name}!")
    return print(f'Congratulations, {name}')
