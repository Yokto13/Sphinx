import traceback
from typing import List

from picotui.widgets import *
from picotui.menu import *
from picotui.context import Context

from models.abstract_question import AbstractQuestion
from tui.multiline_label import MultiLineLabel

import utils.io as IO
from models.questions import BasicQuestion, BasicQuestionWithStatistics
import random

import csv

# Dialog on the screen
d = None

no_answer_text: str = "No answer was set."


def load_questions(questions_path, add_stats=False):
    rows = IO.load_csv(questions_path)
    first_row = rows[0]
    questions = []
    if not 1 <= len(first_row) <= 3:
        raise TypeError("Wrong format of the CSV file. Please see README.md for more info.")
    if len(first_row) == 3:
        for row in rows:
            questions.append(BasicQuestionWithStatistics(question=row['Question'], answer=row['Answer'],
                                                         stats_raw=row['Stats']))
    else:
        for row in rows:
            question, answer, stats = [None] * 3
            if 'Question' in row:
                question = row['Question']
            if 'Answer' in row:
                answer = row['Answer']
            if 'Stats' in row:
                stats = row['Stats']
            if stats is not None or add_stats:
                questions.append(BasicQuestionWithStatistics(question=question, answer=answer, stats_raw=stats))
            else:
                questions.append(BasicQuestion(question=question, answer=answer))
    return questions


# This routine is called to redraw screen "in menu's background"
def screen_redraw(s):
    s.attr_color(C_WHITE, C_GREEN)
    s.cls()
    s.attr_reset()
    d.redraw()


def main_loop():
    while 1:
        key = m.get_input()

        if key == KEY_F1:
            b_answer_clicked(b_answer)
        elif key == KEY_F2:
            b_next_clicked(b_next)
        elif key == KEY_F3 and not b_correct.disabled:
            b_correct_clicked(b_correct)
        elif key == KEY_F4 and not b_wrong.disabled:
            b_wrong_clicked(b_wrong)
        else:
            res = d.handle_input(key)
            if res is not None and res is not True:
                return res


with Context():
    d = Dialog(10, 5, 80, 20)

    # Listboxes to choose question set and pack.
    d.add(1, 2, WLabel("Question sets:"))
    sets = "question-sets"
    set_listbox = WListBox(16, 4, IO.list_sets_dir(f"{sets}"))
    d.add(1, 3, set_listbox)

    d.add(20, 2, WLabel("Packs in QS:"))
    try:
        set_choice = IO.list_sets_dir(sets)[set_listbox.choice]
    except IndexError as e:
        raise Exception("Are you sure that you have sets in the question-sets directory?") from e

    pack_listbox = WListBox(16, 4, IO.list_packs_dir(f"{sets}/{set_choice}"))
    d.add(20, 3, pack_listbox)

    # Displays statistics if there are any.
    QALabel = MultiLineLabel("", d, 40, 2, w=40, lines=8)
    StatisticsLabel = MultiLineLabel("", d, 1, 12, w=35, lines=5)
    StatisticsLabel.set_text(
        "Statistics (if there are any) are going to be displayed here. Also some messages to the user can appear."
    )

    add_stats_checkbox = WCheckbox("Add stats if not present.")
    d.add(1,8, add_stats_checkbox)

    def b_answer_clicked(b):
        if QALabel.raw_text == current_question.question:
            if current_question.answer is None or current_question.answer == '':
                QALabel.set_text(no_answer_text)
            else:
                QALabel.set_text(current_question.answer)
            b.t = "SHOW QUESTION(F1)"
        else:
            QALabel.set_text(current_question.question)
            b.t = "SHOW ANSWER(F1)"
        b.redraw()

    def b_next_clicked(b):
        set_new_question()

    def b_correct_clicked(b):
        StatisticsLabel.set_text("Good job!")
        global answered
        answered = True
        toggle_answering()
        if hasattr(current_question, 'stats_holder'):
            if "score" in current_question.stats_holder:
                current_question.stats_holder["score"].update(True)

    def b_wrong_clicked(b):
        StatisticsLabel.set_text("Let's try another!")
        global answered
        answered = True
        toggle_answering()
        if hasattr(current_question, 'stats_holder'):
            if "score" in current_question.stats_holder:
                current_question.stats_holder["score"].update(False)

    # Buttons for controlling questions/answers.

    b_answer = WButton(19, "SHOW ANSWER(F1)")
    d.add(40, 14, b_answer)
    b_answer.on("click", b_answer_clicked)

    b_next = WButton(19, "NEXT(F2)")
    d.add(61, 14, b_next)
    b_next.on("click", b_next_clicked)

    b_correct = WButton(19, "CORRECT(F3)")
    d.add(40, 16, b_correct)
    b_correct.on("click", b_correct_clicked)

    b_wrong = WButton(19, "WRONG(F4)")
    d.add(61, 16, b_wrong)
    b_wrong.on("click", b_wrong_clicked)

    questions: List[AbstractQuestion] = None
    current_question: AbstractQuestion = None
    answered: bool = False

    def w_listbox_changed(w):
        global set_choice
        try:
            set_choice = IO.list_sets_dir(sets)[set_listbox.choice]
        except IndexError as e:
            raise Exception("Are you sure that you have sets in the question-sets directory?") from e
        pack_listbox.set_items(IO.list_packs_dir(f"{sets}/{set_choice}"))
        pack_listbox.redraw()

    def set_new_question():
        global current_question
        # Get the next question.
        # gauss favorizes lower numbers so questions with worse score are more likely to be selected.
        # TODO(D): the best way to choose question needs more consideration.
        for i in range(len(questions)):
            questions[i].last_used += 1
        questions.sort(key=lambda x: x.score)
        #question_index = -1
        #while question_index < 0 or question_index >= len(questions):
        #    question_index = abs(int(random.gauss(0, len(questions) * 0.5)))
        question_index = 0
        assert question_index < len(questions)
        current_question = questions[question_index]
        questions[question_index].last_used = 0
        QALabel.set_text(current_question.question)
        global answered
        answered = False
        b_correct.redraw()
        if b_correct.disabled:
            toggle_answering()
        b_answer.t = "SHOW ANSWER(F1)"
        b_answer.redraw()
        # If the question has statistics, display them.
        if hasattr(current_question, 'stats_holder'):
            texts = []
            for stat in current_question.stats_holder:
                texts.append(str(stat))
            StatisticsLabel.set_text(" ".join(texts))
        else:
            StatisticsLabel.set_text("No stats found.")

    def pack_listbox_changed(w):
        global questions
        try:
            pack_choice = IO.list_packs_dir(f"{sets}/{set_choice}")[w.choice]
        except IndexError as e:
            raise Exception(f"Are you sure that you have packs in the question-sets/{set_choice} directory?") from e
        questions = load_questions(f"{sets}/{set_choice}/{pack_choice}", add_stats=add_stats_checkbox.choice)
        set_new_question()

    def toggle_answering():
        """ Disables/enables wrong and correct buttons. """
        b_wrong.disabled = b_correct.disabled ^ 1
        b_correct.disabled = b_correct.disabled ^ 1
        b_correct.redraw()
        b_wrong.redraw()

    w_listbox_changed(set_listbox)
    pack_listbox_changed(pack_listbox)

    set_listbox.on("changed", w_listbox_changed)
    pack_listbox.on("changed", pack_listbox_changed)
    add_stats_checkbox.on("changed", lambda x: pack_listbox_changed(pack_listbox))

    #toggle_answering()

    screen_redraw(Screen)
    Screen.set_screen_redraw(screen_redraw)

    m = WMenuBar([])
    m.permanent = True
    m.redraw()

    # Ensures that statistics are saved on Interrupt.
    try:
        res = main_loop()
    except KeyboardInterrupt:
        StatisticsLabel.set_text("Initing shutdown.")
        StatisticsLabel.set_text("Saving work...")
    finally:
        if hasattr(questions[0], 'stats_holder'):
            pack_choice = IO.list_packs_dir(f"{sets}/{set_choice}")[pack_listbox.choice]
            with open(f"{sets}/{set_choice}/{pack_choice}", 'w') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow(["Question", "Answer", "Stats"])
                for q in questions:
                    writer.writerow([q.question, q.answer, q.stats_holder.dump()])
        StatisticsLabel.set_text("Everything Saved.")
