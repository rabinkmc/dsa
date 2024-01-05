from datetime import date, timedelta
import sys
YEAR = 2024
scores = {
    date(YEAR, 1, 4): (0, 10, 0)
}
def get_day_score(date):
    return sum(scores[date])

def no_of_days(scores):
    return len(scores)

def avg_score(scores):
    days_count = no_of_days(scores)
    total_score = 0
    for date in scores:
        score = get_day_sore(date)
        total_score += score
    return (total_score) / (days_count * 100)

def total_scores(scores):
    total_score = []
    total = 0
    for date in scores:
        score = get_day_sore(date)
        total += score
        total_score.append(total)
    return total

if __name__ == "__main__":
    score = get_day_score(date.today()-timedelta(days=1))
    print(f"{score}/100")
