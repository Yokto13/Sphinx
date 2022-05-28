import os
from typing import List, Dict
import csv


def load_file(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()


def list_sets_dir(path: str) -> List[str]:
    question_dirs = sorted([el for el in os.listdir(path) if el[0] != '.' and os.path.isdir(path + '/' + el)])
    return question_dirs


def list_packs_dir(path: str) -> List[str]:
    question_dirs = sorted([el for el in os.listdir(path) if el[-3:] == 'csv'])
    return question_dirs


def load_csv(path: str) -> List[Dict[str, str]]:
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        rows = [row for row in reader]
    return rows
