from os import listdir
from typing import List
import csv


def load_file(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()


def list_question_dir(path: str) -> List[str]:
    question_dirs = [el for el in listdir(path) if el[0] != '.']
    return question_dirs


def load_csv(path: str) -> List[str]:
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        rows = [row for row in reader]
    return rows
