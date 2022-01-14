"""
This is currently WIP.
Please use main_tui.py instead. I think it is much better to use it with TUI.
I'm planning to do the raw version here, but right now it's not a priority.


import utils.io as IO
from models.questions import BasicQuestion

print(IO.list_question_dir("question_sets"))
question_set_path = input("Choose question set: ")
question_set_path = "question_sets/" + question_set_path
print(IO.list_question_dir(question_set_path))
questions_path = input("Choose questions: ")
questions_path = question_set_path + '/' + questions_path
rows = IO.load_csv(questions_path)
header = rows[0]
questions = []
if len(header) == 3:
    # stats
    pass
else:
    for row in rows:
        questions.append(BasicQuestion(row[0], row[1]))

print(questions)
for q in questions[:5]:
    print(q.question)
    print(q.answer)
"""