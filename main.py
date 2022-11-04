import random

num = 0

def generate_random_number():
  return random.randint(1,10)


def different_from_answer(guess, answer):
  answer = int(answer)
  if guess == answer:
    return 'Correct'
  elif guess > answer:
    return 'Too high'
  elif guess < answer:
    return 'Too low'


def make_a_guess(answer):
  guess = int(input("Make a guess: "))
  if type(guess):
    return different_from_answer(guess, answer)
  else:
    print("Not an integer")
    return make_a_guess(answer)