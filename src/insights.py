from src.jobs import read


def get_unique_job_types(path):
    datas = read(path)
    conj = set()
    for data in datas:
        if data['job_type'] != '':
            conj.add(data['job_type'])
    return conj


def filter_by_job_type(jobs, job_type):
    _list = []
    for job in jobs:
        if job['job_type'] == job_type:
            _list.append(job)
    return _list


def get_unique_industries(path):
    datas = read(path)
    conj = set()
    for data in datas:
        if data['industry'] != '':
            conj.add(data['industry'])
    return conj


def filter_by_industry(jobs, industry):
    _list = []
    for job in jobs:
        if job['industry'] == industry:
            _list.append(job)
    return _list


def get_max_salary(path):
    datas = read(path)
    values = set()
    for job in datas:
        if job['max_salary'] != '' and job['max_salary'].isdigit():
            values.add(int(job['max_salary']))
    return max(values)


def get_min_salary(path):
    datas = read(path)
    values = set()
    for job in datas:
        if job['min_salary'] != '' and job['min_salary'].isdigit():
            values.add(int(job['min_salary']))
    return min(values)


def matches_salary_range(job, salary):
    if (
        'min_salary' not in job or 'max_salary' not in job
        or type(job['min_salary']) != int or type(job['max_salary']) != int
        or job['min_salary'] > job['max_salary'] or type(salary) != int
    ):
        raise ValueError
    else:
        return job['min_salary'] <= salary <= job['max_salary']


def filter_by_salary_range(jobs, salary):
    new_list = [count_ocurrences]
    for job in jobs:
        if matches_salary_range(job, salary):
            new_list.append(job)
    return new_list
