# Sphinx
software to practice active-recall questions.

## FAQ
### What is active-recall?
Method of learning based on recalling information from memory.
It's beneficial to your long-term memory and also more enjoyable than reading notes again and
again.

### How to use this method?
Study. Get/create questions. Practice questions. Sleep. Repeat.

### How to use Sphinx?
- clone the repo
- install requirements
- get questions (more on that in the following two questions)
- run 
``` python main_tui.py ```

### How to create questions?
Right now the software expects csv files of the following format.

2 or 3 columns.

The first row is a header that can contain pretty much anything 
but I use (Question, Answer, Stats).
On each row, there is a question, followed byan answer and optionally stats.

When you create questions just create a csv file with question-answer pairs.
Stats are generated automatically when the corresponding checkbox is ticked 
when using the Sphinx.

You can look into question-sets for a sample csv file.

### I don't want to create questions!
That's fine.
You can you some of the questions I have already created during my prep for exams.
Just call
```git submodule init
git submodule update
```
and you are ready to go!
But be aware of the fact that the majority of questions there is in Czech 
and they are useful mainly for students of MFF CUNI.

### Can I create/edit my own question-pack in the software?
Nope. I played with the idea but came to the conclusion that editing question-packs is 
easier to do with some editor already designed to work with csvs. 
I currently see it as reinventing the wheel.
But nonetheless, I may change my mind in the future.

### How stats work?
As of today, the Sphinx can store the number of correct/total attempts for each question.
If this is enabled it prioritizes questions with more wrong answers so you can practice them.

### I found a bug! What should I do?
Create an issue or if you feel like it fix it and do a PR. Thanks :)

## Screenshot
![screenshot](screenshot.png)
