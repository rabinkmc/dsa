data = open("study_guide.md").read().strip("\n").split("\n")
START = 31

problems = {}
for problem in data[START:]:
    if problem == "" or problem.startswith("##"):
        continue
    q_id, name = problem.split(".", 1)
    name = name.strip()
    q_id = int(q_id)
    problems[q_id] = name


print(problems)
