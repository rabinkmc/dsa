import requests
import sys


def api_url(contest_id):
    return f"https://leetcode.com/contest/api/info/weekly-contest-{contest_id}"


def contest_link(contest_id, question_slug):
    return f"https://leetcode.com/contest/weekly-contest-{contest_id}/problems/{question_slug}/"

def file_path(question_id, question_slug, contest_id):
    return f"{question_id}-{question_slug}-{contest_id}.py"

EASY = 0
MEDIUM_EASY = 1
MEDIUM_HARD = 2
HARD = 3
NO_OF_PROBLEMS = 5


def get_questions(contest_id):
    contest_url = api_url(contest_id)
    return requests.get(contest_url).json()["questions"]


def get_all_questions(contest_id):
    questions = get_questions(contest_id)
    links = []
    for question in questions:
        link = contest_link(contest_id, question["title_slug"])
        links.append(link)
    return links


def get_question_by_difficulty(contest_id, difficulty):
    question = get_questions(contest_id)[difficulty]
    link = contest_link(contest_id, question["title_slug"])
    return link

def get_filename(contest_id, difficulty):
    question = get_questions(contest_id)[difficulty]
    link = file_path(question["question_id"], question["title_slug"], contest_id)
    return link

def generate_problem_list(until):
    for contest_id in range(until - NO_OF_PROBLEMS + 1, until+1):
        print(get_question_by_difficulty(contest_id, MEDIUM_HARD))

def generate_files(until):
    for contest_id in range(until - NO_OF_PROBLEMS + 1, until+1):
        path = get_filename(contest_id, MEDIUM_HARD)
        fp = open(path, "w")
        link = "# " + get_question_by_difficulty(contest_id, MEDIUM_HARD)
        fp.write(link)
        fp.close()
        print(path)



if __name__ == "__main__":
    upto_week_id = int(sys.argv[1])
    generate_files(upto_week_id)
