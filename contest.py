import os
from pathlib import Path
folder,*problems  = open("contest.md").read().strip("\n").split("\n")
contest_dir = folder.split("#")[-1].strip()
path = Path(f"contests/{contest_dir}")

path.mkdir(exist_ok=True)

for problem in problems:
    name = problem.split(".")[-1].strip().lower().replace(" ", "-") + ".py"
    print(path / name)



