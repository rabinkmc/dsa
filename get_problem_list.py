import argparse
import requests

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


def get_question_link_by_difficulty(contest_id, difficulty):
    question = get_questions(contest_id)[difficulty]
    link = contest_link(contest_id, question["title_slug"])
    return link

def get_contest_files(contest_id):
    questions = get_questions(contest_id)
    for index, question in enumerate(questions):
        filepath = file_path(question["question_id"], question["title_slug"], contest_id)
        write_file(contest_id, index)

def get_filename(contest_id, difficulty):
    question = get_questions(contest_id)[difficulty]
    filepath = file_path(question["question_id"], question["title_slug"], contest_id)
    return filepath

def generate_problem_list(until, no_of_problems):
    for contest_id in range(until - no_of_problems + 1, until+1):
        print(get_question_link_by_difficulty(contest_id, MEDIUM_HARD))

def generate_medium_problems(until, no_of_problems):
    for contest_id in range(until - no_of_problems + 1, until+1):
        questions = get_questions(contest_id)
        print(contest_link(contest_id, questions[0]["title_slug"]))
        print(contest_link(contest_id, questions[1]["title_slug"]))

def write_file(path, content):
    fp = open(path, "w")
    fp.write(content)
    fp.close()

def generate_files(until):
    for contest_id in range(until - NO_OF_PROBLEMS + 1, until+1):
        difficulty = MEDIUM_HARD
        link = get_question_link_by_difficulty(contest_id, difficulty)
        filepath = get_filename(contest_id, difficulty)
        write_file(filepath, "# " + link)
        print(filepath)


def contest_problems(contest_id):
    questions = get_questions(contest_id)
    for question in questions:
        link = contest_link(contest_id, question["title_slug"])
        content = "# " + link
        filepath = file_path(question["question_id"], question["title_slug"], contest_id)
        write_file(filepath, content)
        print(filepath)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(
        prog="leetcode cli",
        description="Helpful cli tool for leetcode",
    )
    argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
    argsubparsers.required = True
    contest_sp = argsubparsers.add_parser(
        "contest", help="get problems from contest"
    )
    contest_sp.add_argument(
        "contest_id",
        help="The id of the weekly contest",
    )

    args = argparser.parse_args()
    match args.command:
        case "contest":
            contest_problems(args.contest_id)
