import random
import prompt

# функция привествия!
def welcome_user(name):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

# функция рандомного значения
def random_numbers():
    return random.randint(1, 50)

# функция рандомного действия
def operation():
    operation = ("+", "*", "-")
    return operation[random.randint(0, 2)]

def game():
    print('Welcome to the Brain Games!')
    name = welcome_user('Vova')
    print('What is the result of the expression?')
    count = 1
    while count <= 3:
        num_one = random_numbers()
        num_two = random_numbers()
        operator = operation()
        result = 0
        print("Question: " + str(num_one) + " " + operator + " " + str(num_two))
        answer = input("Your answer: ")
        if operator == "+":
            result = num_one + num_two
        elif operator == '*':
            result = num_one * num_two
        elif operator == '-':
            result = num_one - num_two
        if int(answer) == result:
            print("Correct!")
        else:
            print(f"{answer}  is wrong answer ;(. Correct answer was {result}")
            return f"Let's try again, {name}!"
        count += 1
    return print(f"Congratulations, {name}!")


