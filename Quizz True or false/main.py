
from Questions import question_data
from Competitors import Competitor
from qusetionmodel import QuestionModel
from random import choice

user1 = Competitor(username="Filip")
user2 = Competitor(username="Krzysztof")
users = [user1,user2]


is_on = True
while is_on:

    for user in users:
        if len(question_data) > 0:
            rm_q = choice(question_data)
            question_data.remove(rm_q)


            new_q = QuestionModel()
            new_q.answer = rm_q['answer']
            new_q.text = rm_q['text']


            print(f"Player named: {user.username} it is your time :) \n")
            print(f"{new_q.text} True/False\n")
            user_choice = input().strip()


            if user_choice.lower() == new_q.answer.lower():
                user.score += 1
                print(f"Your Score: {user.score}\n")
            else:
                print(f"unfortunately you are wrong the correct answer is {new_q.answer}\n")

        else:
            is_on = False


winner = None
highest_score = 0
draw_check = 0  # Zmienna do liczenia liczby graczy z najwyższym wynikiem

for user in users:
    if user.score > highest_score:
        highest_score = user.score
        winner = user.username
        draw_check = 1  # Resetowanie liczby remisów do 1, gdy nowy zwycięzca
    elif user.score == highest_score:
        draw_check += 1  # Zwiększanie licznika remisów

# Sprawdzanie wyniku
if draw_check > 1:
    print(f"It's a draw between {', '.join(user.username for user in users if user.score == highest_score)} with Score: {highest_score}")
else:
    print(f"The winner is {winner} with Score: {highest_score}")

