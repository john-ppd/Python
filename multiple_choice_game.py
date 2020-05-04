import mult_choice_game_custom_classes
question_prompts = [
"what is your dogs name?",
"what is your name?"
]
questions = [
    mult_choice_game_custom_classes.QA(question_prompts[0], "lucy"),
    mult_choice_game_custom_classes.QA(question_prompts[1], "john")
]
print(questions[0].question)
print(questions[1].answer)

def run_test(questions1):
    score = 0
    #i is the object memory location, the for loops will loop through all objects here
    for i in questions1:
        answer = input(i.question)
        print(i)
        print(i.answer)
        if answer == i.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(questions1)) + " correct")

run_test(questions)
