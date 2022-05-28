from QuestLib import Question1

qustion_prompts = [
    "what colors are apple?\n (a) red/grean\n (b) purple\n (c) orange\n\n",
    "what colors are bananas?\n (a) teal\n (b) magenta\n (c) yellow\n\n",
    "what colors are strawberries\n (a) yellow \n (b) red\n (c) blue\n\n"
]

question = [
    Question1(qustion_prompts[0], "a"),
    Question1(qustion_prompts[1], "c"),
    Question1(qustion_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.quest)
        if answer == question.answer:
            score += 1
    print("you got" + str(score) + "/" + str(len(questions)) + "correct!")

run_test(question)