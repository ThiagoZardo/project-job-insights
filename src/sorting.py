import math
from datetime import date


def max_salary_key(job):
    try:
        return int(job["max_salary"])
    except (KeyError, TypeError, ValueError):
        return -math.inf


def min_salary_key(job):
    try:
        return int(job["min_salary"])
    except (KeyError, TypeError, ValueError):
        return math.inf


def date_posted_key(job):
    try:
        return date.fromisoformat(job["date_posted"])
    except (KeyError, TypeError, ValueError):
        return date.min


def sort_by(jobs, criteria):
    criteria_keys = {
        "date_posted": date_posted_key,
        "max_salary": max_salary_key,
        "min_salary": min_salary_key,
    }

    try:
        key = criteria_keys[criteria]
    except KeyError:
        raise ValueError(f"invalid sorting criteria: {criteria}")

    reverse = criteria in ["max_salary", "date_posted"]

    jobs.sort(key=key, reverse=reverse)
