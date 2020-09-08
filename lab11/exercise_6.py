# guess rand num between 1 to 100, fake answer randomly
from random import randint

fake_answer_ratio = 0.1
rand_num = randint(1,100)


def should_i_fake_it(ratio):
    return False if randint(1, 100) > (ratio*100) else True


def guess():
    while True:
        try:
            return int(input("Guess which number I chose..."))
        except Exception:
            print("Please choose numbers")


answer = guess()
while answer != rand_num:
    if should_i_fake_it(fake_answer_ratio):
        print("Aim lower" if answer < rand_num else "Aim higher")
    else:
        print("Aim lower" if answer > rand_num else "Aim higher")
    answer = guess()

print("That's right!")



